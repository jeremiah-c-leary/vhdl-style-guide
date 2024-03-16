.. include:: includes.rst

Conditional Waveforms Rules
---------------------------

conditional_waveforms_001
#########################

|phase_1| |error| |structure|

This rule checks for code after the **else** keyword.

.. NOTE:: There is a configuration option :code:`allow_single_line` which allows single line concurrent statements.

:code:`allow_single_line` set to :code:`no` (Default)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Violation**

.. code-block:: vhdl

   wr_en <= '0' when overflow = '0' else '1';
   wr_en <= '0' when overflow = '0' else '1' when underflow = '1' else sig_a;

**Fix**

.. code-block:: vhdl

   wr_en <= '0' when overflow = '0' else
            '1';
   wr_en <= '0' when overflow = '0' else
            '1' when underflow = '1' else
            sig_a;

:code:`allow_single_line` set to :code:`yes`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Violation**

.. code-block:: vhdl

   wr_en <= '0' when overflow = '0' else '1';
   wr_en <= '0' when overflow = '0' else '1' when underflow = '1' else sig_a;

**Fix**

.. code-block:: vhdl

   wr_en <= '0' when overflow = '0' else '1';
   wr_en <= '0' when overflow = '0' else
            '1' when underflow = '1' else
            sig_a;

conditional_waveforms_100
#########################

|phase_2| |error| |whitespace|

This rule checks for a single space before the **when** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   wr_en <= '0'when (rd_en = '0') else '1';

**Fix**

.. code-block:: vhdl

   wr_en <= '0' when (rd_en = '0') else '1';

conditional_waveforms_101
#########################

|phase_2| |error| |whitespace|

This rule checks for a single space after the **when** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   wr_en <= '0' when(rd_en = '0') else '1';

**Fix**

.. code-block:: vhdl

   wr_en <= '0' when (rd_en = '0') else '1';

conditional_waveforms_102
#########################

|phase_2| |error| |whitespace|

This rule checks for a single space before the **else** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   wr_en <= '0' when (rd_en = '0')else '1';

**Fix**

.. code-block:: vhdl

   wr_en <= '0' when (rd_en = '0') else '1';

conditional_waveforms_103
#########################

|phase_2| |error| |whitespace|

This rule checks for a single space after the **else** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   wr_en <= '0' when (rd_en = '0') else'1';

**Fix**

.. code-block:: vhdl

   wr_en <= '0' when (rd_en = '0') else '1';

conditional_waveforms_500
#########################

|phase_6| |error| |case| |case_keyword|

This rule checks the **when** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   wr_en <= '0' WHEN (rd_en = '0') else '1';

**Fix**

.. code-block:: vhdl

   wr_en <= '0' when (rd_en = '0') else '1';

conditional_waveforms_501
#########################

|phase_6| |error| |case| |case_keyword|

This rule checks the **else** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   wr_en <= '0' when (rd_en = '0') ELSE '1';

**Fix**

.. code-block:: vhdl

   wr_en <= '0' when (rd_en = '0') else '1';
