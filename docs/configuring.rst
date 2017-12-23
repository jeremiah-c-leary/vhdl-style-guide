Configuring
===========

Any attribute of any rule can be configured using the --configuration option and a JSON file.
This is the basic form of a configuration file: 

.. code-block:: json

   {
       "rule":{
           "global":{
               "attributeName":"AttributeValue" 
           },
           "ruleId_ruleNumber":{
               "attributeName":"AttributeValue" 
           }
       }
   }

Using **global** will set the attribute for every rule.
Each rule is addressable by using it's unique **ruleId** and **ruleNumber** combination.

.. NOTE::
   If **global** and unique attributes are set at the same time, the unique attribute will take precedent.


Here are a list of attributes that can be altered:

+-------------+--------------------------------------------------+
| Attribute   | Description                                      |
+=============+==================================================+
| indentSize  | Sets the number of spaces for each indent level. |
+-------------+--------------------------------------------------+
| phase       | Sets the phase the rule will run in.             |
+-------------+--------------------------------------------------+
| disable     | If set to True, the rule will not run.           |
+-------------+--------------------------------------------------+
| fixable     | If set to False, the violation will not be fixed |
+-------------+--------------------------------------------------+

Example Configuration: Disabling a rule
---------------------------------------

Below is an example of a JSON file which disables the rule **entity_004**

.. code-block:: json

   {
       "rule":{
           "entity_004":{
               "disable":"True"
           }
       }
   }


Example Configuration: Setting the indent increment size
--------------------------------------------------------

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

...or configured for every rule using **global**:


.. code-block:: json

   {
       "rule":{
           "global":{
               "indentSize":4
           }
       }
   }

