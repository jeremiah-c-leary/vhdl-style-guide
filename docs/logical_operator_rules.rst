.. include:: includes.rst

Logical Operator Rules
----------------------

logical_operator_500
####################

|phase_6| |error| |case| |case_keyword|

This rule checks logical operators have proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   a <= b AND c;

**Fix**

.. code-block:: vhdl

   a <= b and c;

