Setting up a Development Environment
------------------------------------

If you would like to review the code and make some changes, follow these steps to setup the development environment.

Clone the repo
##############

Clone the repo with the following command:

.. code-block:: text

    git clone https://github.com/jeremiah-c-leary/vhdl-style-guide.git

Setup alias
###########

Set an alias to VSG as follows:

.. code-block:: text

    set alias vsg='python3 <path_to_clone_directory>/bin/vsg'

This allows you to execute VSG without installing it.

Install prerequisites
#####################

.. code-block:: bash

  pip install PyYAML
  pip install tox

Build locally, artifacts will appear in ``dist`` directory.

.. code-block:: bash

  tox

Helpful tools
#############

vsg_parser
==========

vsg_parser is a tool which will show the mapping of tokens to a given file.
It is located in the bin directory and can be invoked with:

.. code-block:: bash

   $ bin/vsg_parser -f <filename>

This is the output when ran against the tests/architecture/rule_001_test_input.vhd file:

.. code-block:: mono

   --------------------------------------------------------------------------------
   0 |
   --------------------------------------------------------------------------------
   1 |
   <class 'vsg.parser.blank_line'>
   --------------------------------------------------------------------------------
   2 | architecture RTL of FIFO is begin end architecture RTL;
   <class 'vsg.token.architecture_body.architecture_keyword'>
   <class 'vsg.token.architecture_body.identifier'>
   <class 'vsg.token.architecture_body.of_keyword'>
   <class 'vsg.token.architecture_body.entity_name'>
   <class 'vsg.token.architecture_body.is_keyword'>
   <class 'vsg.token.architecture_body.begin_keyword'>
   <class 'vsg.token.architecture_body.end_keyword'>
   <class 'vsg.token.architecture_body.end_architecture_keyword'>
   <class 'vsg.token.architecture_body.architecture_simple_name'>
   <class 'vsg.token.architecture_body.semicolon'>
   --------------------------------------------------------------------------------
   3 |
   <class 'vsg.parser.blank_line'>
   --------------------------------------------------------------------------------
   4 | -- This should fail
   <class 'vsg.parser.comment'>
   --------------------------------------------------------------------------------
   5 |
   <class 'vsg.parser.blank_line'>
   --------------------------------------------------------------------------------
   6 |   architecture RTL of FIFO is
   <class 'vsg.token.architecture_body.architecture_keyword'>
   <class 'vsg.token.architecture_body.identifier'>
   <class 'vsg.token.architecture_body.of_keyword'>
   <class 'vsg.token.architecture_body.entity_name'>
   <class 'vsg.token.architecture_body.is_keyword'>
   --------------------------------------------------------------------------------
   7 |
   <class 'vsg.parser.blank_line'>
   --------------------------------------------------------------------------------
   8 | begin
   <class 'vsg.token.architecture_body.begin_keyword'>
   --------------------------------------------------------------------------------
   9 |
   <class 'vsg.parser.blank_line'>
   --------------------------------------------------------------------------------
   10 | end architecture RTL;
   <class 'vsg.token.architecture_body.end_keyword'>
   <class 'vsg.token.architecture_body.end_architecture_keyword'>
   <class 'vsg.token.architecture_body.architecture_simple_name'>
   <class 'vsg.token.architecture_body.semicolon'>

Each line is printed and then each token is listed in the order they appear on the line.
Whitespace tokens can be shown using the :code:`-w` option.

vsg_parser can be useful in rule generation to determine how vsg is assigning token types.

Adding a rule
#############

Following the steps in the given order ensures everything is covered.

#. Create documentation
   #.  Documentation structure
#. Create test
   #.  Test directory structure
   #.  Test File structure
   #.  input file
   #.  fixed file
#. Running failing test
#. Create rule
   #.  Update __init__.py
   #.  create the rule
#. Running passing test
#. Running regression tests

.. NOTE:: If a similar rule already exists, copy that rules elements for each of the following steps.

Create Documentation
====================

A documentation first approach clarifies what a rule will address.

The documentation is located in the `docs` directory.
All rules for a rule group are kept in a file with the following pattern:  <rule_group>_rules.rst.
The rules are in alphabetical order within the documentation.

Rule documentation contains the following items:

#. Rule ID
#. Icons
#. Summary
#. Link to configuration options
#. Violation example
#. Fixed example

.. code-block:: rst

   architecture_001
   ################

   |phase_4| |error| |indent|

   This rule checks for blank spaces before the **architecture** keyword.

   **Violation**

   .. code-block:: vhdl

        architecture rtl of fifo is
      begin

   **Fix**

   .. code-block:: vhdl

      architecture rtl of fifo is
      begin


The Rule ID identifies the rule and is unique through all versions of VSG.
A Rule ID will never be re-used.

Icons provide information about the rule at a quick glance.
These icons indicate the phase in which the rule is ran, whether it is disabled by default, etc...
Links to the icons are stored in a file named icons.rst and is included into each file using an include at the top of every file.

The summary is a very brief description of what issue the rule is attempting to resolve.

If the rule has configuration options, a link to the configuration information will be given.
The links are sored in a file named links.rst and in included into each file using an include at the top of every file.

The Violation Example provides a visual indicating what the issue is.

The Fixed example provides a visual indicating what the end state should be.

Create Test
===========

The next step is to create a test for the soon to be new rule.

Test directory structure
========================

The directory structure of the tests closely matches the rules directory.
Every rule group has it's own directory.

.. code-block:: mono

   tests
   ├── after
   ├── alias_declaration
   ├── architecture
        ...
   └── whitespace 

Each rule will typically consist of at least three files:

#.  test file of the form `test_rule_[0-9][0-9][0-9].py`
#.  input vhdl file with violations in the form of `rule_[0-9][0-9][0-9]_test_input.vhd`
#.  fixed vhdl file without violations in the form of `rule_[0-9][0-9][0-9]_test_input.fixed.vhd`

.. code-block:: mono

   tests
   └── architecture
       ├── rule_001_test_input.fixed.vhd
       ├── rule_001_test_input.vhd
       └── test_rule_001.py

Test file structure
===================

The test file contains a class with the name of `test_rule`.
The minimum number of tests will be one for those rules for which a fix is not available.
The rules in which a fix is available, a minimum of two tests will be required:  one for detecting violations and another for verifying the violations can be fixed.
If the rule has configurable options, then additional tests are required based on the number of configurable items.

.. code-block:: python

   class test_rule(unittest.TestCase):

       def test_rule_001(self):
           oRule = architecture.rule_001()

       def test_fix_rule_001(self):
           oRule = architecture.rule_001()

The test_rule_001 method operates on the test input file and returns a list of lines where a violation was detected.
The line numbers are then validated.

The test_fix_rule_001 method operations on the test input file and attempts to fix the violations.
The resulting fix is compared against the rule_001_test_input.fixed.vhd file.
Any discrepencies are flagged.

Test Input File
===============

The test input file provides examples of code passing and violating the particular rule.
It provides the conditions where the rule is checked.
Depending on the rule, this file can range from very simple to quite complex.
If configuration options are available for the rule, then this file should provide conditions for each configurable item.

.. code-block:: vhdl

   architecture RTL of FIFO is begin end architecture RTL;
   
   -- This should fail
   
     architecture RTL of FIFO is
   
   begin
   
   end architecture RTL;

Fixed Input File
================

This file provides the output product of running the rule in isolation.
Additional rules are not applied.
If configuration options are available for the rule, then additional files are required for each configuraiton.

.. code-block:: vhdl

   architecture RTL of FIFO is begin end architecture RTL;
   
   -- This should fail
   
   architecture RTL of FIFO is
   
   begin
   
   end architecture RTL;

Running failing test
====================

VSG uses pytest

.. code-block:: mono

   $ pytest tests/architecture/test_rule_001.py
   ======================================== test session starts =========================================
   platform linux -- Python 3.10.13, pytest-8.1.1, pluggy-1.4.0
   rootdir: /home/jcleary/projects/vsg-master
   configfile: pyproject.toml
   plugins: html-4.1.1, html-reporter-0.2.9, metadata-3.1.1
   collected 2 items
   
   tests/architecture/test_rule_001.py FF                                                         [100%]
   
   ============================================== FAILURES ==============================================
   ______________________________ test_architecture_rule.test_fix_rule_001 ______________________________
   
   self = <tests.architecture.test_rule_001.test_architecture_rule testMethod=test_fix_rule_001>
   
       def test_fix_rule_001(self):
   >       oRule = architecture.rule_001()
   E       AttributeError: module 'vsg.rules.architecture' has no attribute 'rule_001'. Did you mean: 'rule_002'?
   
   tests/architecture/test_rule_001.py:39: AttributeError
   ________________________________ test_architecture_rule.test_rule_001 ________________________________
   
   self = <tests.architecture.test_rule_001.test_architecture_rule testMethod=test_rule_001>
   
       def test_rule_001(self):
   >       oRule = architecture.rule_001()
   E       AttributeError: module 'vsg.rules.architecture' has no attribute 'rule_001'. Did you mean: 'rule_002'?
   
   tests/architecture/test_rule_001.py:28: AttributeError
   ====================================== short test summary info =======================================
   FAILED tests/architecture/test_rule_001.py::test_architecture_rule::test_fix_rule_001 - AttributeError: module 'vsg.rules.architecture' has no attribute 'rule_001'. Did you mean: 'rule_...
   FAILED tests/architecture/test_rule_001.py::test_architecture_rule::test_rule_001 - AttributeError: module 'vsg.rules.architecture' has no attribute 'rule_001'. Did you mean: 'rule_...
   ========================================= 2 failed in 0.43s ==========================================

The test failed because the rule does not yet exist

Create Rule
===========

Updating __init__.py file
^^^^^^^^^^^^^^^^^^^^^^^^^

In order for a rule to be used, it must be added to the __init__.py file in the rule group directory.

.. code-block:: python

   # -*- coding: utf-8 -*-
   from .rule_001 import rule_001
   from .rule_002 import rule_002

Rule file structure
^^^^^^^^^^^^^^^^^^^

#. class name
#. docstring
#. rule implementation

The class name of the rule must follow this pattern:  `rule_[0-9][0-9][0-9]`.

The docstring must match the documentation but does not include the header or the icons.

The rule implementation could be unique or it could call a base rule.

.. code-block:: python

   # -*- coding: utf-8 -*-
  
   from vsg.rules import token_indent
   from vsg.token import architecture_body as token
  
  
   class rule_001(token_indent):
       """
       This rule checks for blank spaces before the **architecture** keyword.
  
       **Violation**
  
       .. code-block:: vhdl
  
            architecture rtl of fifo is
          begin
  
       **Fix**
  
       .. code-block:: vhdl
  
          architecture rtl of fifo is
          begin
       """
  
       def __init__(self):
           super().__init__([token.architecture_keyword])

In this case the `token_indent` base rule is used to check the indent of the architecture keyword.

Running passing test
^^^^^^^^^^^^^^^^^^^^

Re-run the test and make any changes until the test passes.

.. code-block:: mono

   ======================================== test session starts =========================================
   platform linux -- Python 3.10.13, pytest-8.1.1, pluggy-1.4.0
   rootdir: /home/jcleary/projects/vsg-master
   configfile: pyproject.toml
   plugins: html-4.1.1, html-reporter-0.2.9, metadata-3.1.1
   collected 2 items
   
   tests/architecture/test_rule_001.py ..                                                         [100%]
   
   ========================================= 2 passed in 0.34s ==========================================

Running regression tests
^^^^^^^^^^^^^^^^^^^^^^^^

Now that the single test runs, the entire suite of tests must be ran to ensure there no side effects.

.. code-block:: mono

   $ tox -e test-py38
   ======================================== test session starts =========================================
   platform linux -- Python 3.8.10, pytest-8.1.1, pluggy-1.4.0
   cachedir: .tox/test-py38/.pytest_cache
   rootdir: /home/jcleary/projects/vsg-master
   configfile: pyproject.toml
   plugins: cov-5.0.0, html-4.1.1, xdist-3.5.0, html-reporter-0.2.9, metadata-3.1.1
   8 workers [3005 items]
   .............................................................................................. [  3%]
   .............................................................................................. [  6%]

   .............................................................................................. [ 97%]
   .......................................................................................        [100%]
   
   ---------- coverage: platform linux, python 3.8.10-final-0 -----------
   Coverage HTML written to dir build.out/test-py38/coverage
   Coverage XML written to file build.out/test-py38/coverage.xml
   
   - Generated html report: file:///home/jcleary/projects/vsg-master/build.out/test-py38/test/pytest.html -
   ================================== 3005 passed in 72.67s (0:01:12) ===================================
     test-py38: OK (81.82=setup[8.52]+cmd[73.30] seconds)
     congratulations :) (81.87 seconds)

Prepare for pull request
========================

Before creating a pull request use tox to perform all checks against the code base:

.. code-block:: bash

   $ tox

This will run code style checks, unittests against multiple versions of python and attempt to perform a build.
When this passes create a pull request.

.. NOTE:: Issue 1157 https://github.com/jeremiah-c-leary/vhdl-style-guide/issues/1157 is still being resolved and should not gate any PR creation.
