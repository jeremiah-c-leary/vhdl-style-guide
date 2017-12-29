Localizing
==========

VSG supports customization to your style standards by allowing localized rules.
This is a directory with an __init__.py file and one or more python files.
The files should follow the same structure and naming convention as the rules found in the vsg/rules directory.

The localized rules will be used when the **--local_rules** command line argument is given.

Example: Create rule to check for entity and architectures in the same file.
----------------------------------------------------------------------------

Let's suppose in our orginization the entity and architecture should be split into seperate files.
This rule is not in the base rule set, but we can add it through localization.
For this example, we will be setting up the localized rules in your home directory.

Prepare local rules directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create an empty directory with an empty __init__.py file

.. code-block:: bash

  $ mkdir ~/local_rules
  $ touch ~/local_rules/__init__.py

Create new rule file
~~~~~~~~~~~~~~~~~~~~

We will create a new rule by extending the base rule class.

.. NOTE::
  The file name and class name must start with **rule_**.
  Otherwise VSG will not recognize it as a rule.

The rule will be in the **localized** group.
Since this is the first rule, we will number it **001**.

.. code-block:: python

   from vsg import rule


   class rule_001(rule.rule):

     def __init__(self):
         rule.rule.__init__(self, 'localized', '001')
         
Referencing the :doc:`phases`, we decide it should be in phase 1: structural.

.. code-block:: python

   from vsg import rule


   class rule_001(rule.rule):

     def __init__(self):
         rule.rule.__init__(self, 'localized', '001')
         self.phase = 1

Now we need to add the **analyze** method to perform the check.

.. code-block:: python

   from vsg import rule


   class rule_001(rule.rule):

     def __init__(self):
         rule.rule.__init__(self, 'localized', '001')
         self.phase = 1

     def analyze(self, oFile):

The built in variables in the vsg.line class can be used to build rules.
There are helper functions in vsg.utilities, :doc:`vsg.check`, and vsg.fix also.
In this case, the vsg.vhdlFile class has two attributes(hasEntity and hasArchitecture) that are exactly what we need.
We are ready to write the body of the **analyze** method:

.. code-block:: python

   from vsg import rule


   class rule_001(rule.rule):

     def __init__(self):
         rule.rule.__init__(self, 'localized', '001')
         self.phase = 1

     def analyze(self, oFile):
         if oFile.hasEntity and oFile.hasArchitecture:
             self.add_violation(1)

The base rule class has an **add_violation** method which takes a line number an as argument.
This method appends the line number to a violation list, which is processed later for reporting and fixing purposes.
In this case, any line number will do so we picked 1.

We must decide if we want to give VSG the ability to fix this rule on it's own.
If so, then we will need to write the **_fix_violations** method.
However, for this violation we want the user to split the file.
There are too many variables to consider; including headers, footers, and copyright statements.
So we will tell VSG the rule is not fixable.

.. code-block:: python

   from vsg import rule


   class rule_001(rule.rule):

     def __init__(self):
         rule.rule.__init__(self, 'localized', '001')
         self.phase = 1
         self.fixable = False  # User must split the file

     def analyze(self, oFile):
         if oFile.hasEntity and oFile.hasArchitecture:
             self.add_violation(1)

We also need to provide a solution to the user so they will know how to fix the violation:

.. code-block:: python

   from vsg import rule


   class rule_001(rule.rule):

     def __init__(self):
         rule.rule.__init__(self, 'localized', '001')
         self.phase = 1
         self.fixable = False  # User must split the file
         self.solution = 'Split entity and architecture into seperate files.'

     def analyze(self, oFile):
         if oFile.hasEntity and oFile.hasArchitecture:
             self.add_violation(1)

The rule is complete, so we save it as rule_localized_001.py.
Performing an **ls** on our local_rules directory:

.. code-block:: bash

   $ ls ~/local_rules
   __init__.py  rule_localized_001.py

Use new rule to analyze
~~~~~~~~~~~~~~~~~~~~~~~

When we want to run with localized rules, use the **--local_rules** option.

.. code-block:: bash

   $ vsg -f RAM.vhd --local_rules ~/local_rules
   File:  RAM.vhd
   ==============
   Phase 1... Reporting
   localized_001            |            1 | Split entity and architecture into seperate files.
   Phase 2... Not executed
   Phase 3... Not executed
   Phase 4... Not executed
   Phase 5... Not executed
   Phase 6... Not executed
   Phase 7... Not executed
   ==============
   Total Rules Checked: 50
   Total Failures:      1

Our new rule will now flag files which have both an entity and an architecture in the same file.
