For Loop Rules
--------------

for_loop_001
############

This rule checks the indentation of the **for** keyword.

**Violation**

.. code-block:: vhdl

   FIFO_PROC : process () is
   begin

   for index in 4 to 23 loop

     end loop;

   end process;

**Fix**

.. code-block:: vhdl

   FIFO_PROC : process () is
   begin

     for index in 4 to 23 loop

     end loop;

   end process;

for_loop_002
############

This rule checks the indentation of the **end loop** keywords.

**Violation**

.. code-block:: vhdl

   FIFO_PROC : process () is
   begin

     for index in 4 to 23 loop

        end loop;

   end process;

**Fix**

.. code-block:: vhdl

   FIFO_PROC : process () is
   begin

     for index in 4 to 23 loop

     end loop;

   end process;

