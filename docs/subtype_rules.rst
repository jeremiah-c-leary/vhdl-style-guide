Subtype Rules
-------------

subtype_001
###########

This rule checks for indentation of the subtype keyword.
Proper indentation enhances comprehension.

The indent amount can be controlled by the **indentSize** attribute on the rule.
**indentSize** defaults to 2.

**Violation**

.. code-block:: vhdl

   architecture RTL of FIFO is

        subtype read_size is range 0 to 9;
   subtype write_size is range 0 to 9;

   begin

**Fix**

.. code-block:: vhdl

   architecture RTL of FIFO is

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
   
