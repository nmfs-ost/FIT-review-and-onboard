import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('metadata', ROOT / 'scripts/metadata.py')
metadata = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(metadata)
SCHEMA = json.loads((ROOT / 'model_schema/schema_model_list.json').read_text())
EXAMPLE = json.loads((ROOT / 'model_schema/FishPath.json').read_text())


def submission():
    return 'FishPath onboarding request:\n\n' + json.dumps(EXAMPLE, indent=2)


class MetadataTests(unittest.TestCase):
    def test_example(self):
        self.assertEqual(metadata.validate(EXAMPLE, SCHEMA), [])

    def test_missing_required_properties(self):
        self.assertTrue(metadata.validate({}, SCHEMA))

    def test_limits_and_types(self):
        for changes in [
            {'keywords': []}, {'keywords': [str(index) for index in range(6)]},
            {'toolbox_drawers': []}, {'active_development': 'Yes'},
            {'FIT_reviewed': 'Maybe'},
            {'associated_tools': [{'name': 'Missing link'}]},
            {'software_badges': [{'link': 'https://example.org/badge'}]},
        ]:
            self.assertTrue(metadata.validate({**EXAMPLE, **changes}, SCHEMA), changes)

    def test_schema_controls_policy(self):
        self.assertEqual(metadata.validate({**EXAMPLE, 'extra': 'allowed by this schema'}, SCHEMA), [])
        self.assertEqual(metadata.validate({**EXAMPLE, 'tool_name': ''}, SCHEMA), [])
        evolved_schema = {
            '$schema': 'https://json-schema.org/draft/2020-12/schema',
            'type': 'object',
            'properties': {'new_field': {'type': 'string', 'minLength': 1}},
            'required': ['new_field'],
            'additionalProperties': False,
        }
        self.assertEqual(metadata.validate({'new_field': 'new metadata'}, evolved_schema), [])
        self.assertTrue(metadata.validate({'new_field': ''}, evolved_schema))
        self.assertTrue(metadata.validate({'new_field': 'value', 'extra': True}, evolved_schema))

    def test_duplicate_json_properties(self):
        with self.assertRaisesRegex(ValueError, 'Duplicate JSON property'):
            metadata.parse_json('{"tool_name": "First", "tool_name": "Second"}')


if __name__ == '__main__':
    unittest.main()