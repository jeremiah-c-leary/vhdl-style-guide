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

generate_008
############
 
This rule checks for a single space after the **end** keyword.

**Violation**

.. code-block:: vhdl

   end   generate RAM_ARRAY;

**Fix**

.. code-block:: vhdl

   end generate RAM_ARRAY;

generate_009
############
 
This rule checks the **end** keyword is lowercase.

**Violation**

.. code-block:: vhdl

   END generate RAM_ARRAY;

**Fix**

.. code-block:: vhdl

   end generate RAM_ARRAY;

generate_010
############
 
This rule checks the **generate** keyword is lowercase in the **end generate** line.

**Violation**

.. code-block:: vhdl

   end GENERATE RAM_ARRAY;

**Fix**

.. code-block:: vhdl

   end generate RAM_ARRAY;

generate_011
############
 
This rule checks the **end generate** line has a label.

**Violation**

.. code-block:: vhdl

   end generate;

**Fix**

.. code-block:: vhdl

   end generate RAM_ARRAY;

generate_012
############
 
This rule checks the **end generate** label is uppercase.

**Violation**

.. code-block:: vhdl

   end generate ram_array;

**Fix**

.. code-block:: vhdl

   end generate RAM_ARRAY;

generate_013
############
 
This rule checks for a single space after the **generate** keyword and the label in the **end generate** keywords.

**Violation**

.. code-block:: vhdl

   end generate    RAM_ARRAY;

**Fix**

.. code-block:: vhdl

   end generate RAM_ARRAY;
