.. include:: includes.rst

Range Constraint Rules
----------------------

range_constraint_500
####################

|phase_6| |error| |case| |case_keyword|

This rule checks the **range** keyword in range constraints have the proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   subtype t_range is natural RANGE 1 to 0;

**Fix**

.. code-block:: vhdl

   subtype t_range is natural range 1 to 0;
