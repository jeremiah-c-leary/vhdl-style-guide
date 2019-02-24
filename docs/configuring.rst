Configuring
===========

VSG can use a configuration file to alter it's behavior or include a list of files to analyze.
This is accomplished by passing a JSON file through the **--configuration** command line argument.
This is the basic form of a configuration file: 

.. code-block:: json

   {
       "file_list":[
         "fifo.vhd",
         "source/spi.vhd",
         "$PATH_TO_FILE/spi_master.vhd"
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

It is not required to have **file_list**, **local_rules**, and **rule** defined in the configuration file.
Any combination can be defined.
The order does not matter either.

file_list
---------

The file_list is a list of files that will be analyzed.
Environment variables will expanded.
File globbing is also supported.
The Environment variables will be exanded before globbing occurs.
This option can be useful when running VSG over multiple files.

local_rules
-----------

Local rules can be defined on the command line or in a configuration file.
If they are defined in both locations, the configuration will have precedence.

rule
----

Any attribute of any rule can be configured.
Using **global** will set the attribute for every rule.
Each rule is addressable by using it's unique **ruleId** and **ruleNumber** combination.

.. NOTE::
   If **global** and unique attributes are set at the same time, the unique attribute will take precedent.


Here are a list of attributes that can be altered:

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

Example:  Disabling a rule
##########################

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
############################################################

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
########################################################

Configure the indent size for all rules by setting the **global** attribute.

.. code-block:: json

   {
       "rule":{
           "global":{
               "indentSize":4
           }
       }
   }
