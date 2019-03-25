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
                                  [-b] [-oc OUTPUT_CONFIGURATION]
    
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

VSG will report the rule which is violated and the line number or group of lines where the violation occured.
It also gives a suggestion on how to fix the violation.
The rules VSG uses are grouped together into :doc:`phases`.
These phases follow the order in which the user would take to address the violations.
Each rule is detailed in the :doc:`rules` section.
The violation and the appropriate fix for each rule is shown.

The violations can be fixed manually, or use the **--fix** option to have VSG update the file.

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

Multiple configuration example
------------------------------

More than one configuration can be passed using the **--configuration** option.
This can be useful in two situations:

  1)  Block level configurations
  2)  Multilevel rule configurations

The priority of the configurations is from right to left.
The last configuration has the highest priority.
This is true for all configuration parameters except **file_list**.

Block level configurations
##########################

Many code bases are large enough to be broken into multiple sub blocks.
A single configuration can be created and maintained for each subblock.
This allows each subblock to be analyzed independently.

When the entire code base needs be analyzed, all the subblock configurations can be passed to VSG.
This reduces the amount of external scripting required.

**config_1.json**

.. code-block:: json

   {
       "file_list":[
         "fifo.vhd",
         "source/spi.vhd",
         "$PATH_TO_FILE/spi_master.vhd",
         "$OTHER_PATH/src/*.vhd"
       ]
   }

**config_2.json**

.. code-block:: json

   {
       "file_list":[
         "dual_port_fifo.vhd",
         "flash_interface.vhd",
         "$PATH_TO_FILE/ddr.vhd"
       ]
   }

Both configuration files can be processed by vsg with the following command:

.. code-block:: bash

  $ vsg --configuration config_1.json config_2.json


Multilevel rule configurations
##############################

Some code bases may require rule adjustments that apply to all the files along with rule adjustments against individual files.
Use multiple configurations to accomplish this.
One configuration can handle code base wide adjustments.
A second configuration can target individual files.
VSG will combine any number of configurations to provide a unique set of rules for any file.

**config_1.json**

.. code-block:: json

   {
       "rule":{
           "entity_004":{
               "disable":true
           },
           "entity_005":{
               "disable":true
           },
           "global":{
               "indentSize":2
           }
       }
   }

**config_2.json**

.. code-block:: json

   {
       "rule":{
           "entity_004":{
               "disable":false,
               "indentSize":4
           }
       }
   }


Both configuration files can be processed by VSG with the following command:

.. code-block:: bash

  $ vsg --configuration config_1.json config_2.json -f fifo.vhd

VSG will combine the two configurations into this equivalent configuration...

.. code-block:: json

   {
       "rule":{
           "entity_004":{
               "disable":false,
               "indentSize":4
           },
           "entity_005":{
               "disable":true
           },
           "global":{
               "indentSize":2
           }
       }
   }

...and run on the file **fifo.vhd**.
