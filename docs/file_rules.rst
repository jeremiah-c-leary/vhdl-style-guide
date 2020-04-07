File Rules
----------

file_001
########

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

This rule checks the **file** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

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

This rule checks for spaces after the **file** keyword.

**Violation**

.. code-block:: vhdl

     file   defaultImage : load_file_type open read_mode is load_file_name;

**Fix**

.. code-block:: vhdl

     file defaultImage : load_file_type open read_mode is load_file_name;

.. NOTE:: The number of spaces after the **file** keyword is configurable.
   Use the following YAML file example to change the default number of spaces.

   .. code-block:: yaml

   rule:
     file_003:
         spaces: 3 

