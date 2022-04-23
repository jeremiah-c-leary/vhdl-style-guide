.. include:: includes.rst

Case Generate Alternative Rules
-------------------------------

case_generate_alternative_300
#############################

|phase_4| |error| |alignment|

This rule aligns consecutive comment only lines above a **when** keyword in a case generate statement with the **when** keyword.

**Violation**

.. code-block:: vhdl

       -- comment 1
 -- comment 2
    -- comment 3
   when wr_en =>
     rd_en <= '0';

**Fix**

.. code-block:: vhdl

   -- comment 1
   -- comment 2
   -- comment 3
   when wr_en =>
     rd_en <= '0';

case_generate_alternative_500
#############################

|phase_6| |error| |case| |case_keyword|

This rule checks the *when* keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   WHEN choices =>

**Fix**

.. code-block:: vhdl

   when choices =>

