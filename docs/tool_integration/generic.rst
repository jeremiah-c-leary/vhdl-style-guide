Generic Tool Integration
------------------------

VSG supports integration with other tools via several command line options.

+-------------------------------+-------------------------------------------------+
| --all_phases                  | Executes all phases without stopping if a       |
|                               | violation is found.                             |
+-------------------------------+-------------------------------------------------+
| --json                        | Filename of JSON file to generate.              |
+-------------------------------+-------------------------------------------------+
| --fix_only                    | Filename of JSON file with fix instructions     |
+-------------------------------+-------------------------------------------------+

--all_phases
############

VSG has a concept of phases, where violations in one phase should be addressed before moving to the next phase.
The **--all_phases** option will run an analysis over all the phases.
It will not stop if a violation has occurred.

This option can be useful when integrating VSG into an editor that supports linters.
It is important to note there are dependencies between some rules.
If violations for a later phase are fixed before violations on an earlier phase, it could lead to reoccurrences of violations until the correct order is followed.

--json
######

The violations discovered by VSG can be saved in a JSON formatted file.
This eases the transferring information from VSG to another tool.

Below is the basic format of the JSON file:

.. code-block:: text

   {
     "<filename>": {
       "violations": [
         {
           "rule": <rule_id>,
           "linenumber": <linenumber>,
           "solution": <solution>
         }
       ]
     }
   }

where:

+-------------------------------+-------------------------------------------------+
| <filename>                    | Name of the file violations refer to.           |
+-------------------------------+-------------------------------------------------+
| <rule_id>                     | The rule identifier and number.                 |
+-------------------------------+-------------------------------------------------+
| <linenumber>                  | The linenumber of the violation.                |
+-------------------------------+-------------------------------------------------+
| <solution>                    | The solution required to fix the violation.     |
+-------------------------------+-------------------------------------------------+

--fix_only
##########

Using this option with the **--fix** option will restrict the rules fixed base on a JSON file.
This allows tools a finer granularity in instructing VSG how to fix a file.

Below is the basic format of the JSON file:

.. code-block:: text

   {
     "fix": {
        "rule": {
          "<rule_id>": [ <number> ]
        }
     }
   }

where:

+-------------------------------+-------------------------------------------------+
| <rule_id>                     | The rule identifier and number.                 |
+-------------------------------+-------------------------------------------------+
| <number>                      | If this value is "all", then all violations     |
|                               | will be fixed.  If it is a series of numbers,   |
|                               | then only those lines will be fixed.            |
+-------------------------------+-------------------------------------------------+

It is important to note there are rules that will modify the line number at which errors occur.
The number reported at the command line or via the **--json** option are after all rules have been applied.
Therefore, when using **--fix_only** option the line numbers given in the JSON file may not line up with the line number while VSG is analyzing the file while it is being modified.
