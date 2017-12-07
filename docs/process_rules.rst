Process Rules
-------------

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

