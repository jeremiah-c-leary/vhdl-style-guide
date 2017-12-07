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

   function FUNC1 (v : in natural) return natural is
     variable temp, log : natural;
   begin

   while (temp /= 0) loop
       temp := temp/2;
     end loop;

     return temp;

   end function FUNC1;

**Fix**

.. code-block:: vhdl

   function FUNC1 (v : in natural) return natural is
     variable temp, log : natural;
   begin

     while (temp /= 0) loop
       temp := temp/2;
     end loop;

     return temp;

   end function FUNC1;


**Configuration**

.. code-block:: json

   {
     "rule":{
       "subtype_001":{
         "indentSize":4
       }
     }
   }
