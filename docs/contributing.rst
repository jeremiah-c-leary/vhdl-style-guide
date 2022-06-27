Contributing
------------

Any contributions to this project are welcomed.
No matter how small or large.

There are several ways to contribute:

1. Bug reports
2. Code base improvements
3. Feature requests
4. Pull requests

Bug Reports
###########

Code from open cores was utilized to develop VSG.
It provided many different coding styles to process.
There are bound to be some corner cases or incorrect assumptions in the code due to the small sample size.
If problems are found with the output or in using VSG, please submit an issue.
When creating the issue, use the **bug** label to highlight it.
Fixing bugs is prioritized over feature enhancements.

Code Base Improvements
######################

VSG started out to solve a problem and learn how to code in Python.
The learning part is still on going, and the code base could always be improved.
The code base is run through *Codacy* and *Code Climate*, and they are very helpful.
However, any suggestions to improve the code base would be appreciated.

Create an issue and use the **refactor** label for any code which could be improved.

Feature Requests
################

VSG is still a work in progress and by no means feature complete.
In fact, the following features were not in the original concept of VSG.

* fix
* fix_phase
* output_format
* backup

Fix is probably the most important feature.
It was added when a user said it would be nice if VSG just fixed the problems it found.
There may be other important missing features in the current implementation.

Create an issue with the **enhancement** label for any new features.

Pull Requests
#############

Pull requests are always welcome.

VSG was developed using a Test Driven Development (TDD) process.
There are over 1000 tests which cover individual rules and other features of VSG.
For each pull request, an accompanying test to validate the pull request would be appreciated.

Refer to `Setting up a Development Environment <setting_up_a_development_environment.html#running-unit-tests>`_ for more information on how to get started.

Quality Control
###############

This project uses the following open source tools to help with code quality:

* *Travis CI* to run all the tests.
* *Codacy* and *Code Climate* to check for code style issues.
* *Codcov* to check the code coverage of the tests.

The results will be available on the pull request GitHub page.

