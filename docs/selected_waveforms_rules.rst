.. include:: includes.rst

Selected Waveforms Rules
------------------------

selected_waveforms_500
######################

|phase_6| |error| |case| |case_keyword|

This rule checks the **when** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   with mux_sel select
     addr <= "0000" WHEN 0,
             "0001" WHEN 1,
             "1111" WHEN others;

**Fix**

.. code-block:: vhdl

   with mux_sel select
     addr <= "0000" when 0,
             "0001" when 1,
             "1111" when others;

