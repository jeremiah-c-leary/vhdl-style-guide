Procedure Rules
---------------

There are three forms a procedure:  with parameters, without parameters, and a package declaration:

**with parameters**

.. code-block:: vhdl

   procedure average_samples (
      constant a : in integer;
      signal b : in std_logic;
      variable c : in std_logic_vector(3 downto 0);
      signal d : out std_logic) is
   begin
   end procedure average_samples;

**without parameters**

.. code-block:: vhdl

   procedure average_samples is
   begin
   end procedure average_samples;

**package declaration**

.. code-block:: vhdl

   procedure average_samples;

   procedure average_samples (
      constant a : in integer;
      signal b : in std_logic;
      variable c : in std_logic_vector(3 downto 0);
      signal d : out std_logic);

procedure_001
#############

This rule checks the indent of the **procedure** keyword.

**Violation**

.. code-block:: vhdl

     procedure average_samples (
     constant a : in integer;
     signal b : in std_logic;
     variable c : in std_logic_vector(3 downto 0);
     signal d : out std_logic ) is
   begin
   end procedure average_samples;

**Fix**

.. code-block:: vhdl

   procedure average_samples (
     constant a : in integer;
     signal b : in std_logic;
     variable c : in std_logic_vector(3 downto 0);
     signal d : out std_logic ) is
   begin
   end procedure average_samples;

procedure_002
#############

This rule checks the indent of the **begin** keyword.

**Violation**

.. code-block:: vhdl

   procedure average_samples (
     constant a : in integer;
     signal b : in std_logic;
     variable c : in std_logic_vector(3 downto 0);
     signal d : out std_logic ) is
     begin
   end procedure average_samples;

**Fix**

.. code-block:: vhdl

   procedure average_samples (
     constant a : in integer;
     signal b : in std_logic;
     variable c : in std_logic_vector(3 downto 0);
     signal d : out std_logic ) is
   begin
   end procedure average_samples;

procedure_003
#############

This rule checks the indent of the **end** keyword.

**Violation**

.. code-block:: vhdl

   procedure average_samples (
     constant a : in integer;
     signal b : in std_logic;
     variable c : in std_logic_vector(3 downto 0);
     signal d : out std_logic ) is
   begin
     end procedure average_samples;

**Fix**

.. code-block:: vhdl

   procedure average_samples (
     constant a : in integer;
     signal b : in std_logic;
     variable c : in std_logic_vector(3 downto 0);
     signal d : out std_logic ) is
   begin
   end procedure average_samples;

procedure_004
#############

This rule checks the indent of parameters.

**Violation**

.. code-block:: vhdl

   procedure average_samples (
   constant a : in integer;
       signal b : in std_logic;
      variable c : in std_logic_vector(3 downto 0);
    signal d : out std_logic ) is
   begin
   end procedure average_samples;

**Fix**

.. code-block:: vhdl

   procedure average_samples (
     constant a : in integer;
     signal b : in std_logic;
     variable c : in std_logic_vector(3 downto 0);
     signal d : out std_logic ) is
   begin
   end procedure average_samples;

procedure_005
#############

This rule checks the indent of line between the **is** and **begin** keywords

**Violation**

.. code-block:: vhdl

   procedure average_samples (
     constant a : in integer;
     signal d : out std_logic ) is
   variable var_1 : integer;
       variable var_1 : integer;
   begin
   end procedure average_samples;


**Fix**

.. code-block:: vhdl

   procedure average_samples (
     constant a : in integer;
     signal b : in std_logic;
     variable c : in std_logic_vector(3 downto 0);
     signal d : out std_logic ) is
     variable var_1 : integer;
     variable var_1 : integer;
   begin
   end procedure average_samples;

procedure_006
#############

This rule checks the indent of the closing parenthesis if it is on it's own line.

**Violation**

.. code-block:: vhdl

   procedure average_samples (
     constant a : in integer;
     signal d : out std_logic
     ) is


**Fix**

.. code-block:: vhdl

   procedure average_samples (
     constant a : in integer;
     signal d : out std_logic
   ) is

procedure_007
#############

This rule checks for consistent capitalization of procedure names.

**Violation**

.. code-block:: vhdl

   architecture rtl of entity1 is

     procedure average_samples (
       constant a : in integer;
       signal d : out std_logic
     ) is

   begin

     proc1 : process () is
     begin

       Average_samples();

     end process proc1;

   end architecture rtl; 

**Fix**

.. code-block:: vhdl

   architecture rtl of entity1 is

     procedure average_samples (
       constant a : in integer;
       signal d : out std_logic
     ) is

   begin

     proc1 : process () is
     begin

       average_samples();

     end process proc1;

   end architecture RTL; 
