Generate Rules
--------------

generate_001
############

This rule checks the indent of the generate declaration.

**Violation**

.. code-block:: vhdl

   architecture rtl of fifo is
   begin

   ram_array : for i in 0 to 7 generate

         ram_array : for i in 0 to 7 generate

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is
   begin

     ram_array : for i in 0 to 7 generate

     ram_array : for i in 0 to 7 generate

generate_002
############

This rule checks for a single space between the label and the :.

**Violation**

.. code-block:: vhdl

   ram_array: for i in 0 to 7 generate

**Fix**

.. code-block:: vhdl

   ram_array : for i in 0 to 7 generate

generate_003
############

This rule checks for a blank line after the **end generate** keywords.

**Violation**

.. code-block:: vhdl

   end generate ram_array;
   wr_en <= '1';

**Fix**

.. code-block:: vhdl

   end generate ram_array;

   wr_en <= '1';

generate_004
############

This rule checks for a blank line before the **generate** keyword.

**Violation**

.. code-block:: vhdl

   wr_en <= '1';
   ram_array : for i in 0 to 7 generate

**Fix**

.. code-block:: vhdl

   wr_en <= '1';

   ram_array : for i in 0 to 7 generate

generate_005
############

This rule checks the generate label has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   RAM_ARRAY: for i in 0 to 7 generate

**Fix**

.. code-block:: vhdl

   ram_array: for i in 0 to 7 generate


generate_006
############

This rule checks the indent of the **begin** keyword.

**Violation**

.. code-block:: vhdl

   ram_array : for i in 0 to 7 generate
      begin

**Fix**

.. code-block:: vhdl

   ram_array : for i in 0 to 7 generate
   begin

generate_007
############

This rule checks the indent of the **end generate** keyword.

**Violation**

.. code-block:: vhdl

   ram_array : for i in 0 to 7 generate
   begin
     end generate ram_array;

**Fix**

.. code-block:: vhdl

   ram_array : for i in 0 to 7 generate
   begin
   end generate ram_array;

generate_008
############
 
This rule checks for a single space after the **end** keyword.

**Violation**

.. code-block:: vhdl

   end   generate ram_array;

**Fix**

.. code-block:: vhdl

   end generate ram_array;

generate_009
############
 
This rule checks the **end** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   END generate ram_array;

**Fix**

.. code-block:: vhdl

   end generate ram_array;

generate_010
############
 
This rule checks the **generate** keyword has the proper case in the **end generate** line.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   end GENERATE ram_array;

**Fix**

.. code-block:: vhdl

   end generate ram_array;

generate_011
############
 
This rule checks the **end generate** line has a label.

**Violation**

.. code-block:: vhdl

   end generate;

**Fix**

.. code-block:: vhdl

   end generate ram_array;

generate_012
############
 
This rule checks the **end generate** label has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   end generate RAM_ARRAY;

**Fix**

.. code-block:: vhdl

   end generate ram_array;

generate_013
############
 
This rule checks for a single space after the **generate** keyword and the label in the **end generate** keywords.

**Violation**

.. code-block:: vhdl

   end generate    ram_array;

**Fix**

.. code-block:: vhdl

   end generate ram_array;

generate_014
############

This rule checks for a single space between the : and the **for** keyword.

**Violation**

.. code-block:: vhdl

   ram_array :for i in 0 to 7 generate
   ram_array :   for i in 0 to 7 generate

**Fix**

.. code-block:: vhdl

   ram_array : for i in 0 to 7 generate
   ram_array : for i in 0 to 7 generate

generate_015
############

This rule checks the generate label and the **generate** keyword are on the same line.
Keeping the label and generate on the same line reduces excessive indenting.

**Violation**

.. code-block:: vhdl

   ram_array :
     for i in 0 to 7 generate

**Fix**

.. code-block:: vhdl

   ram_array : for i in 0 to 7 generate

generate_016
############

This rule checks the alignment of the **when** keyword in generic case statements.

**Violation**

.. code-block:: vhdl

   GEN_LABEL : case condition generate
     when 0 =>
       when 1 =>
   when 2 =>

**Fix**
.. code-block:: vhdl

   GEN_LABEL : case condition generate
     when 0 =>
     when 1 =>
     when 2 =>

generate_017
############

This rule checks for valid prefixes on generic statement labels.
The default prefix is *gen\_*.

Refer to the section `Configuring Prefix and Suffix Rules <configuring_prefix_suffix.html>`_ for information on changing the allowed prefixes.

**Violation**

.. code-block:: vhdl

   label : case condition generate

**Fix**

.. code-block:: vhdl

   gen_label : case condition generate
