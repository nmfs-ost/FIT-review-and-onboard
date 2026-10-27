# Tool author submission guide

Thank you for considering your tool for inclusion in the Fisheries Integrated Toolbox (FIT)! This guide is designed to assist tool authors with the submission process.

To request review, [open an issue and fill out the Quality Review Request form](https://github.com/nmfs-ost/FIT-test-quality-checks/issues/new?template=quality-review-request.yml) in this repository. Include links to your source repository, documentation, and test evidence. Keep follow-up questions, revisions, and publication coordination in that issue; a second onboarding issue is not needed.

For the sequence, target timeframes, command reference, and a worked example, see the [review process](README.md#process-for-review). Report unclear instructions in the submission issue or [open a documentation issue](https://github.com/nmfs-ost/FIT-test-quality-checks/issues).


## Meeting the checklist requirements

Review of software for inclusion in the FIT is checklist-based. A NOAA internal reviewer will assess your tool for items on the reviewer checklist. The purpose of this process is to offer feedback, enabling you to modify your tool to align with the necessary standards for FIT inclusion.

The FIT committee recognizes that some checklist items may not be widespread practices within NOAA Fisheries, so this guide is provided as support for implementing new practices.

The form marks some fields as required to submit the issue and leaves others optional. An optional field can still provide evidence for a checklist item; blank fields are treated as information that was not provided, not as confirmation that the item is met. Follow the checklist requirements below as well as the field-specific instructions in the form.

Below are descriptions and guidance on how to meet criteria on the reviewer checklist.

### Basics

Everything in this section is required for inclusion in the FIT.

#### Confirm the tool is in scope

Review the [FIT scope statement](https://noaa-fisheries-integrated-toolbox.github.io/resources/about/) to confirm that the tool is in scope.

#### Metadata is complete

To meet this criteria, fill out all required fields of the onboarding form and follow the instructions. The FIT coordinator will let you know if something is missing or needs clarification.

The FIT coordinator will run the metadata against a [JSON schema](https://github.com/nmfs-ost/FIT_web_templating/blob/main/schema_model_list.json) to identify any missing information.

#### Links in metadata are active

The FIT coordinator will check that all links provided in the submitted onboarding form are functioning properly. We suggest developers double check that the links they provide are correct before submitting. Please note that all links listed in the onboarding form are NOT required, as long as there is at least one working metadata link.

#### A License is included

FIT licensing guidance provided here is not legal advice.

For comprehensive licensing guidance, refer to the [complete documentation](https://nmfs-opensci.github.io/GitHub-Guide/#sec-license). Generally, if only NOAA federal employees have contributed to a tool, a permissive open license, such as Apache 2.0, is required. The licensing process can be more complex when other contributors are involved. For assistance with software licensing decisions, contact the FIT service account at fisheries.toolbox@noaa.gov.

While software licenses can be changed, this typically requires agreement from all contributors. It is therefore recommended to establish a license before development begins to simplify the process.

#### Software version is included

A software version or a GitHub releases link should be included in the onboarding form. When using [GitHub releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases), leave the static version number blank and provide the source repository link.

Do you still need to decide how to [version](https://en.wikipedia.org/wiki/Software_versioning) the software? A common option is using [semantic versioning](https://semver.org/), although there are other standard schemes.

#### Source code is linked

Generally, source code should be made available for tools on the FIT, as typically developed NOAA federal employee code should have a permissive open source license. However, there may be special instances where code is not made available, such as if confidential fisheries information is included in the codebase.

Use the direct repository URL in the form's Source Code Link field, not a project website or documentation landing page.

#### NOAA Disclaimer on ReadMe

For tools with source code, add a [NOAA disclaimer](https://github.com/nmfs-ost/FIT-resource-files?tab=readme-ov-file#noaa-license) on the README.md of the source code:

```
## Disclaimer

“This repository is a scientific product and is not official communication of the National Oceanic and Atmospheric Administration, or the United States Department of Commerce. All NOAA GitHub project code
is provided on an ‘as is’ basis and the user assumes responsibility for its use. Any claims against the Department of Commerce or Department of Commerce bureaus stemming from the use of this GitHub project will be governed by all applicable Federal law. Any reference to specific commercial products, processes, or services by service mark, trademark, manufacturer, or otherwise, does not constitute or imply
their endorsement, recommendation or favoring by the Department of Commerce. The Department of Commerce seal and logo, or the seal and logo of a DOC bureau, shall not be used in any manner to imply endorsement of any commercial product or activity by DOC or the United States Government.”
```

#### Checks for accessibility (Applications only)

Per [Section 508 of the Rehabilitation Act](https://www.section508.gov/manage/laws-and-policies/section-508-law/), federal agencies must make their electronic products accessible to people with disabilities. Script-based tools typically are accessible (as text can be read by a screen reader), but additional checks and tests are needed to ensure accessibility for applications. Some tools to help with this are:

- Use [ANDI](https://www.ssa.gov/accessibility/andi/help/install.html) or [WAVE](https://wave.webaim.org/) for any applications using web-based technologies. These tools will identify inaccessible content and provide information on changes to make. For Shiny, check out [shinya11y](https://github.com/ewenme/shinya11y) for an alternative checker and accessible tooling options for Shiny.
- The [18F accessibility checklist](https://guides.18f.org/accessibility/checklist/) can also be helpful for manual checking of accessibility. 
- [Section508.gov](https://www.section508.gov/) provides extensive information on meeting requirements of Section 508 compliance.


### Documentation

Everything in this section is required for inclusion in the FIT.

#### Background Text

The background text should include a description of the tool and its motivation or scope, as well as the developers or organizations involved. It should also include a link to examples where the tool has informed science-based decision making, if this is appropriate.

#### Installation Instructions

Installation instructions should be provided. The tool reviewer must be able to follow them and successfully install the software.

If the software does not require user install, e.g., on a web app, no install instructions need to be provided.

#### A Getting Started Example

For first-time users, a "getting started" example is crucial for orienting them to the software. This concise example, demonstrating basic usage, should be embedded in or linked from the README.md of the source code repository, or otherwise easily discoverable. It should avoid advanced use cases.

#### Citation Instructions

To ensure users properly credit your work, provide citation instructions, preferably with a Digital Object Identifier (DOI), as requested in the form. A DOI offers a persistent link to your software or an accompanying paper.

There are three primary methods for obtaining a DOI for your software:

1. Academic Publication: This involves writing and publishing an academic paper. Users can then cite this publication. While it demands the most effort and time, academic publications are a recognized form of currency in scholarly environments.
2. Software Repository (e.g., [Zenodo](https://zenodo.org/)): Depositing your software in a repository like Zenodo will generate a citable DOI for your submission. This method requires the least effort and time, but it doesn't offer users an additional resource for learning about the tool.
3. Open Source Software Journal (e.g., [Journal of Open Source Software](https://joss.theoj.org/)): Journals such as the Journal of Open Source Software require a concise paper, allowing software authors to quickly prepare a submission. This option demands less effort than typical academic publications, though the publication timeline can still be lengthy depending on the review process.

Consider archiving releasable code and data in [Zenodo](https://zenodo.org/) for persistent access and citable DOIs. Include author [ORCIDs](https://orcid.org/) in the archive metadata, a license, and links between related software and data records. Archive the release used for review, not just a moving development branch. Do not upload confidential, restricted, or third-party materials without permission.

#### Tool Use Documentation

Tool use documentation, such as a user guide or function reference, should provide instructions on how to use the tool. Examples of such documentation include [roxygen](https://r-pkgs.org/man.html), [doxygen](https://www.doxygen.nl/), and [Sphinx](https://www.sphinx-doc.org/).


### Tests

To be onboarded to the FIT, a tool must meet the criteria described below.

#### Testing narrative

Use the test fields in the submission form to explain how a reviewer can evaluate your tests; add details in Comments if needed. Include the reviewed version or commit, operating system, language versions and dependencies, commands or manual steps, input data, expected outputs, approximate runtime, and any known limitations. Explain how to interpret success or failure.

For example: "For commit abc123 on Python 3.12/Linux, install the documented dependencies, run `python tests/check_example.py` against `data/example.csv`, and compare the generated totals with `tests/expected.csv` using the documented tolerance. This takes about two minutes. The linked logs show the results and the coverage command and report." Adapt the commands and expected results to your tool.

#### Integration and end-to-end tests

Integration tests check whether components work correctly together, such as a data reader passing its output to a model. End-to-end tests exercise a complete user workflow from input to final output. A getting started example can serve as an end-to-end test if it includes expected results for comparison. Provide steps and results for both; manual or automated testing is acceptable.

#### Language-specific check results

A unit testing framework provides a scaffolding for easily writing and running tests of your software. 

For R package developers, this is likely done using the [testthat](https://testthat.r-lib.org/) R package. A great resource to learn how to set up and use testthat is available in the [Testing Basics Chapter of the R packages book](https://r-pkgs.org/testing-basics.html).

For applications, consider GUI testing toolkits like shinytest2 for Shiny apps or Selenium for web applications.

#### Code coverage

Greater than **40% line coverage** is mandatory. Include the coverage report and measurement command for the reviewed version, and explain excluded code. 

For R package developers, the [covr](https://covr.r-lib.org/) package provides this functionality. For Python, [Coverage.py](https://coverage.readthedocs.io/en/7.10.2/) and [pytest-cov](https://pypi.org/project/pytest-cov/) are popular tools. For C++, [gcovr](https://gcovr.com/en/stable/) could be used.

#### Sample Data Availability

In the Sample Data Availability field, describe and link any available sample data that validates the tool's functionality. If none are available, state that. Where sample data are available, include instructions on how to run the tool with the data and a description of the results, and/or provide a results dataset or plot for comparison.

### Sound practices (not mandatory)

These checklist items could help improve the software's documentation and testing, however they are not required for onboarding to the Fisheries Integrated Toolbox.

#### Unit testing framework

A unit testing framework makes it easier to write and run isolated tests of functions or components with one command. For R, consider [testthat](https://testthat.r-lib.org/) and the [Testing Basics chapter of R Packages](https://r-pkgs.org/testing-basics.html). Python options include pytest and unittest; C++ options include googletest. For application testing, shinytest2 or Selenium may also help. Using a framework is optional, while the mandatory line-coverage threshold still applies.

#### Regression and correctness tests

Regression tests detect reintroduced bugs or unexpected changes to established behavior, often by retaining a test for each fixed bug or comparing with a trusted baseline. Correctness tests compare results with known answers, analytical solutions, or independent reference implementations. State appropriate numerical tolerances. These describe test purposes and can be implemented as unit, integration, or end-to-end tests; a saved output is not automatically proof of correctness.

#### Advanced Features Example

An advanced features example provides information on how to run the software for more advanced use cases. If possible, providing a real example can be helpful. The example should be embedded in or linked on the README.md of the source code repository. Otherwise, it should be hosted somewhere easy to find for users of the software.

#### Web-hosted Documentation

Web-hosted documentation allows users to more easily browse documentation. Common formats are a [pkgdown](https://pkgdown.r-lib.org/) site or a [doxygen](https://doxygen.nl/) site.

For source code that is hosted on GitHub, using GitHub pages to host the documentation may be an option that allows the user to quickly access web-hosted documentation. 

There are [instructions to host a NOAA-themed pkgdown site](https://nmfs-ost.github.io/noaa-fit-resources/noaa%20resources/NOAA-pkgdown/), which includes a [section on automating the pkgdown rendering](https://nmfs-ost.github.io/noaa-fit-resources/noaa%20resources/NOAA-pkgdown/#automate-your-pkgdown-rendering).

Other options include hosting [Quarto documentation](https://quarto.org/) on the [NMFS Posit Connect server](https://sites.google.com/noaa.gov/nmfs-hq-st-posit-connect/home).
 
#### Code Coverage is excellent

See the "Code coverage" section in the mandatory testing checklist items. To increase code coverage, untested parts of the codebase should be identified and new unit tests can be added that will run those parts of the codebase. For R packages, the [covr package](https://covr.r-lib.org/index.html) can help identify low and zero coverage locations in the codebase. These tests should be meaningful.

#### Automated Testing on a continuous integrated service

Continuous integration services, such as [GitHub Actions](https://github.com/features/actions) and [Jenkins](https://www.jenkins.io/), automate checks and tests. Running these checks and tests frequently, either on a schedule or when code changes are made, helps to quickly identify and resolve code issues. GitHub Actions is often the simplest to configure if your codebase is already hosted on GitHub.

For R packages, running [R cmd check](https://r-pkgs.org/R-CMD-check.html) can be a helpful way to ensure your R package is ready for users to download, so it is common to set up R cmd check as the primary automated testing check on a continuous integration service. 

There are 2 common ways within NOAA Fisheries to set up R cmd check.

The first approach is using [`usethis::use_github_action(name = "check-standard")`](https://usethis.r-lib.org/reference/use_github_action.html) to generate a GitHub action workflow file that runs R cmd check using the latest version of R on 3 operating systems (Linux, Windows, and Mac) and using the development version of R and the 1 older version of R on Linux only. This approach is best for users who may want to customize the workflow file or require custom dependencies or options because the user can edit the GitHub Actions file as they please. You will be responsible for maintaining the GitHub Action on your repository, as updates are NOT pushed automatically from `usethis::use_github_action("check-standard")`.

Alternatively, [ghactions4r::use_r_cmd_check()](https://nmfs-ost.github.io/ghactions4r/reference/use_r_cmd_check.html) can be used to generate a "caller" GitHub Action workflow file that calls a reusable workflow. This package is maintained by staff within NOAA Fisheries' Office of Science and Technology. This approach is best for users who want to use a standard workflow and do not want to maintain their own action. The benefit of this approach is that the bulk of the workflow is maintained within the ghactions4r package, and users can [open issues in the ghactions4r repository](https://github.com/nmfs-ost/ghactions4r/issues/) to report problems in running the workflow. Changes to the ghactions4r workflow are pushed automatically to the user by modifying the reusable workflow within ghactions4r.







