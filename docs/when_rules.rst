.. include:: includes.rst

When Rules
----------

These rules cover the usage of **when** keywords in sequential and concurrent statements.

when_001
########

|phase_1| |error| |structure|

This rule checks the **else** keyword is not at the beginning of a line.
The else should be at the end of the preceeding line.

**Violation**

.. code-block:: vhdl

   wr_en <= '1' when a = '1' -- This is comment
            else '0' when b = '0'
            else c when d = '1'
            else f;

**Fix**

.. code-block:: vhdl

   wr_en <= '1' when a = '1' else -- This is a comment
            '0' when b = '0' else
            c when d = '1' else
            f;

