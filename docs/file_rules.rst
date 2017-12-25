File Rules
----------

file_001
########

This rule checks the indent of **file** declarations.

**Violation**

.. code-block:: vhdl

   architecture RTL of FIFO is

   file defaultImage : load_file_type open read_mode is load_file_name;

   file defaultImage : load_file_type open read_mode
   is load_file_name;

   begin

**Fix**

.. code-block:: vhdl

   architecture RTL of FIFO is

     file defaultImage : load_file_type open read_mode is load_file_name;

     file defaultImage : load_file_type open read_mode
       is load_file_name;

   begin

file_002
########

This rule checks the **file** keyword is lowercase.

**Violation**

.. code-block:: vhdl

   architecture RTL of FIFO is

     FILE defaultImage : load_file_type open read_mode is load_file_name;

   begin

**Fix**

.. code-block:: vhdl

   architecture RTL of FIFO is

     file defaultImage : load_file_type open read_mode is load_file_name;

   begin

file_003
########

This rule checks for a single space after the **attribute** keyword.

**Violation**

.. code-block:: vhdl

     file   defaultImage : load_file_type open read_mode is load_file_name;

**Fix**

.. code-block:: vhdl

     file defaultImage : load_file_type open read_mode is load_file_name;

