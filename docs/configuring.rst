Configuring
===========

VSG can use a configuration file to alter it's behavior or include a list of files to analyze.
This is accomplished by passing JSON and/or YAML file(s) through the **--configuration** command line argument.
This is the basic form of a configuration file in JSON: 

.. code-block:: json

   {
       "file_list":[
         "fifo.vhd",
         "source/spi.vhd",
         "$PATH_TO_FILE/spi_master.vhd",
         "$OTHER_PATH/src/*.vhd"
       ],
       "local_rules":"$DIRECTORY_PATH",
       "rule":{
           "global":{
               "attributeName":"AttributeValue" 
           },
           "ruleId_ruleNumber":{
               "attributeName":"AttributeValue" 
           }
       }
   }

This is the basic form of a configuration file in YAML:

.. code-block:: yaml

   ---
   file_list:[
     - fifo.vhd
     - source/spi.vhd
     - $PATH_TO_FILE/spi_master.vhd
     - $OTHER_PATH/src/*.vhd
   local_rules: $DIRECTORY_PATH
   rule:
     global:
       attributeName: AttributeValue
     ruleId_ruleNumber:
         attributeName: AttributeValue
   ...


It is not required to have **file_list**, **local_rules**, and **rule** defined in the configuration file.
Any combination can be defined.
The order does not matter either.

.. NOTE:: All examples of configurations in this documentation use JSON.  However, YAML can be used instead.

file_list
---------

The file_list is a list of files that will be analyzed.
Environment variables will expanded.
File globbing is also supported.
The Environment variables will be expanded before globbing occurs.
This option can be useful when running VSG over multiple files.

local_rules
-----------

Local rules can be defined on the command line or in a configuration file.
If they are defined in both locations, the configuration will take precedence.

rule
----

Any attribute of any rule can be configured.
Using **global** will set the attribute for every rule.
Each rule is addressable by using it's unique **ruleId** and **ruleNumber** combination.  For example, whitespace_006 or port_010.

.. NOTE::
   If **global** and unique attributes are set at the same time, the unique attribute will take precedence.


Here are a list of attributes that can be altered for each rule:

+-------------+---------+--------------------------------------------------+
| Attribute   | Values  | Description                                      |
+=============+=========+==================================================+
| indentSize  | Integer | Sets the number of spaces for each indent level. |
+-------------+---------+--------------------------------------------------+
| phase       | Integer | Sets the phase the rule will run in.             |
+-------------+---------+--------------------------------------------------+
| disable     | Boolean | If set to True, the rule will not run.           |
+-------------+---------+--------------------------------------------------+
| fixable     | Boolean | If set to False, the violation will not be fixed |
+-------------+---------+--------------------------------------------------+

.. NOTE:: Some rules have additional attributes.  These will be noted in the rule description.

Reporting Single Rule Configuration
-----------------------------------

The configuration for a single rule can be reported using the **-rc** option:

.. code-block:: bash

   $ vsg -rc entity_001
   {
     "rule": {
       "entity_001": {
         "indentSize": 2,
         "phase": 4,
         "disable": false,
         "fixable": true
       }
     }
   }

VSG will print the configuration for the rule given in a JSON format.
This configuration can be altered and added to a configuration file.

Reporting Configuration for All Rules
-------------------------------------

Every rule configuration can be report and saved to a file using the **-oc** option:

.. code-block:: bash

   $ vsg -oc configuration.json

The output file will be in JSON format and can be modified and passed back to VSG using the *-c* option.

Example:  Disabling a rule
--------------------------

Below is an example of a JSON file which disables the rule **entity_004**

.. code-block:: json

   {
       "rule":{
           "entity_004":{
               "disable":true
           }
       }
   }

Use the configuration with the **--configuration** command line argument:

.. code-block:: bash

   $ vsg -f RAM.vhd --configuration entity_004_disable.json

Example: Setting the indent increment size for a single rule
------------------------------------------------------------

The indent increment size is the number of spaces an indent level takes.
It can be configured on an per rule basis...

.. code-block:: json

   {
       "rule":{
           "entity_004":{
               "indentSize":4
           }
       }
   }

Example: Setting the indent increment size for all rules
--------------------------------------------------------

Configure the indent size for all rules by setting the **global** attribute.

.. code-block:: json

   {
       "rule":{
           "global":{
               "indentSize":4
           }
       }
   }

.. include:: configuring_case.rst
.. include:: configuring_prefix_suffix.rst
.. include:: configuring_number_of_signals.rst
.. include:: configuring_line_length.rst
.. include:: configuring_keyword_alignment.rst
