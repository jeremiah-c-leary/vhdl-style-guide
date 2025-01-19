.. include:: includes.rst

File Open Information Rules
---------------------------

file_open_information_500
#########################

|phase_6| |error| |case| |case_keyword|

This rule checks the **open** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   architecture rtl of fifo is

     file defaultImage : load_file_type OPEN read_mode is load_file_name;

   begin

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

     file defaultImage : load_file_type open read_mode is load_file_name;

   begin

file_open_information_501
#########################

|phase_6| |error| |case| |case_keyword|

This rule checks the file open kind expression has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   architecture rtl of fifo is

     FILE defaultImage : load_file_type open READ_MODE is load_file_name;

   begin

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

     file defaultImage : load_file_type open read_mode is load_file_name;

   begin

file_open_information_502
#########################

|phase_6| |error| |case| |case_keyword|

This rule checks the **is** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   architecture rtl of fifo is

     file defaultimage : load_file_type open read_mode IS load_file_name;

   begin

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

     file defaultImage : load_file_type open read_mode is load_file_name;

   begin
