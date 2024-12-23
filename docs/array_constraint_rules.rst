.. include:: includes.rst

Array Constraint Rules
----------------------

array_constraint_500
####################

|phase_6| |error| |case| |case_keyword|

This rule checks the **open** keyword in array constraints has the proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   subtype t_my_array is t_array(OPEN)(t_range);


**Fix**

.. code-block:: vhdl

   subtype t_my_array is t_array(open)(t_range);
