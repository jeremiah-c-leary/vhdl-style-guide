Usage
=====

VSG is a both a command line tool and a python package.
The command line tool can be invoked with:

.. code-block:: text

   $ vsg
   usage: VHDL Style Guide (VSG) [-h] [-f FILENAME [FILENAME ...]]
                                 [-lr LOCAL_RULES]
                                 [-c CONFIGURATION [CONFIGURATION ...]] [--fix]
                                 [-fp FIX_PHASE] [-j JUNIT] [-js JSON]
                                 [-of {vsg,syntastic,summary}] [-b]
                                 [-oc OUTPUT_CONFIGURATION]
                                 [-rc RULE_CONFIGURATION]
                                 [--style {indent_only,jcl}] [-v] [-ap]
                                 [--fix_only FIX_ONLY] [--stdin]
                                 [--quality_report QUALITY_REPORT] [-p JOBS]
                                 [--debug]

   Analyzes VHDL files for style guide violations. Reference documentation is
   located at: http://vhdl-style-guide.readthedocs.io/en/latest/index.html

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
     -b, --backup          Creates a copy of input file for comparison with fixed
                           version.
     -oc OUTPUT_CONFIGURATION, --output_configuration OUTPUT_CONFIGURATION
                           Write configuration to file name.
     -rc RULE_CONFIGURATION, --rule_configuration RULE_CONFIGURATION
                           Display configuration of a rule
     --style {indent_only,jcl}
                           Use predefined style
     -v, --version         Displays version information
     -ap, --all_phases     Do not stop when a violation is detected.
     --fix_only FIX_ONLY   Restrict fixing via JSON file.
     --stdin               Read VHDL input from stdin, disables all other file
                           selections, disables multiprocessing
     --quality_report QUALITY_REPORT
                           Create code quality report for GitLab
     -p JOBS, --jobs JOBS  number of parallel jobs to use, default is the number
                           of cpu cores
     --debug               Displays verbose debug information

**Command Line Options**

+-------------------------------+-------------------------------------------------+
| Option                        |  Description                                    |
+-------------------------------+-------------------------------------------------+
| -f FILENAME                   | The VHDL file to be analyzed or fixed.          |
|                               | Multiple files can be passed through this       |
|                               | option.                                         |
|                               | The path to each file can also be specified.    |
|                               | File globbing is also supported.                |
+-------------------------------+-------------------------------------------------+
| --stdin                       | Reads VHDL file input from standard in put      |
|                               | instead of reading from a file or files. Can be |
|                               | useful for using with other tools such as       |
|                               | editors that can interact through stdin/stdout  |
|                               | for diagnostics                                 |
+-------------------------------+-------------------------------------------------+
| --local_rules LOCAL_RULES     | Additional rules not in the base set.           |
+-------------------------------+-------------------------------------------------+
| --configuration CONFIGURATION | JSON or YAML file(s) which alters the behavior  |
|                               | of VSG.  Configuration can also include a list  |
|                               | files to analyze.  Any combination of JSON and  |
|                               | YAML files can be passed.  Each will be         |
|                               | processed in order from left to right.          |
+-------------------------------+-------------------------------------------------+
| --fix                         | Update issues found.                            |
|                               | Replaces current file with updated one.         |
+-------------------------------+-------------------------------------------------+
| --fix_phase                   | Applies for all phases up to and including      |
|                               | this phase.  Analysis will then be performed    |
|                               | on all phases.                                  |
+-------------------------------+-------------------------------------------------+
| --junit                       | Filename of JUnit XML file to generate.         |
|                               | The path to the file can also be specified, but |
|                               | the destination directory must exist.           |
+-------------------------------+-------------------------------------------------+
| --json                        | Filename of JSON file to generate.              |
|                               | The path to the file can also be specified, but |
|                               | the destination directory must exist.           |
+-------------------------------+-------------------------------------------------+
| --output_format               | Configures the sdout output format.             |
|                               |   vsg -- standard VSG output                    |
|                               |   syntastic -- format compatible with the       |
|                               |   syntastic VIM module                          |
|                               |   summary -- Minimal output useful when running |
|                               |   on multiple files                             |
+-------------------------------+-------------------------------------------------+
| --backup                      | Creates a copy of the input file before         |
|                               | applying any fixes.  This can be used to        |
|                               | compare the fixed file against the original.    |
|                               | NOTE:  This is only valid when using --fix.     |
+-------------------------------+-------------------------------------------------+
| --output_configuration        | Writes a JSON configuration file of the current |
|                               | run.  It includes a file_list, local_rules (if  |
|                               | used), and how every rule was configured.       |
|                               | This configuration can be fed back into VSG.    |
|                               | The path to the file can also be specified, but |
|                               | the destination directory must exist.           |
+-------------------------------+-------------------------------------------------+
| --rule_configuration          | Displays the configuration of a rule.           |
+-------------------------------+-------------------------------------------------+
| --style                       | Use a built in coding style.                    |
+-------------------------------+-------------------------------------------------+
| --version                     | Displays the version of VSG.                    |
+-------------------------------+-------------------------------------------------+
| --all-phases                  | Executes all phases without stopping if a       |
|                               | violation is found.                             |
|                               | NOTE: This is not valid with the --fix option.  |
+-------------------------------+-------------------------------------------------+
| --fix_only                    | Restrict which rules are fixed based on JSON    |
|                               | file.                                           |
+-------------------------------+-------------------------------------------------+
| --quality_report              | Write a quality report which can be used by     |
|                               | GitLab                                          |
+-------------------------------+-------------------------------------------------+
| --jobs                        | Restrict the number of cores used to run.  The  |
|                               | default is the number of cores available.       |
+-------------------------------+-------------------------------------------------+
| --debug                       | Print verbose debug information to assist with  |
|                               | debuging errors with VSG.                       |
+-------------------------------+-------------------------------------------------+


Here is an example output running against a test file:

.. code-block:: text

   $ vsg -f example/architecture-empty.vhd
   ================================================================================
   File:  example/architecture-empty.vhd
   ================================================================================
   Phase 1 of 7... Reporting
   Total Rules Checked: 83
   Total Violations:     3
     Error   :     3
     Warning :     0
   ----------------------------+------------+------------+--------------------------------------
     Rule                      |  severity  |  line(s)   | Solution
   ----------------------------+------------+------------+--------------------------------------
     port_021                  | Error      |         45 | Move the ( to the same line as the "port" keyword.
     instantiation_034         | Error      |        169 | Change to component instantiation
     generic_map_003           | Error      |        170 | Move the ( to the same line as the "generic map" keyword.
   ----------------------------+------------+--------------------------------------
   NOTE: Refer to online documentation at https://vhdl-style-guide.readthedocs.io/en/latest/index.html for more information.

VSG will report the rule which is violated and the line number or group of lines where the violation occured.
It also gives a suggestion on how to fix the violation.
The rules VSG uses are grouped together into :doc:`phases`.
These phases follow the order in which the user would take to address the violations.
Each rule is detailed in the :doc:`rules` section.
The violation and the appropriate fix for each rule is shown.

The violations can be fixed manually, or use the **--fix** option to have VSG update the file.

.. code-block:: text

   $ vsg -f example/architecture-empty.vhd
   ================================================================================
   File:  example/architecture-empty.vhd
   ================================================================================
   Phase 7 of 7... Reporting
   Total Rules Checked: 378
   Total Violations:    0

If rule violations can not be fixed, they will be reported after fixing everything that can be mixed:

.. code-block:: text

   $ vsg -f example/architecture-empty.vhd
   ================================================================================
   File:  example/architecture-empty.vhd
   ================================================================================
   Phase 1 of 7... Reporting
   Total Rules Checked: 83
   Total Violations:     1
     Error   :     1
     Warning :     0
   ----------------------------+------------+------------+--------------------------------------
     Rule                      |  severity  |  line(s)   | Solution
   ----------------------------+------------+------------+--------------------------------------
     instantiation_034         | Error      |        169 | Change to component instantiation
   ----------------------------+------------+--------------------------------------
   NOTE: Refer to online documentation at https://vhdl-style-guide.readthedocs.io/en/latest/index.html for more information.

Use Cases
#########

The following examples show how to perform certain tasks with VSG.

Checking a single file
----------------------

.. code-block:: text

   $ vsg -f fifo.vhd

Checking a single file over standard input
------------------------------------------

.. code-block:: text

   $ vsg --stdin

Checking multiple files using globbing
--------------------------------------

.. code-block:: text

   $ vsg -f *.vhd

Checking multiple files in different directories
------------------------------------------------

.. code-block:: text

   $ vsg -f fifos/src/*.vhd cpu_core/src/*.vhd usb_hub/src/*.vhd

Checking all files in a project
-------------------------------

.. code-block:: text

   $ find . -name "*.vhd" -exec vsg -f {} \;

Integration with CI server
--------------------------

.. code-block:: text

   $ vsg -f fifos/src/*.vhd --junit fifos/src/fifos_junit.xml

Fixing a single file
--------------------

.. code-block:: text

   $ vsg -f fifo.vhd --fix

Fixing multiple files using globbing
------------------------------------

.. code-block:: text

   $ vsg -f *.vhd --fix

Fixing all files in a project
-----------------------------

.. code-block:: text

   $ find . -name "*.vhd" -exec vsg -f {} --fix \;

Error Codes
###########

One of the following error codes will be returned after running VSG:

+------------+-------------------------------------------------+
| Error Code |  Description                                    |
+------------+-------------------------------------------------+
|     0      |  VSG ran without encountering any errors and no |
|            |  rule violations were detected.                 |
+------------+-------------------------------------------------+
|     1      |  VSG ran and detected a rule violation.         |
+------------+-------------------------------------------------+
|     2      |  An attempt was made to configure a rule which  |
|            |  was deprecated.                                |
+------------+-------------------------------------------------+
