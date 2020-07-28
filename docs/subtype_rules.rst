Subtype Rules
-------------

subtype_001
###########

This rule checks for indentation of the **subtype** keyword.
Proper indentation enhances comprehension.

The indent amount can be controlled by the **indentSize** attribute on the rule.
**indentSize** defaults to 2.

**Violation**

.. code-block:: vhdl

   architecture rtl of fifo is

        subtype read_size is range 0 to 9;
   subtype write_size is range 0 to 9;

   begin

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

     subtype read_size is range 0 to 9;
     subtype write_size is range 0 to 9;

   begin


subtype_002
###########

This rule checks for consistent capitalization of subtype names.

**Violation**

.. code-block:: vhdl

   subtype read_size is range 0 to 9;
   subtype write_size is range 0 to 9;

   signal read  : READ_SIZE;
   signal write : write_size;

   constant read_sz  : read_size := 8;
   constant write_sz : WRITE_size := 1;
   

**Fix**

.. code-block:: vhdl

   subtype read_size is range 0 to 9;
   subtype write_size is range 0 to 9;

   signal read  : read_size;
   signal write : write_size;

   constant read_sz  : read_size := 8;
   constant write_sz : write_size := 1;

subtype_003
###########

This rule was depricated and replaced with rules:  function_015, package_019, procedure_010, architecture_029 and process_037.

subtype_004
###########

This rule checks for valid prefixes in user defined subtype identifiers.
The default new subtype prefix is *st\_*.

Refer to the section `Configuring Prefix and Suffix Rules <configuring_prefix_suffix.html>`_ for information on changing the allowed prefixes.

**Violation**

.. code-block:: vhdl

   subtype my_subtype is range 0 to 9;

**Fix**

.. code-block:: vhdl

   subtype st_my_subtype is range 0 to 9;
