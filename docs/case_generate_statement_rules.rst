.. include:: includes.rst

Case Generate Statement Rules
-----------------------------

case_generate_statement_500
###########################

|phase_6| |error| |case| |case_keyword|

This rule checks the *case* keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   CASE expression generate

**Fix**

.. code-block:: vhdl

   case expression generate

case_generate_statement_501
###########################

|phase_6| |error| |case| |case_keyword|

This rule checks the *generate* keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   case expression GENERATE

**Fix**

.. code-block:: vhdl

   case expression generate

