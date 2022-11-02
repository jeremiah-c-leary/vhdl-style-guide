.. include:: includes.rst

Selected Assignment Rules
-------------------------

selected_assignment_001
#######################

|phase_1| |error| |structure|

This rule checks the structure of selected assignments.

|configuring_selected_assignment_structure_rules_link|

**Violation**

.. code-block:: vhdl

   with mux_sel select addr := "0000"when 0, "0001" when 1, "1111"  when others;

**Fix**

.. code-block:: vhdl

   with mux_sel select
     addr := "0000" when 0,
             "0001" when 1,
             "1111" when others;

