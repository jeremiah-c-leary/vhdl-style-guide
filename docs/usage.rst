Usage
=====

VSG is a both a command line tool and a python package.
The command line tool can be invoked with:

.. code-block:: bash

    $ vsg
    usage: VHDL Style Guide (VSG) [-h] [-f FILENAME [FILENAME ...]]
                                  [-lr LOCAL_RULES]
                                  [-c CONFIGURATION [CONFIGURATION ...]] [--fix]
                                  [-fp FIX_PHASE] [-j JUNIT] [-of {vsg,syntastic}]
                                  [-b] [-oc OUTPUT_CONFIGURATION] [-v]
    
    Analyzes VHDL files for style guide violations. Reference documentation is
    located at: http://vhdl-style-guide.readthedocs.io/en/latest/index.html
    
    optional arguments:
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
      -of {vsg,syntastic}, --output_format {vsg,syntastic}
                            Sets the output format.
      -b, --backup          Creates copy of input file for comparison with fixed
                            version.
      -oc OUTPUT_CONFIGURATION, --output_configuration OUTPUT_CONFIGURATION
                            Output configuration file name
      -v, --version         Displays version information

**Command Line Options**

+-------------------------------+-------------------------------------------------+
| Option                        |  Description                                    |
+===============================+=================================================+
| -f FILENAME                   | The VHDL file to be analyzed or fixed.          |
|                               | Multiple files can be passed through this       |
|                               | option.                                         |
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
+-------------------------------+-------------------------------------------------+
| --output_format               | Configures the sdout output format.             |
|                               |   vsg -- standard VSG output                    |
|                               |   syntastic -- format compatible with the       |
|                               |   syntastic VIM module                          |
+-------------------------------+-------------------------------------------------+
| --backup                      | Creates a copy of the input file before         |
|                               | applying any fixes.  This can be used to        |
|                               | compare the fixed file against the original.    |
+-------------------------------+-------------------------------------------------+
| --output_configuration        | Writes a JSON configuration file of the current |
|                               | run.  It includes a file_list, local_rules (if  |
|                               | used), and how every rule was configured.       |
|                               | This configuration can be fed back into VSG.    |
+-------------------------------+-------------------------------------------------+
| --rule_configuration          | Displays the configuration of a rule.           |
+-------------------------------+-------------------------------------------------+
| --version                     | Displays the version of VSG.                    |
+-------------------------------+-------------------------------------------------+


Here is an example output running against a test file:

.. code-block:: bash

   $ vsg -f example/architecture-empty.vhd
   ================================================================================
   File:  example/architecture-empty.vhd
   ================================================================================
   Phase 2 of 7... Reporting
   Total Rules Checked: 151
   Total Violations:    3
   ----------------------------+------------+--------------------------------------
     Rule                      |  line(s)   | Solution
   ----------------------------+------------+--------------------------------------
     signal_003                |          4 | Ensure there are only 1 space(s) after the "signal" keyword.
     signal_005                |          4 | Ensure only a signal space after the colon.
     signal_005                |          5 | Ensure only a signal space after the colon.
   ----------------------------+------------+--------------------------------------
   NOTE: Refer to online documentation at https://vhdl-style-guide.readthedocs.io/en/latest/index.html for more information.

VSG will report the rule which is violated and the line number or group of lines where the violation occured.
It also gives a suggestion on how to fix the violation.
The rules VSG uses are grouped together into :doc:`phases`.
These phases follow the order in which the user would take to address the violations.
Each rule is detailed in the :doc:`rules` section.
The violation and the appropriate fix for each rule is shown.

The violations can be fixed manually, or use the **--fix** option to have VSG update the file.

.. code-block:: bash

   $ vsg -f example/architecture-empty.vhd
   ================================================================================
   File:  example/architecture-empty.vhd
   ================================================================================
   Phase 7 of 7... Reporting
   Total Rules Checked: 378
   Total Violations:    0

If rule violations can not be fixed, they will be reported after fixing everything else:

.. code-block:: bash

   $ vsg -f example/architecture-empty.vhd
   ================================================================================
   File:  example/architecture-empty.vhd
   ================================================================================
   Phase 1 of 7... Reporting
   Total Rules Checked: 61
   Total Violations:    1
   ----------------------------+------------+--------------------------------------
     Rule                      |  line(s)   | Solution
   ----------------------------+------------+--------------------------------------
     signal_007                |          5 | Remove default assignment.
   ----------------------------+------------+--------------------------------------
   NOTE: Refer to online documentation at https://vhdl-style-guide.readthedocs.io/en/latest/index.html for more information.
