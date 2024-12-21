.. include:: includes.rst

Index Subtype Definition Rules
------------------------------

index_subtype_definition_500
############################

|phase_6| |error| |case| |case_keyword|

This rule checks the **range** keyword in index subtype definitions has the proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   type t_unsigned_array is array(natural RANGE <>) of unsigned;

**Fix**

.. code-block:: vhdl

   type t_unsigned_array is array(natural range <>) of unsigned;
