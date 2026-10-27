# test-quality-checks
Test out the tool quality checks.

See the .github/workflows folder to preview the checklists.

## Instructions for developer

Thank you for submitting your software to the Fisheries Integrated Toolbox! Read the [tool author submission guide](tool-author-submission-guide.md), confirm that your software is [in scope for FIT](https://nmfs-ost.github.io/noaa-fit-resources/about/#scope-statement), then [open an issue and fill out the Quality Review Request form](https://github.com/nmfs-ost/FIT-test-quality-checks/issues/new?template=quality-review-request.yml). Include a short testing narrative, language-specific check results, and a line-coverage report.

After submitting, some basic checks will occur before the software is assigned a peer reviewer who will review the materials you provide to begin checking off components of the checklist. This is a checklist-based review, where all mandatory items must be checked off before the software can be onboarded to the FIT.

## Process for review

1. Author submits tool using the "quality review checklist" issue under https://github.com/nmfs-ost/FIT-test-quality-checks/issues
2. FIT coordinator generates the basics checklist using `/generate-basics-checklist` in an issue comment and completes it.
3. Once basics is completed, FIT coordinator identifies a reviewer.
4. Once a reviewer is identified, the FIT coordinators uses `/generate-reviewer-instructions @reviewer-github-name` to generate instructions for the reviewer.
5. The reviewer generates their checklist using `/generate-reviewer-checklist` and completes it. They can ask questions to the author as needed.
6. Once the tool is accepted, the FIT coordinator generates the post-acceptance checklist using `/generate-post-acceptance-checklist` and completes it.
7. Once the post-acceptance checklist is complete and the author is satisfied with how the page looks on the FIT, the software is included on the FIT production website.
8. The FIT coordinator comments `/generate-acceptance-message` on the submission issue to generate an acceptance message tagging the author and providing the FIT quality checks badge code.

> Note: Use `/list-commands` to see command options available for use.

### Timing and coordination

The FIT coordinator aims to complete basic checks within **one week of submission**. Reviewers aim to complete peer review within **four weeks of assignment**. These are targets, not deadlines: record blockers and agree on extensions in the submission issue. Reviewer recruitment and author revisions depend on availability; the coordinator should post progress updates when delayed.

Reviewers- See the [reviewer guide](reviewer-guide.md).

The staged, issue-based approach draws on [rOpenSci](https://devguide.ropensci.org/softwarereviewintro.html), [JOSS](https://joss.readthedocs.io/en/latest/reviewer_guidelines.html), and [pyOpenSci](https://www.pyopensci.org/software-peer-review/).

Keep the submission and review discussion in the issue. Link existing source code, documentation, test logs, and archives rather than copying them into another onboarding repository. The FIT coordinator handles the FIT website publication steps; authors should not open a second onboarding request. Link any detailed implementation issues back to the submission.

### Command quick reference

Post commands at the start of a new comment on the submission issue. Coordinator commands require `OWNER` or `MEMBER` association; the reviewer checklist also allows `COLLABORATOR`.

| Command | Who | Result |
| --- | --- | --- |
| `/generate-basics-checklist` | Coordinator | Replaces the command comment with basic checks and documentation completeness checks. |
| `/generate-reviewer-instructions @reviewer-github-name` | Coordinator | Posts a new comment with reviewer instructions. |
| `/generate-reviewer-checklist` | Reviewer | Replaces the command comment with installation, example, and testing checks. |
| `/generate-post-acceptance-checklist` | Coordinator | Replaces the command comment with publication tasks. |
| `/generate-acceptance-message` | Coordinator | Replaces the command comment with the acceptance message |
| `/list-commands` | Coordinator | Posts a new comment listing commands. |

### Example review

See the [fishprior review](https://github.com/nmfs-ost/FIT-test-quality-checks/issues/48).

### Submission and status automation

New issues with the `Review Request` label receive one welcome comment linking to the peer review sequence and command reference in this README. Applying that label to an existing issue also initializes it; reruns do not duplicate the welcome or reset an existing review stage. Pull requests and unrelated issues are excluded.

| Stage label | Trigger |
| --- | --- |
| `review: submitted` | Submission opened or labeled `Review Request`. |
| `review: basic checks` | Coordinator posts `/generate-basics-checklist`. |
| `review: peer review` | Coordinator posts `/generate-reviewer-instructions @reviewer-github-name`. |
| `review: post-acceptance` | Coordinator posts `/generate-post-acceptance-checklist`. |
| `review: accepted` | Coordinator posts `/generate-acceptance-message`. |

Only owner/member commands advance stages. The tracking workflow creates stage labels as needed and replaces the previous review-stage label without removing unrelated labels. It tracks the **requested stage**, not successful execution of another workflow or verification of checklist completion. Coordinators must verify the mandatory checks and publication before issuing the corresponding commands; reissuing an earlier command can move the stage back for another review round.

These workflows need `issues: write` and must be on the default branch to receive issue events. They do not execute submitted code, fork repositories, or perform AI metadata validation. Language-specific checks remain author-run.

### Reviewing existing tools (section under construction)

These software already have metadata in the FIT. What needs to happen is:
1. Author reviews metadata and changes it as needed.
2. Author adds additional info needed for the peer review process, should not need to re-enter existing metadata.
3. Complete 2-8 for the software tool.

## Workflow development checks

With Python, PyYAML (`python -m pip install PyYAML`), and Node.js installed, run `python -B -m unittest discover -s tests -v`. The tests parse the issue form and workflows and execute their JavaScript with mocked GitHub APIs; they do not modify GitHub issues. Live event delivery and repository permissions must still be verified after deployment.


## disclaimer

“The United States Department of Commerce (DOC) GitHub project code is provided on an ‘as is’ basis and the user assumes responsibility for its use. DOC has relinquished control of the information and no longer has responsibility to protect the integrity, confidentiality, or availability of the information. Any claims against the Department of Commerce stemming from the use of its GitHub project will be governed by all applicable Federal law. Any reference to specific commercial products, processes, or services by service mark, trademark, manufacturer, or otherwise, does not constitute or imply their endorsement, recommendation or favoring by the Department of Commerce. The Department of Commerce seal and logo, or the seal and logo of a DOC bureau, shall not be used in any manner to imply endorsement of any commercial product or activity by DOC or the United States Government.”
