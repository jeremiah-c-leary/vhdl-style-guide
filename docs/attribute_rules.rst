Attribute Rules
---------------

attribute_001
#############

This rule checks the indent of **attribute** declarations.

**Violation**

.. code-block:: vhdl

   architecture rtl of fifo is

   attribute ram_init_file : string;
   attribute ram_init_file of ram_block :
         signal is "contents.mif";

   begin

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

     attribute ram_init_file : string;
     attribute ram_init_file of ram_block :
       signal is "contents.mif";

   begin

attribute_002
#############

This rule checks the **attribute** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   architecture rtl of fifo is

     ATTRIBUTE ram_init_file : string;
     Attribute ram_init_file of ram_block :
       signal is "contents.mif";

   begin

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

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

