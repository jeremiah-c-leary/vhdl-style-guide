Subtype Rules
-------------

subtype_001
###########

This rule checks for indentation of the subtype keyword.
Proper indentation enhances comprehension.

The indent amount can be controlled by the **indentSize** attribute on the rule.
**indentSize** defaults to 2.

**Violation**

.. code-block:: vhdl

   architecture RTL of entity FIFO is

         subtype width is range 0 to 9;

   subtype length is range 5 to 20;

   begin

**Fix**

.. code-block:: vhdl

   architecture RTL of entity FIFO is

     subtype width is range 0 to 9;

     subtype length is range 5 to 20;

   begin

**Configuration**

.. code-block:: json

   {
     "rule":{
       "subtype_001":{
         "indentSize":4
       }
     }
   }
