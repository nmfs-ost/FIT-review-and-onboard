# Reviewer Guide

A guide to help reviewers in filling out the tool quality standards.

## Review workflow

Use the submission issue as the review record. The coordinator checks metadata and documentation completeness before assigning a reviewer.

1. Confirm that you have no conflict of interest
2. Post `/generate-reviewer-checklist` in a new issue comment. Ask the coordinator for help if you cannot run it.
3. Complete the checklist, record results and questions in the issue. Ask for explanations or corrected evidenc. Link detailed source-repository issues back to the review. Only check mandatory items once they are verified; optional sound practices need not all be met.
6. Tell the coordinator when the review is complete. The coordinator will handle the post-acceptance steps.

Aim to finish within **four weeks of assignment**. This is a target, not a hard deadline; please discuss blockers or extensions in the issue. 

See the [command quick reference and example review](README.md#command-quick-reference) and the [test definitions and evidence requirements](tool-author-submission-guide.md#tests).

## Optional external review aids

- **rOpenSci pkgcheck:** [pkgcheck](https://docs.ropensci.org/pkgcheck/) combines R-package checks, including R CMD check results, statistics, and rOpenSci-specific structure checks. It can supplement author-provided evidence, but its readiness result is not a FIT acceptance decision. Its extra system dependencies and GitHub API setup make it an optional aid rather than a required FIT step; review its setup and credential needs before use.
- **pyOpenSci:** the [software peer-review guide](https://www.pyopensci.org/software-peer-review/) and [Python packaging guide](https://www.pyopensci.org/python-package-guide/) provide Python-focused guidance for authors and reviewers. Use them to interpret packaging, documentation, and testing evidence, not as a second mandatory checklist or an executable pass/fail checker.
- **Process models:** [rOpenSci's review guide](https://devguide.ropensci.org/softwarereviewintro.html) and [JOSS reviewer guidelines](https://joss.readthedocs.io/en/latest/reviewer_guidelines.html) offer useful models for staged, collaborative review. FIT retains its own criteria and time targets.

For now, FIT requires author-provided language-specific results and human review.

## Checklist item extended descriptions.

See the [Tool Author Submission Guide](https://github.com/nmfs-ost/FIT-test-quality-checks/blob/main/tool-author-submission-guide.md).

## Reviewer conflict of interest

The FIT reviewer has a conflict of interest if any of the following apply:

* They are a co-developer of the tool  
* They supervise or are supervised by a co-author of the tool  
* They feel that they cannot review the tool in an unbiased way

If there is a conflict of interest, they should recuse themselves from tool review and a replacement reviewer will be found.

Note that federal employees are subject to [federal ethics rules](https://2010-2014.commerce.gov/sites/default/files/documents/2015/january/noaa-summary_of_ethics_rules-2015_0.pdf), which include [personal relationships](https://2010-2014.commerce.gov/sites/default/files/documents/2015/january/appearance_of_bias-awae-2015-e_0.pdf). Non-government peer reviewers of influential scientific information are subject to a [NOAA Conflict of Interest Policy](https://www.noaa.gov/organization/information-technology/policy-oversight/information-quality/noaa-conflict-of-interest-policy-for-non-government-peer-reviewers-of-influential-scientific).