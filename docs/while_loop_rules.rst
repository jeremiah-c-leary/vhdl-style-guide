.. include:: icons.rst

While Loop Rules
----------------

while_loop_001
##############

|phase_4| |error| |indent|

This rule checks for indentation of the **while** keyword.
Proper indentation enhances comprehension.

**Violation**

.. code-block:: vhdl

   begin

   while (temp /= 0) loop
       temp := temp/2;
     end loop;

**Fix**

.. code-block:: vhdl

   begin

     while (temp /= 0) loop
       temp := temp/2;
     end loop;

while_loop_002
##############

This rule has been moved to **loop_statement_302**.

