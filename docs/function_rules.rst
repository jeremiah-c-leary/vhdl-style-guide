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

This rule checks for a single space after the function name and the (.'

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

This rule checks the **begin** keyword is lowercase.

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

This rule checks the **function** keyword is lowercase.

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

