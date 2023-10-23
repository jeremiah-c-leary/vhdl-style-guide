.. include:: includes.rst

Concurrent Selected Signal Assignment Rules
-------------------------------------------

.. code-block:: text

   concurrent_selected_signal_assignment ::=
     with expression select [ ? ]
       target <= [ guarded ] [ delay_mechanism ] selected_waveforms ;

   selected_waveforms ::=
     { waveform when choices , } waveform when choices

concurrent_selected_signal_assignment_400
#########################################

|phase_5| |error| |alignment|

This rule checks alignment of multiline concurrent selected signal statements.

|configuring_conditional_multiline_indent_rules_link|

**Violation**

.. code-block:: vhdl

   with mux_sel select addr <=
     c_input_data when 0,
     c_output_data when 1,
     (others => 'X') when others;

**Fix**

.. code-block:: vhdl

   with mux_sel select addr <=
     c_input_data    when 0,
     c_output_data   when 1,
     (others => 'X') when others;

