.. include:: icons.rst

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

|phase_4| |error| |indent|

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

|phase_4| |error| |indent|

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

|phase_4| |error| |indent|

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

|phase_4| |error| |indent|

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

|phase_4| |error| |indent|

This rule checks the indent of lines between the **is** and **begin** keywords

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

|phase_4| |error| |indent|

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

|phase_6| |error| |case|

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

|phase_6| |error| |case| |case_keyword|

This rule checks the **end** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

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

|phase_6| |error| |case| |case_keyword|

This rule checks the **procedure** keyword in the **end procedure** has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

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

|phase_5| |error| |alignment|

This rule checks the identifiers for all declarations are aligned in the procedure declarative part.

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

procedure_011
#############

|phase_1| |error| |structure|

This rule checks for a procedure parameter on the same line as the procedure keyword when the parameters are on multiple lines.

**Violation**

.. code-block:: vhdl

   procedure average_samples (constant a : in integer;
     signal d : out std_logic
   ) is
   begin


**Fix**

.. code-block:: vhdl

   procedure average_samples (
     constant a : in integer;
     signal d : out std_logic
   ) is
   begin

procedure_100
#############

|phase_2| |error| |whitespace|

This rule checks for a single space between the following procedure elements:  **procedure** keyword, procedure designator, open parenthesis, close parenthesis, and **is** keywords.

**Violation**

.. code-block:: vhdl

   procedure    average_samples    (
       constant a : in integer;
       signal d : out std_logic
     )    is
   procedure    average_samples      is

**Fix**

.. code-block:: vhdl

   procedure average_samples (
       constant a : in integer;
       signal d : out std_logic
     ) is
   procedure average_samples is

procedure_101
#############

|phase_2| |error| |whitespace|

This rule checks for a single space between the **end** and **procedure** keywords and procedure designator.

**Violation**

.. code-block:: vhdl

   end   procedure   average_samples;
   end   procedure;
   end   average_samples;

**Fix**

.. code-block:: vhdl

   end procedure average_samples;
   end procedure;
   end average_samples;

procedure_200
#############

|phase_3| |error| |blank_line|

This rule checks for blank lines or comments above the **procedure** keyword.

Refer to `Configuring Previous Line Rules <configuring.html#configuring-previous-line-rules>`_ for options.

**Violation**

.. code-block:: vhdl

   architecture RTL of FIFO is
     procedure proc1 is


**Fix**

.. code-block:: vhdl

   architecture RTL of FIFO is

     procedure proc1 is

procedure_201
#############

This rule has been moved to rule `subprogram_body_201 <subprogram_rules.html#subprogram-body-201>`_.

procedure_202
#############

This rule has been moved to rule `subprogram_body_202 <subprogram_rules.html#subprogram-body-202>`_.

procedure_203
#############

This rule has been moved to rule `subprogram_body_203 <subprogram_rules.html#subprogram-body-203>`_.

procedure_204
#############

This rule has been moved to rule `subprogram_body_204 <subprogram_rules.html#subprogram-body-204>`_.

procedure_205
#############

This rule has been moved to rule `subprogram_body_205 <subprogram_rules.html#subprogram-body-205>`_.

procedure_401
#############

|phase_5| |error| |alignment|

This rule checks the colons are in the same column for all declarations in the procedure declarative part.

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

procedure_410
#############

|phase_5| |error| |alignment|

This rule checks the alignment of the colon for each parameter in the procedure declaration.

Refer to the section `Configuring Keyword Alignment Rules <configuring.html#configuring-keyword-alignment-rules>`_ for information on changing the configurations.

**Violation**

.. code-block:: vhdl

     procedure average_samples (
       constant a : in integer;
       signal d : out std_logic
     );

**Fix**

.. code-block:: vhdl

     procedure average_samples (
       constant a : in integer;
       signal d   : out std_logic
     );

procedure_411
#############

|phase_5| |error| |alignment|

This rule checks the alignment of **:=** operator for each parameter in the procedure declaration.

Refer to the section `Configuring Keyword Alignment Rules <configuring.html#configuring-keyword-alignment-rules>`_ for information on changing the configurations.

**Violation**

.. code-block:: vhdl

     procedure average_samples (
       constant a : in integer := 0;
       signal d : out std_logic   := 'X';
     );

**Fix**

.. code-block:: vhdl

     procedure average_samples (
       constant a : in integer  := 0;
       signal d : out std_logic := 'X';
     );

procedure_412
#############

|phase_5| |error| |alignment|

This rule checks for alignment of inline comments for each parameter in the procedure declaration.

Refer to the section `Configuring Keyword Alignment Rules <configuring.html#configuring-keyword-alignment-rules>`_ for information on changing the configurations.

**Violation**

.. code-block:: vhdl

     procedure average_samples (
       constant a : in integer;   -- Comment about a
       signal d   : out std_logic;   -- Comment about d
     );

**Fix**

.. code-block:: vhdl

     procedure average_samples (
       constant a : in integer;    -- Comment about a
       signal d   : out std_logic; -- Comment about d
     );

procedure_500
#############

|phase_6| |error| |case| |case_keyword|

This rule checks the **procedure** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   PROCEDURE average_samples is

**Fix**

.. code-block:: vhdl

   procedure average_samples is

procedure_501
#############

|phase_6| |error| |case| |case_name|

This rule checks the procedure designator has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   procedure AVERAGE_SAMPLES is

**Fix**

.. code-block:: vhdl

   procedure average_samples is

procedure_502
#############

|phase_6| |error| |case| |case_keyword|

This rule checks the **is** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   procedure average_samples IS

**Fix**

.. code-block:: vhdl

   procedure average_samples is

procedure_503
#############

|phase_6| |error| |case| |case_keyword|

This rule checks the **begin** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   procedure average_samples is
   BEGIN

**Fix**

.. code-block:: vhdl

   procedure average_samples is
   begin

procedure_504
#############

|phase_6| |error| |case| |case_keyword|

This rule checks the **end** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   END procedure average_samples;

**Fix**

.. code-block:: vhdl

   end procedure average_samples;

procedure_505
#############

|phase_6| |error| |case| |case_keyword|

This rule checks the **procedure** keyword in the **end procedure** has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   end PROCEDURE average_samples;

**Fix**

.. code-block:: vhdl

   end procedure average_samples;

procedure_506
#############

|phase_6| |error| |case| |case_name|

This rule checks the procedure designator has proper case on the end procedure declaration.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   end procedure AVERAGE_SAMPLES;

**Fix**

.. code-block:: vhdl

   end procedure average_samples;

procedure_507
#############

|phase_6| |error| |case|

This rule checks for consistent capitalization of procedure names.

**Violation**

.. code-block:: vhdl

   architecture rtl of fifo is

     procedure average_samples is
     begin
     end procedure average_samples

   begin

     Average_samples;

     PROC1 : process () is
     begin

        AVERAGE_SAMPLES;

     end process;

   end architecture rtl;

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

     procedure average_samples is
     begin
     end procedure average_samples

   begin

     average_samples;

     PROC1 : process () is
     begin

        average_samples;

     end process;

   end architecture rtl;

