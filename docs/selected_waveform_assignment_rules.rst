.. include:: includes.rst

Selected Waveform Assignment Rules
----------------------------------

selected_waveform_assignment_100
################################

|phase_2| |error| |whitespace|

This rule checks for a single space after the **with** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   with    mux_sel select
     addr <= "0000" when 0,
             "0001" when 1,
             "1111" when others;

**Fix**

.. code-block:: vhdl

   with mux_sel select
     addr <= "0000" when 0,
             "0001" when 1,
             "1111" when others;

selected_waveform_assignment_101
################################

|phase_2| |error| |whitespace|

This rule checks for a single space before the **select** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   with mux_sel     select
     addr <= "0000" when 0,
             "0001" when 1,
             "1111" when others;

**Fix**

.. code-block:: vhdl

   with mux_sel select
     addr <= "0000" when 0,
             "0001" when 1,
             "1111" when others;

selected_waveform_assignment_102
################################

|phase_2| |error| |whitespace|

This rule checks for a single space after the **select** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   with mux_sel select     addr <= "0000" when 0,
                               "0001" when 1,
                               "1111" when others;

**Fix**

.. code-block:: vhdl

   with mux_sel select addr <= "0000" when 0,
                               "0001" when 1,
                               "1111" when others;

selected_waveform_assignment_103
################################

|phase_2| |error| |whitespace|

This rule checks for a single space before the **<=**.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   with mux_sel select
     addr<= "0000" when 0,
             "0001" when 1,
             "1111" when others;

**Fix**

.. code-block:: vhdl

   with mux_sel select
     addr <= "0000" when 0,
             "0001" when 1,
             "1111" when others;

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

selected_waveform_assignment_500
################################

|phase_6| |error| |case| |case_keyword|

This rule checks the **with** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   WITH mux_sel select
     addr <= "0000" when 0,
             "0001" when 1,
             "1111" when others;

**Fix**

.. code-block:: vhdl

   with mux_sel select
     addr <= "0000" when 0,
             "0001" when 1,
             "1111" when others;

selected_waveform_assignment_501
################################

|phase_6| |error| |case| |case_keyword|

This rule checks the **with** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   with mux_sel SELECT
     addr <= "0000" when 0,
             "0001" when 1,
             "1111" when others;

**Fix**

.. code-block:: vhdl

   with mux_sel select
     addr <= "0000" when 0,
             "0001" when 1,
             "1111" when others;

