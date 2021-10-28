.. include:: icons.rst

Loop Statement Rules
--------------------

loop_statement_300
##################

|phase_4| |error|

This rule checks the indentation of the **loop** keyword.

**Violation**

.. code-block:: vhdl

   fifo_proc : process () is
   begin

       loop

     end loop;

   end process;

**Fix**

.. code-block:: vhdl

   fifo_proc : process () is
   begin

     loop

     end loop;

   end process;
