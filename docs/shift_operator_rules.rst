.. include:: includes.rst

Shift Operator Rules
--------------------

shift_operator_500
##################

|phase_6| |error| |case| |case_keyword|

This rule checks shift operators have proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   a <= b SLL c;

**Fix**

.. code-block:: vhdl

   a <= b sll c;
