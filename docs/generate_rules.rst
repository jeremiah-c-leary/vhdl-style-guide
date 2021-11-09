.. include:: icons.rst

Generate Rules
--------------

generate_001
############

|phase_4| |error| |indent|

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

|phase_2| |error| |whitespace|

This rule checks for a single space between the label and the colon.

**Violation**

.. code-block:: vhdl

   ram_array: for i in 0 to 7 generate

**Fix**

.. code-block:: vhdl

   ram_array : for i in 0 to 7 generate

generate_003
############

|phase_3| |error| |blank_line|

This rule checks for a blank line below the **end generate** keywords.

Refer to the section `Configuring Blank Lines <configuring.html#configuring-blank-lines>`_ for options regarding comments.

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

|phase_3| |error| |blank_line|

This rule checks for blank lines or comments before the **generate** label.

Refer to `Configuring Previous Line Rules <configuring.html#configuring-previous-line-rules>`_ for options.

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

|phase_6| |error|

This rule checks the generate label has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   RAM_ARRAY: for i in 0 to 7 generate

**Fix**

.. code-block:: vhdl

   ram_array: for i in 0 to 7 generate


generate_006
############

|phase_4| |error| |indent|

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

|phase_4| |error| |indent|

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

|phase_2| |error| |whitespace|

This rule checks for a single space after the **end** keyword.

**Violation**

.. code-block:: vhdl

   end   generate ram_array;

**Fix**

.. code-block:: vhdl

   end generate ram_array;

generate_009
############

|phase_6| |error|

This rule checks the **end** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   END generate ram_array;

**Fix**

.. code-block:: vhdl

   end generate ram_array;

generate_010
############

|phase_6| |error|

This rule checks the **generate** keyword has the proper case in the **end generate** line.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   end GENERATE ram_array;

**Fix**

.. code-block:: vhdl

   end generate ram_array;

generate_011
############

|phase_1| |error|

This rule checks the **end generate** line has a label on for generate statements.

**Violation**

.. code-block:: vhdl

   ram_array : for i in 0 to 127 generate

   end generate;

**Fix**

.. code-block:: vhdl

   ram_array : for i in 0 to 127 generate

   end generate ram_array;

generate_012
############

|phase_6| |error|

This rule checks the **end generate** label has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   end generate RAM_ARRAY;

**Fix**

.. code-block:: vhdl

   end generate ram_array;

generate_013
############

|phase_2| |error| |whitespace|

This rule checks for a single space after the **generate** keyword and the label in the **end generate** keywords.

**Violation**

.. code-block:: vhdl

   end generate    ram_array;

**Fix**

.. code-block:: vhdl

   end generate ram_array;

generate_014
############

|phase_2| |error| |whitespace|

This rule checks for a single space between the colon and the **for** keyword.

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

|phase_1| |error|

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

|phase_4| |error| |indent|

This rule checks the indent of the **when** keyword in generate case statements.

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

|phase_7| |disabled| |error|

This rule checks for valid prefixes on generate statement labels.
The default prefix is *gen\_*.

Refer to the section `Configuring Prefix and Suffix Rules <configuring.html#configuring-prefix-and-suffix-rules>`_ for information on changing the allowed prefixes.

**Violation**

.. code-block:: vhdl

   label : case condition generate

**Fix**

.. code-block:: vhdl

   gen_label : case condition generate

generate_018
############

|phase_4| |error| |indent|

This rule checks the indent of the **end** keyword in the generate statement body.

**Violation**

.. code-block:: vhdl

   ram_array : for i in 0 to 7 generate
   begin
     end;
   end generate;

**Fix**

.. code-block:: vhdl

   ram_array : for i in 0 to 7 generate
   begin
   end;
   end generate;

generate_400
############

|phase_5| |error|

This rule checks the identifiers for all declarations are aligned in the generate declarative part in for generate statements.

Refer to the section `Configuring Identifier Alignment Rules <configuring.html#configuring-identifier-alignment-rules>`_ for information on changing the configurations.

**Violation**

.. code-block:: vhdl

   variable    var1 : natural;
   constant  c_period : time;

**Fix**

.. code-block:: vhdl

   variable var1     : natural;
   constant c_period : time;

generate_401
############

|phase_5| |error|

This rule checks the colons are in the same column for all declarations in the generate declarative part in for generate statements.

Refer to the section `Configuring Keyword Alignment Rules <configuring.html#configuring-keyword-alignment-rules>`_ for information on changing the configurations.

**Violation**

.. code-block:: vhdl

   signal sig1: natural;
   variable var2  : natural;
   constant c_period : time;
   file my_test_input : my_file_type;

**Fix**

.. code-block:: vhdl

   signal sig1        : natural;
   variable var2      : natural;
   constant c_period  : time;
   file my_test_input : my_file_type;

generate_402
############

|phase_5| |error|

This rule checks the identifiers for all declarations are aligned in the generate declarative part in if generate statements.

Refer to the section `Configuring Identifier Alignment Rules <configuring.html#configuring-identifier-alignment-rules>`_ for information on changing the configurations.

**Violation**

.. code-block:: vhdl

   variable    var1 : natural;
   constant  c_period : time;

**Fix**

.. code-block:: vhdl

   variable var1     : natural;
   constant c_period : time;

generate_403
############

|phase_5| |error|

This rule checks the colons are in the same column for all declarations in the generate declarative part in if generate statements.

Refer to the section `Configuring Keyword Alignment Rules <configuring.html#configuring-keyword-alignment-rules>`_ for information on changing the configurations.

**Violation**

.. code-block:: vhdl

   signal sig1: natural;
   variable var2  : natural;
   constant c_period : time;
   file my_test_input : my_file_type;

**Fix**

.. code-block:: vhdl

   signal sig1        : natural;
   variable var2      : natural;
   constant c_period  : time;
   file my_test_input : my_file_type;

generate_404
############

|phase_5| |error|

This rule checks the identifiers for all declarations are aligned in the generate declarative part in case generate statements.

Refer to the section `Configuring Identifier Alignment Rules <configuring.html#configuring-identifier-alignment-rules>`_ for information on changing the configurations.

**Violation**

.. code-block:: vhdl

   variable    var1 : natural;
   constant  c_period : time;

**Fix**

.. code-block:: vhdl

   variable var1     : natural;
   constant c_period : time;

generate_405
############

|phase_5| |error|

This rule checks the colons are in the same column for all declarations in the generate declarative part in case generate statements.

Refer to the section `Configuring Keyword Alignment Rules <configuring.html#configuring-keyword-alignment-rules>`_ for information on changing the configurations.

**Violation**

.. code-block:: vhdl

   signal sig1: natural;
   variable var2  : natural;
   constant c_period : time;
   file my_test_input : my_file_type;

**Fix**

.. code-block:: vhdl

   signal sig1        : natural;
   variable var2      : natural;
   constant c_period  : time;
   file my_test_input : my_file_type;

generate_600
############

|phase_7| |disabled| |error|

This rule checks for valid suffixes on generate statement labels.
The default suffix is *\_gen*.

Refer to the section `Configuring Prefix and Suffix Rules <configuring.html#configuring-prefix-and-suffix-rules>`_ for information on changing the allowed suffixes.

**Violation**

.. code-block:: vhdl

   label : case condition generate

**Fix**

.. code-block:: vhdl

   label_gen : case condition generate


