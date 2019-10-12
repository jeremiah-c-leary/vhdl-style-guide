Attribute Rules
---------------

attribute_001
#############

This rule checks the indent of **attribute** declarations.

**Violation**

.. code-block:: vhdl

   architecture RTL of FIFO is

   attribute ram_init_file : string;
   attribute ram_init_file of ram_block :
         signal is "contents.mif";

   begin

**Fix**

.. code-block:: vhdl

   architecture RTL of FIFO is

     attribute ram_init_file : string;
     attribute ram_init_file of ram_block :
       signal is "contents.mif";

   begin

attribute_002
#############

This rule checks the **attribute** keyword has proper case.

.. NOTE::  The default is lowercase.

**Violation**

.. code-block:: vhdl

   architecture RTL of FIFO is

     ATTRIBUTE ram_init_file : string;
     Attribute ram_init_file of ram_block :
       signal is "contents.mif";

   begin

**Fix**

.. code-block:: vhdl

   architecture RTL of FIFO is

     attribute ram_init_file : string;
     attribute ram_init_file of ram_block :
       signal is "contents.mif";

   begin

attribute_003
#############

This rule checks for a single space after the **attribute** keyword.

**Violation**

.. code-block:: vhdl

   attribute   ram_init_file : string;

**Fix**

.. code-block:: vhdl

   attribute ram_init_file : string;

