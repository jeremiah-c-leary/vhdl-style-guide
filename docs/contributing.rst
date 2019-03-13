Contributing
------------

I welcome any contributions to this project.
No matter how small or large.

There are several ways to contribute:

1. Bug reports
2. Code base improvements
3. Feature requests
4. Pull requests

Bug Reports
###########

I used code from open cores to develop VSG against.
There are bound to be some corner cases or incorrect assumptions in the code.
If you run into anything that is not handled correctly, please submit an issue.
When creating the issue, use the **bug** label to highlight it.
I prioritize bugs over feature enhancements.

Code Base Improvements
######################

VSG started out to solve a problem and learn how to code in Python.
The learning part is still on going, and I am sure the code base could be improved.
I run the code through *Codacy* and *Code Climate*, and they are very helpful.
However, I would appreciate any suggestions to improve the code base.

Create an issue and use the **refactor** label.

Feature Requests
################

Let me know if there is anything I could add to VSG easier to use.
The following features were not in my original concept of VSG.

* fix
* fix_phase
* output_format
* backup

Fix is probably the most important feature of VSG.
I added it when someone said it would be nice if VSG just fixed the problems it found.
There may be other important features, I just have not thought of them yet.

If you have an idea for a new feature, create an issue with the **enhancement** label.

Pull Requests
#############

Pull requests are always welcome.
I am trying to follow a Test Driven Development (TDD) process.
Currently there are over 1000 tests.
If you do add a new feature or fix a bug, I would appreciate a new or updated test to go along with the change.

I use *Travis CI* to run all the tests.
I also use *Codacy* and *Code Climate* to check for code style issues.
I use *Codcov* to check the code coverage of the tests.

*Travis CI* will run these tools when a pull request is made.
The results will be available on the pull request Github page.
