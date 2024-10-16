.. include:: includes.rst

Function Rules
--------------

function_001
############

|phase_4| |error| |indent|

This rule checks the indentation of the **function** keyword.

**Violation**

.. code-block:: vhdl

   architecture RTL of FIFO is

       function overflow (a: integer) return integer is


   function underflow (a: integer) return integer is

   begin

**Fix**

.. code-block:: vhdl

   architecture RTL of FIFO is

     function overflow (a: integer) return integer is

     function underflow (a: integer) return integer is

   begin

function_002
############

This rule has been merged into `function_100 <function_rules.html#function-100>`_.

function_003
############

This rule has been merged into `function_100 <function_rules.html#function-100>`_.

function_004
############

|phase_6| |error| |case| |case_keyword|

This rule checks the **begin** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   function overflow (a: integer) return integer is
   BEGIN

**Fix**

.. code-block:: vhdl

   function overflow (a: integer) return integer is
   begin

function_005
############

|phase_6| |error| |case| |case_keyword|

This rule checks the **function** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   FUNCTION overflow (a: integer) return integer is

**Fix**

.. code-block:: vhdl

   function overflow (a: integer) return integer is

function_006
############

|phase_3| |error| |blank_line|

This rule checks for blank lines or comments above the **function** keyword.

|configuring_previous_line_rules_link|

**Violation**

.. code-block:: vhdl

   architecture RTL of FIFO is
     function overflow (a: integer) return integer is


**Fix**

.. code-block:: vhdl

   architecture RTL of FIFO is

     function overflow (a: integer) return integer is

function_007
############

This rule has been moved to rule `subprogram_body_205 <subprogram_body_rules.html#subprogram-body-205>`_.

function_008
############

|phase_4| |error| |indent|

This rule checks the indent of function parameters on multiple lines.

**Violation**

.. code-block:: vhdl

   function func_1 (a : integer; b : integer;
               c : unsigned(3 downto 0);
       d : std_logic_vector(7 downto 0);
          e : std_logic) return integer is
   begin

   end;

**Fix**

.. code-block:: vhdl

   function func_1 (a : integer; b : integer;
     c : unsigned(3 downto 0);
     d : std_logic_vector(7 downto 0);
     e : std_logic) return integer is
   begin

   end;

function_009
############

The function of this rule has been superseded and is handled by rule function_019.

function_010
############

|phase_6| |error| |case|

This rule checks for consistent capitalization of function names.

**Violation**

.. code-block:: vhdl

   architecture rtl of fifo is

     function func_1 ()

   begin

     OUT1 <= Func_1;

     PROC1 : process () is
     begin

        sig1 <= FUNC_1;

     end process;

   end architecture rtl;

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

     function func_1 ()

   begin

     OUT1 <= func_1;

     PROC1 : process () is
     begin

        sig1 <= func_1;

     end process;

   end architecture rtl;

function_012
############

|phase_5| |error| |alignment|

This rule checks the colons are in the same column for all declarations in the function declarative part.

|configuring_keyword_alignment_rules_link|

**Violation**

.. code-block:: vhdl

   variable var1 : natural;
   variable var2  : natural;
   constant c_period : time;

**Fix**

.. code-block:: vhdl

   variable var1     : natural;
   variable var2     : natural;
   constant c_period : time;

function_013
############

|phase_6| |error| |case| |case_keyword|

This rule checks the **end** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   END;

   End function foo;

**Fix**

.. code-block:: vhdl

   end;

   end function foo;

function_014
############

|phase_6| |error| |case| |case_keyword|

This rule checks the **function** keyword in the **end function** has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   end FUNCTION;

   end Function foo;

**Fix**

.. code-block:: vhdl

   end function;

   end function foo;

function_015
############

|phase_5| |error| |alignment|

This rule checks the identifiers for all declarations are aligned in the function declarative part.

|configuring_identifier_alignment_rules_link|

**Violation**

.. code-block:: vhdl

   variable var1 : natural;
   signal sig1 : natural;
   constant c_period : time;

**Fix**

.. code-block:: vhdl

   variable var1     : natural;
   signal   sig1     : natural;
   constant c_period : time;

function_016
############

|phase_4| |error| |indent|

This rule checks the indent of return statements in function bodies.

**Violation**

.. code-block:: vhdl

   function func1 return integer is
   begin
        return 99;
   return 99;
   end func1;

**Fix**

.. code-block:: vhdl

   function func1 return integer is
   begin
     return 99;
     return 99;
   end func1;

function_017
############

|phase_6| |error| |case| |case_name|

This rule checks the function designator has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   function OVERflow (a: integer) return integer is

**Fix**

.. code-block:: vhdl

   function overflow (a: integer) return integer is

function_018
############

|phase_1| |error| |structure| |structure_optional|

This rule checks the function keyword exist in the closing of the function specification.

|configuring_optional_items_link|

**Violation**

.. code-block:: vhdl

   function func return integer is

   end func;

**Fix**

.. code-block:: vhdl

   function func return integer is

   end function func;

function_019
############

|phase_1| |error| |structure|

This rule checks the structure of function specifications.

|configuring_subprogram_specification_statement_rules_link|

**Violation**

.. code-block:: vhdl

    function average_samples (num_samples : in integer; sample : out std_logic) return integer;

**Fix**

.. code-block:: vhdl

    function average_samples (
      num_samples : in integer;
      sample      : out std_logic
    ) return integer;

function_020
############

|phase_1| |error| |structure| |structure_optional|

This rule checks the function designator exists in the closing of the function specification.

|configuring_optional_items_link|

**Violation**

.. code-block:: vhdl

   function func return integer is

   end function;

**Fix**

.. code-block:: vhdl

   function func return integer is

   end function func;

function_100
############

|phase_2| |error| |whitespace|

This rule checks for a single space between the following function elements:  **function** keyword, function designator, open parenthesis, close parenthesis, **return** keyword, return type and **is** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   function     overflow    (a: integer)     return     integer    is

**Fix**

.. code-block:: vhdl

   function overflow (a: integer) return integer is

function_101
############

|phase_2| |error| |whitespace|

This rule checks for a single space between the **end** and **function** keywords and function designator.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   end   function   overflow;
   end   function;
   end   overflow;

**Fix**

.. code-block:: vhdl

   end function overflow;
   end function;
   end overflow;

function_201
############

This rule has been moved to rule `subprogram_body_201 <subprogram_body_rules.html#subprogram-body-201>`_.

function_202
############

This rule has been moved to rule `subprogram_body_202 <subprogram_body_rules.html#subprogram-body-202>`_.

function_203
############

This rule has been moved to rule `subprogram_body_203 <subprogram_body_rules.html#subprogram-body-203>`_.

function_204
############

This rule has been moved to rule `subprogram_body_204 <subprogram_body_rules.html#subprogram-body-204>`_.

function_300
############

|phase_4| |error| |indent|

This rule checks the indent of the closing parenthesis if it is on its own line.

**Violation**

.. code-block:: vhdl

   function func_1 (a : integer; b : integer;
     c : unsigned(3 downto 0);
     d : std_logic_vector(7 downto 0);
     e : std_logic
     ) return integer is


**Fix**

.. code-block:: vhdl

   function func_1 (a : integer; b : integer;
     c : unsigned(3 downto 0);
     d : std_logic_vector(7 downto 0);
     e : std_logic
   ) return integer is

function_501
############

|phase_6| |error| |case| |case_keyword|

This rule checks the **return** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   function overflow (a: integer) RETURN integer is

**Fix**

.. code-block:: vhdl

   function overflow (a: integer) return integer is

function_502
############

|phase_6| |error| |case| |case_keyword|

This rule checks the **is** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   function overflow (a: integer) return integer IS

**Fix**

.. code-block:: vhdl

   function overflow (a: integer) return integer is

function_506
############

|phase_6| |error| |case| |case_name|

This rule checks the function designator has proper case on the end function declaration.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   end function OVERFLOW;

**Fix**

.. code-block:: vhdl

   end function overflow;

function_507
############

|phase_6| |error| |case| |case_name|

This rule checks that the parameter names have proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

  function my_func (
    PARAM1 : in integer;
    PaRaM2 : out integer
  ) return integer;

**Fix**

.. code-block:: vhdl

  function my_func (
    param1 : in integer;
    param2 : out integer
  ) return integer;

function_508
############

|phase_6| |error| |case| |case_name|

This rule checks for consistent capitalization of parameter names within the subprogram body.

**Violation**

.. code-block:: vhdl

  function my_func (
    param1 : in integer;
    param2 : out integer
  ) return integer is
  begin

    SIG <= PARAM1 + PARAM2;

  end function my_func;

**Fix**

.. code-block:: vhdl

  function my_func (
    param1 : in integer;
    param2 : out integer
  ) return integer is
  begin

    SIG <= param1 + param2;

  end function my_func;

   end architecture rtl;

function_600
############

|phase_7| |disabled| |error| |unfixable| |naming|

This rule checks for valid prefixes on function designators.
Default signal prefix is *f_*.

|configuring_prefix_and_suffix_rules_link|

**Violation**

.. code-block:: vhdl

   function read_data

**Fix**

.. code-block:: vhdl

   function f_read_data

function_601
############

|phase_7| |disabled| |error| |unfixable| |naming|

This rule checks for valid suffixes on function designators.
Default signal suffix is *_f*.

|configuring_prefix_and_suffix_rules_link|

**Violation**

.. code-block:: vhdl

   function read_data

**Fix**

.. code-block:: vhdl

   function read_data_f
