.. include:: icons.rst

For Loop Rules
--------------

for_loop_001
############

|phase_4| |error| |indent|

This rule checks the indentation of the **for** keyword.

**Violation**

.. code-block:: vhdl

   fifo_proc : process () is
   begin

   for index in 4 to 23 loop

     end loop;

   end process;

**Fix**

.. code-block:: vhdl

   fifo_proc : process () is
   begin

     for index in 4 to 23 loop

     end loop;

   end process;

for_loop_002
############

This rule has been moved to **loop_statement_302**.

for_loop_003
############

This rule has been moved to **loop_statement_503**.

for_loop_004
############

This rule has been moved to **loop_statement_103**.

for_loop_005
############

This rule has been moved to **loop_statement_104**.

