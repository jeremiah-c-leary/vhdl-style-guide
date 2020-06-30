Function Rules
--------------

function_001
############

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

This rule checks a single space exists after the **function** keyword.

**Violation**

.. code-block:: vhdl

   function     overflow (a: integer) return integer is

**Fix**

.. code-block:: vhdl

   function overflow (a: integer) return integer is

function_003
############

This rule checks for a single space between the function name and the (.'

**Violation**

.. code-block:: vhdl

   function overflow   (a: integer) return integer is

   function underflow(a: integer) return integer is

**Fix**

.. code-block:: vhdl

   function overflow (a: integer) return integer is

   function underflow (a: integer) return integer is

function_004
############

This rule checks the **begin** keyword has proper case.
 
Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

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

This rule checks the **function** keyword has proper case.
 
Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   FUNCTION overflow (a: integer) return integer is

**Fix**

.. code-block:: vhdl

   function overflow (a: integer) return integer is

function_006
############

This rule checks for a blank line above the **function** keyword.

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

This rule checks for a blank line below the end of the function declaration.

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

**Violation**

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

This rule checks the colons are in the same column for all declarations in the function declarative part.

Refer to the section `Configuring Keyword Alignment Rules <configuring_keyword_alignment.html>`_ for information on changing the configurations.

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

This rule checks the **end** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

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

This rule checks the **function** keyword in the **end function** has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

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

This rule checks the identifiers for all declarations are aligned in the function declarative part.

Refer to the section `Configuring Identifier Alignment Rules <configuring_declaration_identifier_alignment.html>`_ for information on changing the configurations.

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
