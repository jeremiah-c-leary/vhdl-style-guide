.. include:: includes.rst

If Generate Statement Rules
---------------------------

generate_500
############

|phase_6| |error| |case| |case_keyword|

This rule checks the *if* keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   IF condition generate

**Fix**

.. code-block:: vhdl

   if condition generate

