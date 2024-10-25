.. include:: includes.rst

Aggregate Rules
---------------

aggregate_500
#############

|phase_6| |error| |case| |case_keyword|

This rule checks the *others* keyword has proper case in aggregates.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   signal counter : t_counter := (OTHERS => '1');

**Fix**

.. code-block:: vhdl

   signal counter : t_counter := (others => '1');
