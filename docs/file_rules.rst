.. include:: includes.rst

File Rules
----------

file_001
########

|phase_4| |error| |indent|

This rule checks the indent of **file** declarations.

**Violation**

.. code-block:: vhdl

   architecture rtl of fifo is

   file defaultImage : load_file_type open read_mode is load_file_name;

   file defaultImage : load_file_type open read_mode
   is load_file_name;

   begin

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

     file defaultImage : load_file_type open read_mode is load_file_name;

     file defaultImage : load_file_type open read_mode
       is load_file_name;

   begin

file_002
########

|phase_6| |error| |case| |case_keyword|

This rule checks the **file** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   architecture rtl of fifo is

     FILE defaultImage : load_file_type open read_mode is load_file_name;

   begin

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

     file defaultImage : load_file_type open read_mode is load_file_name;

   begin

file_003
########

This rule was deprecated and replaced with rules:

* `function_015 <function_rules.html#function-015>`_
* `package_019 <package_rules.html#package-019>`_
* `procedure_010 <procedure_rules.html#procedure-010>`_
* `architecture_029 <architecture_rules.html#architecture-029>`_

file_100
########

|phase_2| |disabled| |error| |whitespace|

This rule checks for a single space before the identifier.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   file           defaultImage : load_file_type open read_mode is load_file_name;

**Fix**

.. code-block:: vhdl

   file defaultImage : load_file_type open read_mode is load_file_name;

file_101
########

|phase_2| |error| |whitespace|

This rule checks for a single space after the identifier.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   file defaultImage        : load_file_type open read_mode is load_file_name;

**Fix**

.. code-block:: vhdl

   file defaultImage : load_file_type open read_mode is load_file_name;

file_500
########

|phase_6| |error| |case| |case_name|

This rule checks the file identifier has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   architecture rtl of fifo is

     file DEFAULTIMAGE : load_file_type open read_mode is load_file_name;

   begin

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

     file defaultImage : load_file_type open read_mode is load_file_name;

   begin
