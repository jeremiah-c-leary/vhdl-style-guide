.. include:: includes.rst

Interface Incomplete Type Declaration Rules
-------------------------------------------

interface_incomplete_type_declaration_500
#########################################

|phase_6| |error| |case| |case_keyword|

This rule checks the **type** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   generic (
     TYPE generic_data_type

**Fix**

.. code-block:: vhdl

   generic (
     type generic_data_type
