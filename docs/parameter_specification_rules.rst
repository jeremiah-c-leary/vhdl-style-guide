.. include:: includes.rst

Parameter Specification Rules
-----------------------------

parameter_specification_500
###########################

|phase_6| |error| |case| |case_name|

This rule checks the parameter identifier has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   for LV_THING in t_thing loop

**Fix**

.. code-block:: vhdl

   for lv_thing in t_thing loop
