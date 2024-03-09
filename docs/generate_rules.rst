.. include:: includes.rst

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

|configuring_whitespace_rules_link|

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

|configuring_blank_lines_link|

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

|configuring_previous_line_rules_link|

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

|phase_6| |error| |case| |case_label|

This rule checks the generate label has proper case.

|configuring_uppercase_and_lowercase_rules_link|

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

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   end   generate ram_array;

**Fix**

.. code-block:: vhdl

   end generate ram_array;

generate_009
############

|phase_6| |error| |case| |case_keyword|

This rule checks the **end** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   END generate ram_array;

**Fix**

.. code-block:: vhdl

   end generate ram_array;

generate_010
############

|phase_6| |error| |case| |case_keyword|

This rule checks the **generate** keyword has the proper case in the **end generate** line.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   end GENERATE ram_array;

**Fix**

.. code-block:: vhdl

   end generate ram_array;

generate_011
############

|phase_1| |error| |structure| |structure_optional|

This rule checks the **end generate**  label on for, case and if generate statements.

|configuring_optional_items_link|

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

|phase_6| |error| |case| |case_label|

This rule checks the **end generate** label has proper case.

|configuring_uppercase_and_lowercase_rules_link|

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

|configuring_whitespace_rules_link|

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

|configuring_whitespace_rules_link|

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

|phase_1| |error| |structure|

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

|phase_7| |disabled| |error| |unfixable| |naming|

This rule checks for valid prefixes on generate statement labels.
The default prefix is *gen\_*.

|configuring_prefix_and_suffix_rules_link|

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

generate_019
############

|phase_1| |error| |structure|

This rule checks the **end** keyword is on its own line.

**Violation**

.. code-block:: vhdl

   ram_array : for i in 0 to 7 generate
    a <= b; end generate;

**Fix**

.. code-block:: vhdl

   ram_array : for i in 0 to 7 generate
     a <= b;
   end generate;

generate_400
############

|phase_5| |error| |alignment|

This rule checks the identifiers for all declarations are aligned in the generate declarative part in for generate statements.

|configuring_identifier_alignment_rules_link|

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

|phase_5| |error| |alignment|

This rule checks the colons are in the same column for all declarations in the generate declarative part in for generate statements.

|configuring_keyword_alignment_rules_link|

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

|phase_5| |error| |alignment|

This rule checks the identifiers for all declarations are aligned in the generate declarative part in if generate statements.

|configuring_identifier_alignment_rules_link|

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

|phase_5| |error| |alignment|

This rule checks the colons are in the same column for all declarations in the generate declarative part in if generate statements.

|configuring_keyword_alignment_rules_link|

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

|phase_5| |error| |alignment|

This rule checks the identifiers for all declarations are aligned in the generate declarative part in case generate statements.

|configuring_identifier_alignment_rules_link|

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

|phase_5| |error| |alignment|

This rule checks the colons are in the same column for all declarations in the generate declarative part in case generate statements.

|configuring_keyword_alignment_rules_link|

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

generate_500
############

|phase_6| |error| |case| |case_keyword|

This rule checks the **begin** keyword has the proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   for condition generate
     BEGIN

**Fix**

.. code-block:: vhdl

   for condition generate
     begin

generate_501
############

|phase_6| |error| |case| |case_keyword|

This rule checks the **end** keyword has the proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   for condition generate
     begin
     END
   end generate;

**Fix**

.. code-block:: vhdl

   for condition generate
     begin
     end
   end generate;

generate_600
############

|phase_7| |disabled| |error| |unfixable| |naming|

This rule checks for valid suffixes on generate statement labels.
The default suffix is *\_gen*.

|configuring_prefix_and_suffix_rules_link|

**Violation**

.. code-block:: vhdl

   label : case condition generate

**Fix**

.. code-block:: vhdl

   label_gen : case condition generate

generate_601
############

|phase_7| |disabled| |error| |unfixable| |naming|

This rule checks for valid prefixes on generate parameter identifiers.
The default generate prefix is *gv\_*.

|configuring_prefix_and_suffix_rules_link|

**Violation**

.. code-block:: vhdl

  gen_label : for index in t_range generate

**Fix**

.. code-block:: vhdl

  gen_label : for gv_index in t_range generate

generate_602
############

|phase_7| |disabled| |error| |unfixable| |naming|

This rule checks for valid suffixes on generate parameter identifiers.
The default generate suffix is *\_gv*.

|configuring_prefix_and_suffix_rules_link|

**Violation**

.. code-block:: vhdl

  gen_label : for index in t_range generate

**Fix**

.. code-block:: vhdl

  gen_label : for index_gv in t_range generate

