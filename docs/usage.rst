Usage
=====

VSG is a both a command line tool and a python package.
The command line tool can be invoked with:

.. code-block:: bash

   $ vsg
   
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


**Command Line Options**

+-------------------------------+---------------------------------------------+
| Option                        |  Description                                |
+===============================+=============================================+
| -f FILENAME                   | The VHDL file to be analyzed or fixed.      |
|                               | This must be syntaxtically correct.         |
+-------------------------------+---------------------------------------------+
| --local_rules LOCAL_RULES     | Additional rules not in the base set.       |
+-------------------------------+---------------------------------------------+
| --configuration CONFIGURATION | JSON file which alters the behavior of VSG. |
+-------------------------------+---------------------------------------------+
| --fix                         | Update issues found.                        |
|                               | Raplaces current file with updated one.     |
+-------------------------------+---------------------------------------------+


Here is an example output running against a test file:

.. code-block:: bash

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

VSG will report the rule which is violated the line number or group of lines where the violation occured.
It also gives a suggestion on how to fix the violation.

The rules VSG uses are grouped together into :doc:`phases`.
Each rule is described in the :doc:`rules` section.

The violations can be fixed manually, or you can use the **--fix** option to have VSG update the file.

.. code-block:: bash

   $ vsg -f PIC.vhd --fix
   File:  PIC.fixed.vhd
   ====================
   Phase 1... Reporting
   Phase 2... Reporting
   Phase 3... Reporting
   Phase 4... Reporting
   Phase 5... Reporting
   Phase 6... Reporting
   Phase 7... Reporting
   ====================
   Total Rules Checked: 290
   Total Failures:      0

If rule violations can not be fixed, they will be reported after fixing everything else:

.. code-block:: bash

   $ vsg -f PIC.vhd --fix
   File:  PIC.vhd
   ==============
   Phase 1... Reporting
     signal_007                |         66 | Remove default assignment.
     signal_007                |         67 | Remove default assignment.
     signal_007                |         68 | Remove default assignment.
     signal_007                |         72 | Remove default assignment.
     signal_007                |         73 | Remove default assignment.
     signal_007                |         74 | Remove default assignment.
     process_016               |         78 | Add a label for the process.
     process_018               |        259 | Add a label for the "end process".
   Phase 2... Not executed
   Phase 3... Not executed
   Phase 4... Not executed
   Phase 5... Not executed
   Phase 6... Not executed
   Phase 7... Not executed
   ==============
   Total Rules Checked: 48
   Total Failures:      8

