.. include:: icons.rst

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

|phase_6| |error|

This rule checks the **begin** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

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

|phase_6| |error|

This rule checks the **function** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

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

Refer to `Configuring Previous Line Rules <configuring.html#configuring-previous-line-rules>`_ for options.

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

|phase_3| |error| |blank_line|

This rule checks for a blank line below the end of the function declaration.

Refer to the section `Configuring Blank Lines <configuring.html#configuring-blank-lines>`_ for options regarding comments.

**Violation**

.. code-block:: vhdl

   function overflow (a: integer) return integer is
   end;
   signal wr_en : std_logic;

**Fix**

.. code-block:: vhdl

   function overflow (a: integer) return integer is
   end;

   signal wr_en : std_logic;

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

|phase_1| |error|

This rule checks for a function parameter on the same line as the function keyword when the parameters are on multiple lines.

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

   function func_1 (
     a : integer; b : integer;
     c : unsigned(3 downto 0);
     d : std_logic_vector(7 downto 0);
     e : std_logic) return integer is
   begin

   end;

function_010
############

|phase_6| |error|

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

|phase_5| |error|

This rule checks the colons are in the same column for all declarations in the function declarative part.

Refer to the section `Configuring Keyword Alignment Rules <configuring.html#configuring-keyword-alignment-rules>`_ for information on changing the configurations.

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

|phase_6| |error|

This rule checks the **end** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

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

|phase_6| |error|

This rule checks the **function** keyword in the **end function** has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

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

|phase_5| |error|

This rule checks the identifiers for all declarations are aligned in the function declarative part.

Refer to the section `Configuring Identifier Alignment Rules <configuring.html#configuring-identifier-alignment-rules>`_ for information on changing the configurations.

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

|phase_6| |error|

This rule checks the function designator has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   function OVERflow (a: integer) return integer is

**Fix**

.. code-block:: vhdl

   function overflow (a: integer) return integer is

function_100
############

|phase_2| |error| |whitespace|

This rule checks for a single space between the following function elements:  **function** keyword, function designator, open parenthesis, close parenthesis, **return** keyword, return type and **is** keyword.

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

|phase_3| |error| |blank_line|

This rule checks for a blank line below the **is** keyword.

This rule allows the **begin** keyword to occupy the blank line:

.. code-block:: vhdl

   function overflow (a: integer) return integer is
   begin

Refer to the section `Configuring Blank Lines <configuring.html#configuring-blank-lines>`_ for options regarding comments.

**Violation**

.. code-block:: vhdl

   function overflow (a: integer) return integer is
     constant width : integer := 32;
   begin

**Fix**

.. code-block:: vhdl

   function overflow (a: integer) return integer is

     constant width : integer := 32;
   begin

function_202
############

|phase_3| |error| |blank_line|

This rule checks for blank lines above the **begin** keyword.

This rule allows the **is** keyword to occupy the blank line:

.. code-block:: vhdl

   function overflow (a: integer) return integer is
   begin

Refer to `Configuring Blank Lines <configuring.html#configuring-blank-lines>`_ for options.

**Violation**

.. code-block:: vhdl

   function overflow (a: integer) return integer is

     constant width : integer := 32;
   begin

**Fix**

.. code-block:: vhdl

   function overflow (a: integer) return integer is

     constant width : integer := 32;

   begin

function_203
############

|phase_3| |error| |blank_line|

This rule checks for a blank line below the **begin** keyword.

Refer to the section `Configuring Blank Lines <configuring.html#configuring-blank-lines>`_ for options regarding comments.

**Violation**

.. code-block:: vhdl

   function overflow (a: integer) return integer is
   begin
     a <= b;

**Fix**

.. code-block:: vhdl

   function overflow (a: integer) return integer is
   begin

     a <= b;

function_204
############

|phase_3| |error| |blank_line|

This rule checks for blank lines above the **end** keyword.

Refer to `Configuring Blank Lines <configuring.html#configuring-blank-lines>`_ for options.

**Violation**

.. code-block:: vhdl

   begin

     a <= b;
   end function overflow;

**Fix**

.. code-block:: vhdl

   begin

     a <= b;

   end function overflow;

function_300
############

|phase_4| |error| |indent|

This rule checks the indent of the closing parenthesis if it is on it's own line.

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

function_502
############

|phase_6| |error|

This rule checks the **is** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   function overflow (a: integer) return integer IS

**Fix**

.. code-block:: vhdl

   function overflow (a: integer) return integer is

function_506
############

|phase_6| |error|

This rule checks the function designator has proper case on the end function declaration.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   end function OVERFLOW;

**Fix**

.. code-block:: vhdl

   end function overflow;


