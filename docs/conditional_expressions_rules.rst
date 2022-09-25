.. include:: includes.rst

Conditional Expressions Rules
-----------------------------

conditional_expressions_100
###########################

|phase_2| |error| |whitespace|

This rule checks for a single space before the **when** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   wr_en <= '0'when (rd_en = '0') else '1';

**Fix**

.. code-block:: vhdl

   wr_en <= '0' when (rd_en = '0') else '1';

conditional_expressions_101
###########################

|phase_2| |error| |whitespace|

This rule checks for a single space after the **when** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   wr_en <= '0' when(rd_en = '0') else '1';

**Fix**

.. code-block:: vhdl

   wr_en <= '0' when (rd_en = '0') else '1';

conditional_expressions_102
###########################

|phase_2| |error| |whitespace|

This rule checks for a single space before the **else** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   wr_en <= '0' when (rd_en = '0')else '1';

**Fix**

.. code-block:: vhdl

   wr_en <= '0' when (rd_en = '0') else '1';

conditional_expressions_103
###########################

|phase_2| |error| |whitespace|

This rule checks for a single space after the **else** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   wr_en <= '0' when (rd_en = '0') else'1';

**Fix**

.. code-block:: vhdl

   wr_en <= '0' when (rd_en = '0') else '1';

conditional_expressions_500
###########################

|phase_6| |error| |case| |case_keyword|

This rule checks the **when** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   wr_en <= '0' WHEN (rd_en = '0') else '1';

**Fix**

.. code-block:: vhdl

   wr_en <= '0' when (rd_en = '0') else '1';

conditional_expressions_501
###########################

|phase_6| |error| |case| |case_keyword|

This rule checks the **else** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   wr_en <= '0' when (rd_en = '0') ELSE '1';

**Fix**

.. code-block:: vhdl

   wr_en <= '0' when (rd_en = '0') else '1';

