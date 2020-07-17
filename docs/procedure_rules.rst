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

procedure_008
#############

This rule checks the **end** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   END;

   End procedure proc;

**Fix**

.. code-block:: vhdl

   end;

   end procedure proc;

procedure_009
#############

This rule checks the **procedure** keyword in the **end procedure** has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   end PROCEDURE;

   end Procedure proc;

**Fix**

.. code-block:: vhdl

   end procedure;

   end procedure proc;

procedure_010
#############

This rule checks the identifiers for all declarations are aligned in the procedure declarative part.

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
