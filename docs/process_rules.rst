Process Rules
-------------

process_010
###########
 
This rule checks the "begin" keyword is on it's own line.
Moving the begin to it's own line helps define the transition between the process declarative region and the sequential statements.

**Violation**

.. code-block:: vhdl

   PROC_A : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is begin

**Fix**

.. code-block:: vhdl

   PROC_A : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is
   begin


process_028
###########

This rule checks the alignment of the closing parenthesis of a sensitivity list.
Parenthesis on multiple lines should be in the same column.

**Violation**

.. code-block:: vhdl

   PROC_A : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                       )

**Fix**

.. code-block:: vhdl

   PROC_A : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    )

process_029
###########

This rule checks for **rising_edge** and **falling_edge** in processes.

**Violation**

.. code-block:: vhdl

   if (rising_edge(CLK)) then

   if (falling_edge(CLK)) then

**Fix**

.. code-block:: vhdl

   if (CLK'event and CLK = '1') then

   if (CLK'event and CLK = '0') then

