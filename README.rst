VHDL Style Guide (VSG)
======================

**Coding style enforcement for VHDL.**

.. image:: https://img.shields.io/github/tag/jeremiah-c-leary/vhdl-style-guide.svg?style=flat-square
   :target: https://github.com/jeremiah-c-leary/vhdl-style-guide
   :alt: Github Release
.. image:: https://img.shields.io/pypi/v/vsg.svg?style=flat-square
   :target: https://pypi.python.org/pypi/vsg
   :alt: PyPI Version
.. image:: https://img.shields.io/travis/jeremiah-c-leary/vhdl-style-guide/master.svg?style=flat-square
   :target: https://travis-ci.org/jeremiah-c-leary/vhdl-style-guide
   :alt: Build Status
.. image:: https://img.shields.io/codecov/c/github/jeremiah-c-leary/vhdl-style-guide/master.svg?style=flat-square
   :target: https://codecov.io/github/jeremiah-c-leary/vhdl-style-guide
   :alt: Test Coverage
.. image:: https://img.shields.io/readthedocs/vsg.svg?style=flat-square
   :target: http://vhdl-style-guide.readthedocs.io/en/latest/index.html
   :alt: Read The Docs
.. image:: https://api.codacy.com/project/badge/Grade/42744dca97544824b93cfc99e8030063
   :target: https://www.codacy.com/app/jeremiah-c-leary/vhdl-style-guide?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=jeremiah-c-leary/vhdl-style-guide&amp;utm_campaign=Badge_Grade
   :alt: Codacy

Announcements
-------------

Update 11/05/2023

Release 3.18.0

There were several alignment rules which were ignoring the `comment_line_ends_group` option.
Please be aware that some alignment rules may trigger from the previous release.
Refer to issue #988 for more details.

There was also an issue with YAML configurations with options using `yes` and `no`.
These options could be converted to booleans by PyYAML according to the YAML spec if they were not strings.
Due to this an effort was made to change all the `True` and `False` options to `yes` and `no` strings.
The original `True` and `False` are still supported, but going forward all options will be strings.
Refer to issue #1009 for more details.

Platform independent features were added in this release.
This includes line separators and file path separators.
The type of line separator can be based on the platform or hard coded.

Regards,

--Jeremy

.. image:: https://github.com/jeremiah-c-leary/vhdl-style-guide/blob/master/docs/img/vim_macro.gif

Table of Contents
-----------------

*   `Overview`_
*   `Key Benefits`_
*   `Key Features`_
*   `Known Limitations`_
*   `Installation`_
*   `Usage`_
*   `Documentation`_
*   `Contributing`_

Overview
--------

VSG was created after participating in a code review where a real issue in the code was masked by a coding style issue.
A finding was created for the style issue, while the real issue was missed.
When the code was re-reviewed, the real issue was discovered.

Depending on your process, style issues can take a lot of time to resolve.

#. Create finding/ticket/issue
#. Disposition finding/ticket/issue
#. Fix
#. Verify fix

Spending less time on style issues leaves more time to analyze the substance of the code.
This ultimately reduces the amount of time performing code reviews.
It also allows reviewers to focus on the substance of the code.
This will result in a higher quality code base.

Key Benefits
------------

* Define VHDL coding standards
* Makes coding standards visible to everyone
* Improve code reviews
* Quickly bring code up to current standards

VSG allows the style of the code to be defined and enforced over part or the entire code base.
Configurations allow for multiple coding standards.

Key Features
------------

* Command line tool

  * integrate into continuous integration flow with JUnit output

* Reports and fixes issues found

  * whitespace

    * horizontal
    * vertical

  * upper and lower case
  * keyword alignments
  * etc...

* Fully configurable rules via JSON or YAML configuration file

  * Disable rules
  * Alter behavior of existing rules

* Localize rule sets

  * Create your own rules using python
  * Use existing rules as a template
  * Fully integrates into base rule set

* Built in styles

  * Use existing style or create your own

Known Limitations
-----------------

VSG is a continual work in progress.
As such, this version has the following known limitations:

* Parser will not process embedded PSL
* Parser will not process VHDL 2019

Installation
------------

You can get the latest released version of VSG via **pip**.

.. code-block:: bash

    pip install vsg

The latest development version can be cloned...

.. code-block:: bash

    git clone https://github.com/jeremiah-c-leary/vhdl-style-guide.git

...and then installed locally...

.. code-block:: bash

    python setup.py install

Usage
-----

VSG is a both a command line tool and a python package.
The command line tool can be invoked with:

.. code-block:: bash

   $ vsg
   usage: VHDL Style Guide (VSG) [-h] [-f FILENAME [FILENAME ...]] [-lr LOCAL_RULES] [-c CONFIGURATION [CONFIGURATION ...]] [--fix]
                                 [-fp FIX_PHASE] [-j JUNIT] [-js JSON] [-of {vsg,syntastic,summary}] [-b] [-oc OUTPUT_CONFIGURATION]
                                 [-rc RULE_CONFIGURATION] [--style {indent_only,jcl}] [-v] [-ap] [--fix_only FIX_ONLY] [--stdin]
                                 [--quality_report QUALITY_REPORT] [-p JOBS] [--debug]
                                 [FILENAME ...]

   Analyzes VHDL files for style guide violations. Reference documentation is located at: http://vhdl-style-guide.readthedocs.io/en/latest/index.html

   positional arguments:
     FILENAME              File to analyze

   options:
     -h, --help            show this help message and exit
     -f FILENAME [FILENAME ...], --filename FILENAME [FILENAME ...]
                           File to analyze
     -lr LOCAL_RULES, --local_rules LOCAL_RULES
                           Path to local rules
     -c CONFIGURATION [CONFIGURATION ...], --configuration CONFIGURATION [CONFIGURATION ...]
                           JSON or YAML configuration file(s)
     --fix                 Fix issues found
     -fp FIX_PHASE, --fix_phase FIX_PHASE
                           Fix issues up to and including this phase
     -j JUNIT, --junit JUNIT
                           Extract Junit file
     -js JSON, --json JSON
                           Extract JSON file
     -of {vsg,syntastic,summary}, --output_format {vsg,syntastic,summary}
                           Sets the output format.
     -b, --backup          Creates a copy of input file for comparison with fixed version.
     -oc OUTPUT_CONFIGURATION, --output_configuration OUTPUT_CONFIGURATION
                           Write configuration to file name.
     -rc RULE_CONFIGURATION, --rule_configuration RULE_CONFIGURATION
                           Display configuration of a rule
     --style {indent_only,jcl}
                           Use predefined style
     -v, --version         Displays version information
     -ap, --all_phases     Do not stop when a violation is detected.
     --fix_only FIX_ONLY   Restrict fixing via JSON file.
     --stdin               Read VHDL input from stdin, disables all other file selections, disables multiprocessing
     --quality_report QUALITY_REPORT
                           Create code quality report for GitLab
     -p JOBS, --jobs JOBS  number of parallel jobs to use, default is the number of cpu cores
     --debug               Displays verbose debug information

Here is an example output running against a test file:

.. image:: https://github.com/jeremiah-c-leary/vhdl-style-guide/blob/master/docs/img/fixing_single_file.gif

pre-commit Integration
----------------------

Here is an example of ``.pre-commit-config.yaml`` file:

.. code-block:: yaml

  repos:
    - repo: https://github.com/jeremiah-c-leary/vhdl-style-guide
      rev: v3.18.0
      hooks:
        - id: vsg

Documentation
-------------

All documentation for VSG is hosted at `read-the-docs <http://vhdl-style-guide.readthedocs.io/en/latest/index.html>`_.

Contributing
------------

I welcome any contributions to this project.
No matter how small or large.

There are several ways to contribute:

* Bug reports
* Code base improvements
* Feature requests
* Pull requests

Please refer to the documentation hosted at `read-the-docs <http://vhdl-style-guide.readthedocs.io/en/latest/index.html>`_ for more details on contributing.
