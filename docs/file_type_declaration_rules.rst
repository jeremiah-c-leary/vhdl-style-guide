.. include:: includes.rst

File Type Declaration Rules
---------------------------

file_type_declaration_500
#########################

|phase_6| |error| |case| |case_keyword|

This rule checks the **file** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   type integer_file is FILE of integer;


**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

   type integer_file is file of integer;

   begin

file_type_declaration_501
#########################

|phase_6| |error| |case| |case_keyword|

This rule checks the **of** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   type integer_file is file OF integer;


**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

   type integer_file is file of integer;

   begin
