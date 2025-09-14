.. include:: includes.rst

Constant Rules
--------------

constant_001
############

|phase_4| |error| |indent|

This rule checks the indent of a constant declaration.

**Violation**

.. code-block:: vhdl

   architecture RTL of FIFO is

   constant size : integer := 1;
       constant width : integer := 32;

**Fix**

.. code-block:: vhdl

   architecture RTL of FIFO is

     constant size : integer := 1;
     constant width : integer := 32;

constant_002
############

|phase_6| |error| |case| |case_keyword|

This rule checks the **constant** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   CONSTANT size : integer := 1;

**Fix**

.. code-block:: vhdl

   constant size : integer := 1;

constant_003
############

This rule was deprecated and replaced with rules:  function_015, package_019, procedure_010, architecture_029 and process_037.

constant_004
############

|phase_6| |error| |case| |case_name|

This rule checks the constant identifier has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   constant SIZE : integer := 1;

**Fix**

.. code-block:: vhdl

   constant size : integer := 1;

constant_005
############

|phase_2| |error| |whitespace|

This rule checks for a single space after the colon.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   constant size  :integer := 1;
   constant width :     integer := 32;

**Fix**

.. code-block:: vhdl

   constant size  : integer := 1;
   constant width : integer := 32;

constant_006
############

|phase_2| |error| |whitespace|

This rule checks for at least a single space before the colon.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   constant size: integer := 1;
   constant width     : integer := 32;

**Fix**

.. code-block:: vhdl

   constant size : integer := 1;
   constant width     : integer := 32;

constant_007
############

|phase_1| |error| |structure|

This rule checks the **:=** is on the same line as the **constant** keyword.

**Violation**

.. code-block:: vhdl

   constant size : integer
      := 1;
   constant width : integer
      := 32;

**Fix**

.. code-block:: vhdl

   constant size    : integer :=
     1;
   constant width   : integer :=
     32;

constant_010
############

|phase_2| |error| |whitespace|

This rule checks for a single space before the := keyword in constant declarations.
Having a space makes it clearer where the assignment occurs on the line.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   constant size : integer:= 1;
   constant width : integer   := 10;

**Fix**

.. code-block:: vhdl

   constant size : integer := 1;
   constant width : integer := 10;

constant_011
############

The function of this rule has been superseded by the following rules:

* type_mark_500
* subtype_002
* type_014

constant_012
############

|phase_5| |error| |alignment|

This rule checks the alignment of multiline constants that contain arrays.

|configuring_multiline_indent_rules_link|

.. NOTE:: The structure of multiline array constants is handled by the rule `constant_016 <constant_rules.html#constant-016>`_.

**Violation**

.. code-block:: vhdl

   constant rom : romq_type :=
   (
            0,
        65535,
        32768
     );

**Fix**

.. code-block:: vhdl

   constant rom : romq_type :=
   (
     0,
     65535,
     32768
   );

constant_013
############

|phase_6| |error| |case|

This rule checks for consistent capitalization of constant names.

**Violation**

.. code-block:: vhdl

   architecture RTL of ENTITY1 is

     constant c_size  : integer := 5;
     constant c_ones  : std_logic_vector(c_size - 1 downto 0) := (others => '1');
     constant c_zeros : std_logic_vector(c_size - 1 downto 0) := (others => '0');

     signal data : std_logic_vector(c_size - 1 downto 0);

   begin

     data <= C_ONES;

     PROC_NAME : process () is
     begin

       data <= C_ones;

       if (sig2 = '0') then
         data <= c_Zeros;
       end if;

     end process PROC_NAME;

   end architecture RTL;

**Fix**

.. code-block:: vhdl

   architecture RTL of ENTITY1 is

     constant c_size  : integer := 5;
     constant c_ones  : std_logic_vector(c_size - 1 downto 0) := (others => '1');
     constant c_zeros : std_logic_vector(c_size - 1 downto 0) := (others => '0');

     signal data : std_logic_vector(c_size - 1 downto 0);

   begin

     data <= c_ones;

     PROC_NAME : process () is
     begin

       data <= c_ones;

       if (sig2 = '0') then
         data <= c_zeros;
       end if;

     end process PROC_NAME;

   end architecture RTL;

constant_014
############

|phase_5| |error| |alignment|

This rule checks the indent of multiline constants that do not contain arrays.

|configuring_multiline_indent_rules_link|

**Violation**

.. code-block:: vhdl

   constant width : integer := a + b +
     c + d;

**Fix**

.. code-block:: vhdl

   constant width : integer := a + b +
                               c + d;

constant_015
############

|phase_7| |disabled| |error| |unfixable| |naming|

This rule checks for valid prefixes on constant identifiers.
The default constant prefix is *c_*.

|configuring_prefix_and_suffix_rules_link|

**Violation**

.. code-block:: vhdl

   constant my_const : integer;

**Fix**

.. code-block:: vhdl

   constant c_my_const : integer;

constant_016
############

|phase_5| |error| |structure|

This rule checks the structure of multiline constants that contain arrays.

|configuring_array_multiline_structure_rules_link|

.. NOTE:: The indenting of multiline array constants is handled by the rule `constant_012 <constant_rules.html#constant-012>`_.

**Violation**

.. code-block:: vhdl

   constant rom : romq_type := (0, 65535, 32768);

**Fix**

.. code-block:: vhdl

   constant rom : romq_type :=
   (
     0,
     65535,
     32768
   );

constant_017
############

|phase_1| |error| |structure|

This rule checks the structure of constant constraints.

|configuring_multiline_constraint_rules_link|

**Violation**

.. code-block:: vhdl

   constant con_a : my_record(element1(7 downto 0), element2(3 downto 0));

**Fix**

.. code-block:: vhdl

   constant con_a : my_record(
       element1(7 downto 0),
       element2(3 downto 0)
     );

constant_100
############

|phase_2| |error| |whitespace|

This rule checks for a single space after the := assignment in constant declarations.
Having a space makes it clearer where the assignment occurs on the line.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   constant size : integer :=1;
   constant width : t_type :=(

**Fix**

.. code-block:: vhdl

   constant size : integer := 1;
   constant width : t_type := (

constant_101
############

|phase_2| |disabled| |error| |whitespace|

This rule checks for a single space before the identifier.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   constant    size : integer := 1;
   constant width : integer := 32;

**Fix**

.. code-block:: vhdl

   constant size : integer := 1;
   constant width : integer := 32;

constant_200
############

|phase_3| |disabled| |error| |blank_line|

This rule checks for a blank line below a constant declaration unless there is another constant definition.

|configuring_blank_lines_link|

**Violation**

.. code-block:: vhdl

   constant width  : integer := 32;
   signal   height : integer := 4;

   constant width  : integer := 32;
   constant height : integer := 4;

**Fix**

.. code-block:: vhdl

   constant width  : integer := 32;
   signal   height : integer := 4;

   constant width  : integer := 32;
   constant height : integer := 4;

constant_400
############

|phase_5| |error| |alignment|

This rule checks the alignment of assignment keywords in constant declarations.

|configuring_keyword_alignment_rules_link|

**Violation**

.. code-block:: vhdl

   constant c_default_values : t_address_en := (
     c_address_control => false,
     c_address_data => true,
     others => false
   );

**Fix**

.. code-block:: vhdl

   constant c_default_values : t_address_en := (
     c_address_control => false,
     c_address_data    => true,
     others            => false
   );

constant_600
############

|phase_7| |disabled| |error| |unfixable| |naming|

This rule checks for valid suffixes on constant identifiers.
The default constant suffix is *_c*.

|configuring_prefix_and_suffix_rules_link|

**Violation**

.. code-block:: vhdl

   constant my_const : integer;

**Fix**

.. code-block:: vhdl

   constant my_const_c : integer;
