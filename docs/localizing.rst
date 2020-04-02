Localizing
==========

VSG supports customization to your coding style standards by allowing localized rules.
These rules are stored in a directory with an __init__.py file and one or more python files.
The files should follow the same structure and naming convention as the rules found in the vsg/rules directory.

The localized rules will be used when the **--local_rules** command line argument is given or using the **local_rules** option in a configuration file.

Example: Create rule to check for entity and architectures in the same file.
----------------------------------------------------------------------------

Let's suppose in our organization the entity and architecture should be split into separate files.
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
There are helper functions in :doc:`vsg.utilities`, :doc:`vsg.check`, and :doc:`vsg.fix` also.
In this case, the vsg.vhdlFile class has two attributes (**hasEntity** and **hasArchitecture**) that are exactly what we need.
We are ready to write the body of the **analyze** method:

.. code-block:: python

   from vsg import rule


   class rule_001(rule.rule):

     def __init__(self):
         rule.rule.__init__(self, 'localized', '001')
         self.phase = 1

     def analyze(self, oFile):
         if oFile.hasEntity and oFile.hasArchitecture:
             self.add_violation(utils.create_violation_dict(1))

The base rule class has an **add_violation** method which takes a dictionary as an argument.
The *create_violation_dict* function will create the dictionary.
This dictionary can be modified to include other information about the violation. 
This method appends the dictionary to a violation list, which is processed later for reporting and fixing purposes.
In this case, any line number will do so we picked 1.

We must decide if we want to give VSG the ability to fix this rule on it's own.
If so, then we will need to write the **_fix_violations** method.
However, for this violation we want the user to split the file.
We will tell VSG the rule is not fixable.

.. code-block:: python

   from vsg import rule


   class rule_001(rule.rule):

     def __init__(self):
         rule.rule.__init__(self, 'localized', '001')
         self.phase = 1
         self.fixable = False  # User must split the file

     def analyze(self, oFile):
         if oFile.hasEntity and oFile.hasArchitecture:
             self.add_violation(utils.create_violation_dict(1))

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
             self.add_violation(utils.create_violation_dict(1))

Finally, we need to add a code tag check so the rule can be disabled via comments in the code:

.. code-block:: python

   from vsg import rule


   class rule_001(rule.rule):

     def __init__(self):
         rule.rule.__init__(self, 'localized', '001')
         self.phase = 1
         self.fixable = False  # User must split the file
         self.solution = 'Split entity and architecture into seperate files.'

     def analyze(self, oFile):
         if not self.is_vsg_off(oLine):
             if oFile.hasEntity and oFile.hasArchitecture:
                 self.add_violation(utils.create_violation_dict(1))

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
That was a fairly simple rule.
To write more complex rules, it is important to understand how the rule class works.

Understanding the Rule class
----------------------------

Every rule uses the base rule class.
There are a few methods to the base rule class, but we are interested in only the following:

+-----------------+-------------------------------------------+
| Method          | Description                               |
+-----------------+-------------------------------------------+
| add_violations  | Adds violations to a list.                |
+-----------------+-------------------------------------------+
| analyze         | Calls _pre_analyze and then _analyze.     |
+-----------------+-------------------------------------------+
| _analyze        | Code that performs the analysis.          |
+-----------------+-------------------------------------------+
| fix             | calls analyze and then _fix_violations.   |
+-----------------+-------------------------------------------+
| _fix_violations | Code that fixes the violations.           |
+-----------------+-------------------------------------------+
| _get_solution   | Prints out the solution to stdout.        |
+-----------------+-------------------------------------------+
| _pre_analyze    | Code that sets up variables for _analyze. |
+-----------------+-------------------------------------------+

We will look at the rule **constant_014** to illustrate how VSG uses the methods above:

.. code-block:: python

    class rule_014(rule.rule):
        '''
        Constant rule 014 checks the indent of multiline constants that are not arrays.
        '''
    
        def __init__(self):
            rule.rule.__init__(self)
            self.name = 'constant'
            self.identifier = '014'
            self.solution = 'Align with := keyword on constant declaration line.'
            self.phase = 5
    
        def _pre_analyze(self):
            self.alignmentColumn = 0
            self.fKeywordFound = False
    
        def _analyze(self, oFile, oLine, iLineNumber):
            if not oLine.isConstantArray and oLine.insideConstant:
                if oLine.isConstant and ':=' in oLine.line:
                    self.alignmentColumn = oLine.line.index(':=') + len(':= ')
                    self.fKeywordFound = True
                elif not oLine.isConstant and self.fKeywordFound:
                    sMatch = ' ' * self.alignmentColumn
                    if not re.match('^' + sMatch + '\w', oLine.line):
                        self.add_violation(utils.create_violation_dict(LineNumber))
                        self.dFix['violations'][iLineNumber] = self.alignmentColumn
                if oLine.isConstantEnd:
                    self.fKeywordFound = False
    
        def _fix_violations(self, oFile):
            for iLineNumber in self.violations:
                sLine = oFile.lines[iLineNumber].line
                sNewLine = ' ' * self.dFix['violations'][iLineNumber] + sLine.strip()
                oFile.lines[iLineNumber].update_line(sNewLine)

Creating Class
~~~~~~~~~~~~~~

First we create the rule by inheriting from the base rule class.
We also add a comment to describe what the rule is doing.

.. code-block:: python

    class rule_014(rule.rule):
        '''
        Constant rule 014 checks the indent of multiline constants that are not arrays.
        '''

Adding __init__
~~~~~~~~~~~~~~~~
    
Then we add the **__init__** method.
It calls the init of the base rule class, then we modify attributes for this specific rule:

.. code-block:: python

        def __init__(self):
            rule.rule.__init__(self)
            self.name = 'constant'
            self.identifier = '014'
            self.solution = 'Align with := keyword on constant declaration line.'
            self.phase = 5

For this rule we set it's *name*, *identifier*, *solution*, and *phase*.

Analyzing Considerations
~~~~~~~~~~~~~~~~~~~~~~~~

The **analyze** method of the base rule class will first call **_pre_anaylze** before **_analyze**.
The **_analyze** method is wrapped in a loop that increments through each line of the file.
The **analyze** method also checks if the rule has been turned off for a line, via code tags.
If the code tag indicates to ignore the line, then it will be skipped.
If you decide to override the **analyze** method, then you should add the code tag check.

Adding _pre_analyze method
~~~~~~~~~~~~~~~~~~~~~~~~~~


In this rule, we use the **_pre_analyze** method to initialize some variables.
These variables must be set outside the loop that is present in the **analyze** method.

.. code-block:: python

        def _pre_analyze(self):
            self.alignmentColumn = 0
            self.fKeywordFound = False

Adding _analyze method
~~~~~~~~~~~~~~~~~~~~~~

The **_analyze** method is called on every line of the VHDL file.
Any memory needed between lines must be declared in the **_pre_analyze** method.
In the following code, notice *self.alignmentColumn* and *self.fKeywordFound*.

.. code-block:: python

        def _analyze(self, oFile, oLine, iLineNumber):
            if not oLine.isConstantArray and oLine.insideConstant:
                if oLine.isConstant and ':=' in oLine.line:
                    self.alignmentColumn = oLine.line.index(':=') + len(':= ')
                    self.fKeywordFound = True
                elif not oLine.isConstant and self.fKeywordFound:
                    sMatch = ' ' * self.alignmentColumn
                    if not re.match('^' + sMatch + '\w', oLine.line):
                        self.add_violation(utils.create_violation_dict(LineNumber))
                        self.dFix['violations'][iLineNumber] = self.alignmentColumn
                if oLine.isConstantEnd:
                    self.fKeywordFound = False

This code is searching for the characteristics of a non-array constant.

.. code-block:: python

        def _analyze(self, oFile, oLine, iLineNumber):
            if not oLine.isConstantArray and oLine.insideConstant:

Once the non-array constant is found, it notes the column of the *:=* keyword.

.. code-block:: python

                if oLine.isConstant and ':=' in oLine.line:
                    self.alignmentColumn = oLine.line.index(':=') + len(':= ')
                    self.fKeywordFound = True

On successive lines of the constant declaration, it checks to see if there are enough spaces from the beginning of the line to match the column number the *:=* is located at.

.. code-block:: python

                elif not oLine.isConstant and self.fKeywordFound:

If there are not enough spaces, then a violation is added.
We also store off the required column into a predefined dictionary named *dFix*.
This will be used later when the **fix** method is called.

.. code-block:: python

                    sMatch = ' ' * self.alignmentColumn
                    if not re.match('^' + sMatch + '\w', oLine.line):
                        self.add_violation(utils.create_violation_dict(LineNumber))
                        self.dFix['violations'][iLineNumber] = self.alignmentColumn

When we detect the end of the constant declaration, we clear a flag and prepare for the next constant declaration.

.. code-block:: python

                if oLine.isConstantEnd:
                    self.fKeywordFound = False

Fixing considerations
~~~~~~~~~~~~~~~~~~~~~

The **fix** method will first call the **analyze** method and then the **_fix_violations** method.
Unlike the **analyze** method, it does not wrap the **_fix_violations** in a loop.
This is due to some fixes needing to execute either top down or bottom up.
Rules that add or delete lines need to work from the bottom up.
Otherwise, the violations detected by the **analyze** method will have moved.

Adding the _fix_violations method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this rule, we are going to iterate on all the violations in the *self.violations* attribute.

.. code-block:: python

        def _fix_violations(self, oFile):
            for iLineNumber in self.violations:

We store the current line off to make it easier to read.
Then we strip the line of all leading and trailing spaces and prepend the number of spaces required to align with the *:=* keyword.

.. code-block:: python

                sLine = oFile.lines[iLineNumber].line
                sNewLine = ' ' * self.dFix['violations'][iLineNumber] + sLine.strip()

Finally, we update the line with our modified line using the **update_line** method.

.. code-block:: python

                oFile.lines[iLineNumber].update_line(sNewLine)

Violation dictionary
--------------------

Violations are stored as a list of dictionaries in the **rule.violations** attribute.
This is the generic format of the dictionary represented by json:

.. code-block:: json

   {
     "lines" : [ 
        {
          "number" : "<integer>",
          "<line_attribute>" : "<line_value>",
          "<line_attribute>" : "<line_value>"
        }
       ],
     "<violation_attribute>" : "<violation_value>",
     "<violation_attribute>" : "<violation_value>"
   }

This format gives us the greatest flexibility in describing violations.
The lines[0]['number'] is the only required element in a violation dictionary.
The "<line_attribute>" and "<violation_attribute>" elements are optional.
They are used by more complex rules to maintain information used to fix violations.

Single line violations
~~~~~~~~~~~~~~~~~~~~~~

Most violations are against a single line and no other information is required to fix it.
These dictionaries use the minimumal form.

.. code-block:: json

   {
     "lines" : [ 
        {
          "number" : 40
        }
       ]
   }

Single line violations with additional information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If additional information for single line violations is required, it will be stored at the **violation** level.

.. code-block:: json

   {
     "lines" : [
       {
         "number" : 40
       }
     ],
     "label" : "FIFO"
   }

This violation is indicating there is an issue at line 40 with the label "FIFO".
The "label" element will be used to fix the violation.

Multiple line violations
~~~~~~~~~~~~~~~~~~~~~~~~

If a rule covers multiple lines, then information about individual lines can be stored:

.. code-block:: json

   {
     "lines" : [
       {
         "number" : 40,
         "column" : 20
       },
       {
         "number" : 41,
         "column" : 35
       }
     ],
     "desired_column" : 15
   }
       
In the above case, we are trying to align a keyword over multiple lines.
Each line which is not aligned is reported in the **lines** list.
The **column** attribute indicates which column the keyword was found.
The **desired_column**, which applies to all lines in the **lines** list, indicates which column the keyword should be located.

This violation would cover a group of multiple lines.
If there were violations in multiple groups, then each group with get it's own violation dictionary.

utils functions
~~~~~~~~~~~~~~~

There are three functions in the utils module to help with managing the violation dictionary: **create_violation_dict**, **get_violation_line_number** and **get_violating_line**.
The **create_violation_dict** will return a dictionary in the form of the single line violation described above.
Use this to create the initial violation and add to it as necessary.

The **get_violation_line_number** will return the lines['number'] attribute of the violation.
Use this function to abstract away the line number from the underlying data structure.

The **get_violating_line** will return a line object at the line the violation occured.
This is easier than manually indexing into the oFile list to pull out a line.

Rule creation guidelines
------------------------

Keep these points in mind when creating new rules:

#. Use an existing rule as a starting point
#. Remember that **analyze** calls **_pre_analyze** and then **_analyze**
#. Override **_get_solution** to return complex messages
#. **analyze** method can be overridden if necessary
#. If overriding **analyze**, then include a check for *vsg_off*

