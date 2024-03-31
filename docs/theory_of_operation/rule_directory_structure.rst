Rule Directory Structure
------------------------

Rules are located under the directory vsg/rules.
Each directory under vsg/rules corresponds to a group of rules.
For example, all architecture rules are in a directory named:  vsg/rules/architecture.
Each file under a rule group directory follows this pattern: rule_[0-9][0-9][0-9].py.

The diagram below illustrates rule directory structure given the descriptions above:

.. code-block:: text

   vsg
   └── rules
       ├── after
       │   ├── rule_001.py
                 ...
       │   └── rule_003.py
       ├── alias_declaration
       │   ├── rule_001.py
                 ...
       │   └── rule_601.py
       └── architecture
           ├── rule_001.py
                 ...
           └── rule_601.py

In addition to each rule definition, there are base rules in the vsg/rules directory.
The base rules provide a consistent implementation of a particular type of rule.
For example all rules which address lines before keywords will use the previous_line base rule.

.. code-block:: text

   └── vsg
       └── rules
               ...
           └── previous_line.py
               ...

There are also several utility files along with the base rules to provide helpful functions.
