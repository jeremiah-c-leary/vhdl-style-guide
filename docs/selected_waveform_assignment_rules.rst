.. include:: includes.rst

Selected Waveform Assignment Rules
----------------------------------

selected_waveform_assignment_300
################################

|phase_4| |error| |indent|

This rule checks the indent of the **with** keyword.

**Violation**

.. code-block:: vhdl

   wr_en <= '1';

       with mux_sel select
     addr <= "0000" when 0,
             "0001" when 1,
             "1111" when others;

**Fix**

.. code-block:: vhdl

   wr_en <= '1';

   with mux_sel select
     addr <= "0000" when 0,
             "0001" when 1,
             "1111" when others;

