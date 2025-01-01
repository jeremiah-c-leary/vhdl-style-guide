.. include:: includes.rst

External Variable Name Rules
----------------------------

external_variable_name_100
##########################

|phase_2| |error| |whitespace|

This rule checks for a single space after the double less than.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   <<     variable dut.fifo.wr_en : std_logic >>
   <<variable dut.fifo.wr_en : std_logic >>

**Fix**

.. code-block:: vhdl

   << variable dut.fifo.wr_en : std_logic >>
   << variable dut.fifo.wr_en : std_logic >>

external_variable_name_101
##########################

|phase_2| |error| |whitespace|

This rule checks for a single space after the **variable** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   << variable    dut.fifo.wr_en : std_logic >>

**Fix**

.. code-block:: vhdl

   << variable dut.fifo.wr_en : std_logic >>

external_variable_name_102
##########################

|phase_2| |error| |whitespace|

This rule checks for a single space before the colon.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   << variable dut.fifo.wr_en: std_logic >>
   << variable dut.fifo.wr_en        : std_logic >>

**Fix**

.. code-block:: vhdl

   << variable dut.fifo.wr_en : std_logic >>
   << variable dut.fifo.wr_en : std_logic >>

external_variable_name_103
##########################

|phase_2| |error| |whitespace|

This rule checks for a single space after the colon.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   << variable dut.fifo.wr_en :std_logic >>
   << variable dut.fifo.wr_en :     std_logic >>

**Fix**

.. code-block:: vhdl

   << variable dut.fifo.wr_en : std_logic >>
   << variable dut.fifo.wr_en : std_logic >>

external_variable_name_104
##########################

|phase_2| |error| |whitespace|

This rule checks for a single space before the double greater than.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   << variable dut.fifo.wr_en : std_logic>>
   << variable dut.fifo.wr_en : std_logic     >>

**Fix**

.. code-block:: vhdl

   << variable dut.fifo.wr_en : std_logic >>
   << variable dut.fifo.wr_en : std_logic >>

external_variable_name_500
##########################

|phase_6| |error| |case| |case_keyword|

This rule checks the **variable** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   << VARIABLE dut.fifo.wr_en : std_logic >>

**Fix**

.. code-block:: vhdl

   << variable dut.fifo.wr_en : std_logic >>
