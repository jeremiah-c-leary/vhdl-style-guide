Generate Rules
--------------

generate_001
############

This rule checks the indent of the generate declaration.

**Violation**

.. code-block:: vhdl

   architecture RTL of FIFO is
   begin

   RAM_ARRAY: for i in 0 to 7 generate

         RAM_ARRAY: for i in 0 to 7 generate

**Fix**

.. code-block:: vhdl

   architecture RTL of FIFO is
   begin

     RAM_ARRAY: for i in 0 to 7 generate

     RAM_ARRAY: for i in 0 to 7 generate

generate_002
############

This rule checks for a single space between the label and the :.

**Violation**

.. code-block:: vhdl

   RAM_ARRAY: for i in 0 to 7 generate

**Fix**

.. code-block:: vhdl

   RAM_ARRAY : for i in 0 to 7 generate

generate_003
############

This rule checks for a blank line after the **end generate** keywords.

**Violation**

.. code-block:: vhdl

   end generate RAM_ARRAY;
   wr_en <= '1';

**Fix**

.. code-block:: vhdl

   end generate RAM_ARRAY;

   wr_en <= '1';

generate_004
############

This rule checks for a blank line before the **generate** keyword.

**Violation**

.. code-block:: vhdl

   wr_en <= '1';
   RAM_ARRAY: for i in 0 to 7 generate

**Fix**

.. code-block:: vhdl

   wr_en <= '1';

   RAM_ARRAY: for i in 0 to 7 generate

generate_005
############

This rule checks the generate label is uppercase.

**Violation**

.. code-block:: vhdl

   ram_array: for i in 0 to 7 generate

**Fix**

.. code-block:: vhdl

   RAM_ARRAY: for i in 0 to 7 generate


generate_006
############

This rule checks the indent of the **begin** keyword.

**Violation**

.. code-block:: vhdl

   RAM_ARRAY: for i in 0 to 7 generate
      begin

**Fix**

.. code-block:: vhdl

   RAM_ARRAY: for i in 0 to 7 generate
   begin

generate_007
############

This rule checks the indent of the **end generate** keyword.

**Violation**

.. code-block:: vhdl

   RAM_ARRAY: for i in 0 to 7 generate
   begin
     end generate RAM_ARRAY;

**Fix**

.. code-block:: vhdl

   RAM_ARRAY: for i in 0 to 7 generate
   begin
   end generate RAM_ARRAY;
