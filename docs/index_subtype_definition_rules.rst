.. include:: includes.rst

Index Subtype Definition Rules
------------------------------

index_subtype_definition_100
############################

|phase_2| |error| |whitespace|

This rule checks for a single space before the **range** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   type my_array is array (natural     range <>) of integer;

**Fix**

.. code-block:: vhdl

   type my_array is array (natural range <>) of integer;

index_subtype_definition_101
############################

|phase_2| |error| |whitespace|

This rule checks for a single space after the **range** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   type my_array is array (natural range     <>) of integer;

**Fix**

.. code-block:: vhdl

   type my_array is array (natural range <>) of integer;

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
