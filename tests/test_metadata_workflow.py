import base64
import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
sys.path.insert(0, str(ROOT / 'tests'))
import metadata_workflow as workflow
from test_metadata import EXAMPLE, SCHEMA, metadata, submission


class FakeSource:
    def __init__(self, issue):
        self.issue = issue
        self.comments = []

    def pages(self, path):
        return iter(self.comments)

    def request(self, method, path, data=None):
        if method == 'GET':
            if '/contents/' in path:
                return {'encoding': 'base64', 'content': base64.b64encode(b'Current issue form').decode(), 'size': 18}
            if path == '/repos/nmfs-ost/FIT-test-quality-checks':
                return {'default_branch': 'main'}
            return self.issue
        if method == 'POST':
            self.comments.append({'id': len(self.comments) + 1, 'user': {'login': 'github-actions[bot]'}, 'body': data['body']})
        elif method == 'PATCH':
            comment_id = int(path.rsplit('/', 1)[1])
            next(comment for comment in self.comments if comment['id'] == comment_id)['body'] = data['body']


class FakeTarget:
    def __init__(self):
        self.tasks = []
        self.assigned = []
        self.assignment_fails = False
        self.pr = None
        self.files = []
        self.generated = {}

    def pages(self, path):
        if '/timeline' in path:
            return iter([{'event': 'cross-referenced', 'source': {'issue': {'pull_request': {
                'url': f'https://api.github.com/repos/{workflow.TARGET}/pulls/12',
            }}}}] if self.pr else [])
        if '/files' in path:
            return iter(self.files)
        return iter(self.tasks)

    def file(self, path, ref):
        if path == 'schema_model_list.json':
            return json.dumps(SCHEMA)
        if ref == 'head':
            return json.dumps(self.generated)
        raise workflow.ApiError(404, path)

    def request(self, method, path, data=None):
        if path == '/graphql':
            if 'convertPullRequestToDraft' in data['query']:
                self.pr['draft'] = True
                return {'data': {'convertPullRequestToDraft': {'pullRequest': {'isDraft': True}}}}
            return {'data': {'repository': {'suggestedActors': {'nodes': [{'login': 'copilot-swe-agent'}]}}}}
        if path == '/user':
            return {'login': 'coordinator'}
        if path.endswith('/commits/main'):
            return {'sha': 'base'}
        if path == f'/repos/{workflow.TARGET}':
            return {'default_branch': 'main'}
        if path.endswith('/assignees'):
            self.assigned.append(data)
            if self.assignment_fails:
                raise workflow.ApiError(403, path)
            self.tasks[0]['assignees'] = [{'login': 'copilot-swe-agent[bot]'}]
            return self.tasks[0]
        if method == 'POST':
            self.tasks.append({'number': 7, 'body': data['body'], 'state': 'open',
                               'html_url': 'https://github.com/target/issues/7', 'assignees': []})
            return self.tasks[-1]
        if '/pulls/' in path:
            return self.pr
        return self.tasks[0]


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.repository = 'nmfs-ost/FIT-test-quality-checks'
        self.issue = {'number': 47, 'body': submission(), 'html_url': 'https://github.com/source/issues/47'}
        self.source = FakeSource(self.issue)
        self.target = FakeTarget()

    def dispatch(self):
        workflow.dispatch(self.source, self.target, self.repository, self.issue)

    def add_pr(self, extra_file=False):
        self.target.pr = {
            'number': 12, 'body': workflow.source_marker(self.repository, 47), 'state': 'open',
            'node_id': 'PR_node', 'draft': True,
            'html_url': 'https://github.com/target/pull/12', 'user': {'login': 'copilot-swe-agent[bot]'},
            'head': {'sha': 'head', 'repo': {'full_name': workflow.TARGET}},
            'base': {'sha': 'base', 'ref': 'main', 'repo': {'full_name': workflow.TARGET}},
        }
        self.target.files = [{'filename': 'model_list_dir/FishPath.json', 'status': 'added'}]
        if extra_file:
            self.target.files.append({'filename': '.github/workflows/unwanted.yml', 'status': 'added'})
        self.target.generated = {**EXAMPLE, 'FIT_reviewed': 'In_Progress'}

    def test_assignment_and_idempotency(self):
        self.dispatch()
        self.dispatch()
        self.assertEqual(len(self.target.tasks), 1)
        self.assertEqual(len(self.target.assigned), 1)
        self.assertEqual(self.target.assigned[0]['agent_assignment']['target_repo'], workflow.TARGET)
        self.assertIn('DRAFT', self.target.tasks[0]['body'])
        self.assertIn('Current issue form', self.target.tasks[0]['body'])
        self.assertIn(json.dumps(self.issue['body']), self.target.tasks[0]['body'])
        self.assertNotIn('Prepared metadata', self.target.tasks[0]['body'])
        self.assertIn('metadata task', self.source.comments[0]['body'])

    def test_assignment_failure_reuses_task(self):
        self.target.assignment_fails = True
        with self.assertRaises(workflow.ApiError):
            self.dispatch()
        self.target.assignment_fails = False
        self.dispatch()
        self.assertEqual(len(self.target.tasks), 1)
        self.assertEqual(len(self.source.comments), 1)

    def test_free_form_submission_is_sent_to_agent(self):
        self.issue['body'] = 'A new form layout with fields for the agent to interpret.'
        self.dispatch()
        self.assertEqual(len(self.target.tasks), 1)
        self.assertIn(self.issue['body'], self.target.tasks[0]['body'])
        self.assertIn('Never invent facts', self.target.tasks[0]['body'])

    def test_validated_pr_and_repeated_checks(self):
        self.dispatch()
        self.add_pr()
        self.dispatch()
        _, state = workflow.find_state(self.source, self.repository, 47)
        self.assertEqual(state['status'], 'validated')
        self.assertEqual(state['validated_head'], 'head')
        body = self.source.comments[0]['body']
        self.dispatch()
        self.assertEqual(self.source.comments[0]['body'], body)

    def test_extra_changes_and_invalid_schema_fail(self):
        self.dispatch()
        self.add_pr(extra_file=True)
        self.dispatch()
        self.assertIn('exactly one JSON file', self.source.comments[0]['body'])
        self.target.files.pop()
        self.target.pr['head']['sha'] = 'head2'
        self.target.file = lambda path, ref: json.dumps(SCHEMA) if path == 'schema_model_list.json' else json.dumps({**EXAMPLE, 'active_development': 'Yes'})
        self.dispatch()
        self.assertIn('is not of type', self.source.comments[0]['body'])

    def test_agent_interpretation_is_not_compared_with_fixed_mapping(self):
        self.dispatch()
        self.add_pr()
        self.target.generated['background_text'] = 'An AI-interpreted description for coordinator review.'
        self.dispatch()
        _, state = workflow.find_state(self.source, self.repository, 47)
        self.assertEqual(state['status'], 'validated')
        self.assertIn('does not verify source accuracy', self.source.comments[0]['body'])

    def test_stale_submission(self):
        self.dispatch()
        self.issue['body'] += '\n\n### Comments\n\nChanged'
        self.dispatch()
        self.assertEqual(len(self.target.tasks), 1)
        self.assertIn('submission changed', self.source.comments[0]['body'])


if __name__ == '__main__':
    unittest.main()