.. include:: includes.rst

Variable Rules
--------------

variable_001
############

|phase_4| |error| |indent|

This rule checks the indent of variable declarations.

**Violation**

.. code-block:: vhdl

   proc : process () is

   variable count : integer;
         variable counter : integer;

   begin

**Fix**

.. code-block:: vhdl

   proc : process () is

     variable count : integer;
     variable counter : integer;

   begin

variable_002
############

|phase_6| |error| |case| |case_keyword|

This rule checks the **variable** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   VARIABLE count : integer;

**Fix**

.. code-block:: vhdl

   variable count : integer;

variable_003
############

This rule was deprecated and replaced with rules:

* `function_015 <function_rules.html#function-015>`_
* `package_019 <package_rules.html#package-019>`_
* `procedure_010 <procedure_rules.html#procedure-010>`_
* `architecture_029 <architecture_rules.html#architecture-029>`_

variable_004
############

|phase_6| |error| |case| |case_name|

This rule checks the variable name has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   variable COUNT : integer;

**Fix**

.. code-block:: vhdl

   variable count : integer;

variable_005
############

|phase_2| |error| |whitespace|

This rule checks there is a single space after the colon.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   variable count   :integer;
   variable counter :     integer;

**Fix**

.. code-block:: vhdl

   variable count   : integer;
   variable counter : integer;

variable_006
############

|phase_2| |error| |whitespace|

This rule checks for at least a single space before the colon.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   variable count: integer;
   variable counter : integer;

**Fix**

.. code-block:: vhdl

   variable count : integer;
   variable counter : integer;

variable_007
############

|phase_1| |error| |unfixable| |structure|

This rule checks for default assignments in variable declarations.

**Violation**

.. code-block:: vhdl

   variable count : integer := 32;

**Fix**

.. code-block:: vhdl

   variable count : integer;

variable_010
############

The function of this rule has been superseded by the following rules:

* type_mark_500
* subtype_002
* type_014

variable_011
############

|phase_6| |error| |case|

This rule checks for consistent capitalization of variable names.

**Violation**

.. code-block:: vhdl

   architecture rtl of entity1 is

     shared variable var1 : std_logic;
     shared variable var2 : std_logic;

   begin

     proc_name : process () is

       variable var3 : std_logic;
       variable var4 : std_logic;

     begin

       Var1 <= '0';

       if (VAR2 = '0') then
         vaR3 <= '1';
       elsif (var2 = '1') then
         VAR4 <= '0';
       end if;

     end process proc_name;

   end architecture rtl;

**Fix**

.. code-block:: vhdl

   proc_name : process () is

     variable var1 : std_logic;
     variable var2 : std_logic;
     variable var3 : std_logic;
     variable var4 : std_logic;

   begin

     var1 <= '0';

     if (var2 = '0') then
       var3 <= '1';
     elsif (var2 = '1') then
       var4 <= '0';
     end if;

   end process proc_name;

variable_012
############

|phase_7| |disabled| |error| |unfixable| |naming|

This rule checks for valid prefixes on variable identifiers.
The default variable prefix is *v_*.

|configuring_prefix_and_suffix_rules_link|

**Violation**

.. code-block:: vhdl

   variable my_var : natural;

**Fix**

.. code-block:: vhdl

   variable v_my_var : natural;

variable_015
############

|phase_1| |error| |structure|

This rule checks for multiple (shared) variable names defined in a single (shared) variable declaration.
By default, this rule will only flag more than two (shared) variable declarations.

|configuring_number_of_variables_in_variable_declaration_link|

**Violation**

.. code-block:: vhdl

   variable var1, var2
     var3, var4,
     var5
     : std_logic;

   shared variable var6, var7, var8 : std_logic;

**Fix**

.. code-block:: vhdl

   variable var1 : std_logic;
   variable var2 : std_logic;
   variable var3 : std_logic;
   variable var4 : std_logic;
   variable var5 : std_logic;

   shared variable var6 : std_logic;
   shared variable var7 : std_logic;
   shared variable var8 : std_logic;

variable_017
############

|phase_1| |error| |structure|

This rule checks the structure of variable constraints.

|configuring_multiline_constraint_rules_link|

.. NOTE:: The indenting of multiline variable constraints is handled by the rule `variable_400 <variable_rules.html#variable-400>`_.

**Violation**

.. code-block:: vhdl

   variable v_element : my_record(element1(7 downto 0), element2(3 downto 0));

**Fix**

.. code-block:: vhdl

   variable v_element : my_record(
       element1(7 downto 0),
       element2(3 downto 0)
     );

variable_018
############

|phase_1| |error| |structure|

This rule checks the **:=** is on the same line as the **variable** keyword.

**Violation**

.. code-block:: vhdl

   variable size : integer
      := 1;
   variable width : integer
      := 32;

**Fix**

.. code-block:: vhdl

   variable size    : integer :=
     1;
   variable width   : integer :=
     32;

variable_100
############

|phase_2| |disabled| |error| |whitespace|

This rule checks for a single space before the identifier.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   variable    size : integer;
   variable width : integer;

**Fix**

.. code-block:: vhdl

   variable size : integer;
   variable width : integer;

variable_101
############

|phase_2| |error| |whitespace|

This rule checks for a single space after the **shared** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   shared    variable size : integer;

**Fix**

.. code-block:: vhdl

   shared variable size : integer;

variable_102
############

|phase_2| |error| |whitespace|

This rule checks for a single space before the assignment.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   variable size : integer      := 32;
   variable width : integer:= 256;

**Fix**

.. code-block:: vhdl

   variable size : integer := 32;
   variable width : integer := 256;

variable_103
############

|phase_2| |error| |whitespace|

This rule checks for a single space after the assignment.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   variable size : integer :=32;
   variable width : integer :=     256;

**Fix**

.. code-block:: vhdl

   variable size : integer := 32;
   variable width : integer := 256;

variable_400
############

|phase_5| |error| |alignment|

This rule checks alignment of multiline constraints in variable declarations.

|configuring_multiline_indent_rules_link|

**Violation**

.. code-block:: vhdl

   variable v_element : my_record(
            element1(7 downto 0),
   element2(3 downto 0)
           );

**Fix**

.. code-block:: vhdl

   variable v_element : my_record(
       element1(7 downto 0),
       element2(3 downto 0)
     );

variable_401
############

|phase_5| |error| |alignment|

This rule checks the alignment of assignment keywords in variable declarations.

|configuring_keyword_alignment_rules_link|

**Violation**

.. code-block:: vhdl

   variable v_default_values : t_address_en := (
     c_address_control => false,
     c_address_data => true,
     others => false
   );

**Fix**

.. code-block:: vhdl

   variable v_default_values : t_address_en := (
     c_address_control => false,
     c_address_data    => true,
     others            => false
   );

variable_402
############

|phase_5| |error| |alignment|

This rule checks the alignment of multiline variable initializations that contain arrays.

|configuring_multiline_indent_rules_link|

.. NOTE:: The structure of multiline array variables is handled by the rule `variable_403 <variable_rules.html#variable-403>`_.

**Violation**

.. code-block:: vhdl

   variable rom : romq_type :=
   (
            0,
        65535,
        32768
     );

**Fix**

.. code-block:: vhdl

   variable rom : romq_type :=
   (
     0,
     65535,
     32768
   );

variable_403
############

|phase_5| |error| |structure|

This rule checks the structure of multiline variable initializations that contain arrays.

|configuring_array_multiline_structure_rules_link|

.. NOTE:: The indenting of multiline array variables is handled by the rule `variable_402 <variable_rules.html#variable-402>`_.

**Violation**

.. code-block:: vhdl

   variable rom : romq_type := (0, 65535, 32768);

**Fix**

.. code-block:: vhdl

   variable rom : romq_type :=
   (
     0,
     65535,
     32768
   );

variable_500
############

|phase_6| |error| |case| |case_keyword|

This rule checks that the keyword **shared** has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   SHARED variable size : integer;

**Fix**

.. code-block:: vhdl

   shared variable size : integer;

variable_600
############

|phase_7| |disabled| |error| |unfixable| |naming|

This rule checks for valid suffix on variable identifiers.
The default variable suffix is *_v*.

|configuring_prefix_and_suffix_rules_link|

**Violation**

.. code-block:: vhdl

   variable my_var : natural;

**Fix**

.. code-block:: vhdl

   variable my_var_v : natural;
