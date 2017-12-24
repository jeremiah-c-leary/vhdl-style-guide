VHDL Style Guide (VSG)
======================

**Coding style enforcement for VHDL.**

<div align="center">
  <!-- github release -->
  <a href="https://github.com/jeremiah-c-leary/vhdl-style-guide">
    <img src="https://img.shields.io/github/tag/jeremiah-c-leary/vhdl-style-guide.svg?style=flat-square"
      alt="Github Release" />
  </a>
  <!-- PyPI version -->
  <a href="https://pypi.python.org/pypi/vsg">
    <img src="https://img.shields.io/pypi/v/vsg.svg?style=flat-square"
      alt="PyPI Version" />
  </a>
  <!-- Build Status -->
  <a href="https://travis-ci.org/jeremiah-c-leary/vhdl-style-guide">
    <img src="https://img.shields.io/travis/jeremiah-c-leary/vhdl-style-guide/master.svg?style=flat-square"
      alt="Build Status" />
  </a>
  <!-- Test Coverage -->
  <a href="https://codecov.io/github/jeremiah-c-leary/vhdl-style-guide">
    <img src="https://img.shields.io/codecov/c/github/jeremiah-c-leary/vhdl-style-guide/master.svg?style=flat-square"
      alt="Test Coverage" />
  </a>
  <!-- Read The Docs -->
  <a href="http://vhdl-style-guide.readthedocs.io/en/latest/index.html">
    <img src="https://img.shields.io/readthedocs/vsg.svg?style=flat-square"
      alt="Read The Docs" />
  </a>
  <!-- Codacy -->
  <a class="badge-align" href="https://www.codacy.com/app/jeremiah-c-leary/vhdl-style-guide?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=jeremiah-c-leary/vhdl-style-guide&amp;utm_campaign=Badge_Grade">
    <img src="https://api.codacy.com/project/badge/Grade/42744dca97544824b93cfc99e8030063"
      alt="Codacy" />
  </a>
</div>

After recently performing code reviews, most of the issues found were related to style.
Time spent in code reviews addressing style issues is a waste.
Depending on your process, style issues can take a lot of time to resolve.

1. Create finding/ticket/issue
2. Disposition
3. Fix
4. Verify fix

Spending less time on style issues, leaves more time to analyze the substance of the code.
Ultimately, this will reduce the amount of time performing code reviews.
Spending more time on substance than style will result in higher quality code that costs less.

## Key benefits

* Define VHDL coding standards
* Makes coding standards visible to everyone
* Improve code reviews
* Quickly bring code up to current standards

VSG allows the style of the code to be defined and enforced over part or the entire code base.
Configurations allow for multiple coding standards.

## Key Features

* Command line tool
  - integrate into continuous integration flow
* Fixes and/or reports issues found
  - whitespace
    - horizontal
    - vertical
  - upper and lower case
  - keyword alignments
  - etc...
* Fully configurable rules via JSON configuration file
  - Disable rules
  - Alter behavior of existing rules
  - Change phase of execution
* Localize rule sets
  - Create your own rules using python
  - Use existing rules as a template
  - Fully integrates into base rule set

## Installation

You can get the latest released version of VSG via **pip**.

```
pip install vsg
```

The latest development version can be cloned...

```
git clone https://github.com/jeremiah-c-leary/vhdl-style-guide.git
```
...and then installed locally...
```
python setup.py install
```

## Usage

VSG is a command line tool and is invoked with...
```
$vsg

usage: VHDL Style Guide (VSG) [-h] -f FILENAME [--local_rules LOCAL_RULES]
                              [--configuration CONFIGURATION] [--fix]

Analyzes VHDL files for style guide violations.

optional arguments:
  -h, --help            show this help message and exit
  -f FILENAME, --filename FILENAME
                        File to analyze
  --local_rules LOCAL_RULES
                        Path to local rules
  --configuration CONFIGURATION
                        JSON configuration file
  --fix                 Fix issues found
```

Here is an example output running against a test file:
```
$ vsg -f PIC.vhd 
File:  PIC.vhd
==============
Phase 1... Reporting
Phase 2... Reporting
Phase 3... Reporting
Phase 4... Reporting
Phase 5... Reporting
  comment_002               |         51 | Ensure proper alignment of comment with previous line.
  comment_002               |         52 | Ensure proper alignment of comment with previous line.
  comment_002               |         54 | Ensure proper alignment of comment with previous line.
  comment_002               |         55 | Ensure proper alignment of comment with previous line.
  comment_003               |     76-256 | Inconsistent alignment of comments within process.
  sequential_005            |      87-93 | Inconsistent alignment of "<=" in group of lines.
  sequential_005            |    102-103 | Inconsistent alignment of "<=" in group of lines.
  sequential_005            |    105-108 | Inconsistent alignment of "<=" in group of lines.
  sequential_005            |    110-113 | Inconsistent alignment of "<=" in group of lines.
  sequential_005            |    115-118 | Inconsistent alignment of "<=" in group of lines.
  sequential_005            |    120-124 | Inconsistent alignment of "<=" in group of lines.
  sequential_005            |    129-133 | Inconsistent alignment of "<=" in group of lines.
  sequential_005            |    160-161 | Inconsistent alignment of "<=" in group of lines.
  sequential_005            |    173-174 | Inconsistent alignment of "<=" in group of lines.
  comment_002               |        183 | Ensure proper alignment of comment with previous line.
  sequential_005            |    225-226 | Inconsistent alignment of "<=" in group of lines.
  sequential_005            |    238-239 | Inconsistent alignment of "<=" in group of lines.
Phase 6... Not executed
Phase 7... Not executed
==============
Total Rules Checked: 204
Total Failures:      523
```

## Documentation

All documentation for VSG is hosted at [read-the-docs](http://vhdl-style-guide.readthedocs.io/en/latest/index.html)

## Running Tests

You can run all the tests at the top level by invoking the following command...

```
$ python setup.py test
running test
Searching for nose
.
.
.

----------------------------------------------------------------------
Ran 578 tests in 0.364s

OK
```
...or...
```
$ python -m unittest discover
..................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................
----------------------------------------------------------------------
Ran 578 tests in 0.072s

OK
```


## Local rules

VSG supports customization by allowing localized rules.
This is simply a directory with an __init__.py file and one or more python files.
The files should follow the same structure and naming convention as the rules found in the vsg/rules directory.

The localized rules will be used when the -l command line argument is given.

