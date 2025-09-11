.. include:: includes.rst

Architecture Rules
------------------

architecture_001
################

|phase_4| |error| |indent|

This rule checks for blank spaces before the **architecture** keyword.

**Violation**

.. code-block:: vhdl

     architecture rtl of fifo is
   begin

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is
   begin

architecture_002
################

This rule has been split into the following rules:

* :ref:`architecture_030`
* :ref:`architecture_031`
* :ref:`architecture_032`
* :ref:`architecture_033`

architecture_003
################

|phase_3| |error| |blank_line|

This rule checks for a blank lines or comments above the **architecture** declaration.

|configuring_previous_line_rules_link|

**Violation**

.. code-block:: vhdl

   library ieee;
   architecture rtl of fifo is

**Fix**

.. code-block:: vhdl

   library ieee;

   architecture rtl of fifo is

architecture_004
################

|phase_6| |error| |case| |case_keyword|

This rule checks the proper case of the **architecture** keyword in the architecture declaration.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   ARCHITECTURE rtl of fifo is

.. code-block:: vhdl

   architecture rtl of fifo is

architecture_005
################

|phase_1| |error| |structure|

This rule checks the **of** keyword is on the same line as the **architecture** keyword.

**Violation**

.. code-block:: vhdl

   architecture rtl
     of fifo is

**Fix**

.. code-block:: vhdl

   architecture rtl of
   fifo is

architecture_006
################

|phase_1| |error| |structure|

This rule checks the **is** keyword is on the same line as the **architecture** keyword.

**Violation**

.. code-block:: vhdl

   architecture rtl of fifo
     is

   architecture rtl of fifo

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

   architecture rtl of fifo is

architecture_007
################

|phase_4| |error| |indent|

This rule checks for spaces before the **begin** keyword.

**Violation**

.. code-block:: vhdl

   architecture rtl of fifo is
     begin

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is
   begin

architecture_008
################

|phase_4| |error| |indent|

This rule checks for spaces before the **end architecture** keywords.

**Violation**

.. code-block:: vhdl

   architecture rtl of fifo is
   begin
     end architecture

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is
   begin
   end architecture

architecture_009
################

|phase_6| |error| |case| |case_keyword|

This rule checks the **end** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   END architecture;

   End architecture;

**Fix**

.. code-block:: vhdl

   end architecture;

   end architecture;

architecture_010
################

|phase_1| |error| |structure| |structure_optional|

This rule checks for the keyword **architecture** in the **end architecture** statement.
It is clearer to the reader to state what is ending.

|configuring_optional_items_link|

**Violation**

.. code-block:: vhdl

   end architecture_name;

**Fix**

.. code-block:: vhdl

   end architecture architecture_name;

architecture_011
################

|phase_6| |error| |case| |case_name|

This rule checks the architecture name case in the **end architecture** statement.

|configuring_uppercase_and_lowercase_rules_link|


**Violation**

.. code-block:: vhdl

   end architecture ARCHITECTURE_NAME;

**Fix**

.. code-block:: vhdl

   end architecture architecture_name;

architecture_012
################

|phase_2| |error| |whitespace|

This rule checks for a single space between **end** and **architecture** keywords.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   end    architecture architecture_name;

**Fix**

.. code-block:: vhdl

   end architecture architecture_name;

architecture_013
################

|phase_6| |error| |case| |case_name|

This rule checks the case of the architecture name in the architecture declaration.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   architecture RTL of fifo is

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

architecture_014
################

|phase_6| |error| |case| |case_name|

This rule checks the case of the entity name in the architecture declaration.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   architecture rtl of FIFO is

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

architecture_015
################

|phase_3| |error| |blank_line|

This rule checks for blank lines below the architecture declaration.

|configuring_blank_lines_link|

**Violation**

.. code-block:: vhdl

   architecture rtl of fifo is
     signal wr_en : std_logic;
   begin

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

     signal wr_en : std_logic;
   begin

architecture_016
################

|phase_3| |error| |blank_line|

This rule checks for blank lines above the **begin** keyword.

|configuring_blank_lines_link|

**Violation**

.. code-block:: vhdl

   architecture rtl of fifo is

     signal wr_en : std_logic;
   begin

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

     signal wr_en : std_logic;

   begin

architecture_017
################

|phase_3| |error| |blank_line|

This rule checks for a blank line below the **begin** keyword.

|configuring_blank_lines_link|

**Violation**

.. code-block:: vhdl

   begin
     wr_en <= '0';

**Fix**

.. code-block:: vhdl

   begin

     wr_en <= '0';

architecture_018
################

|phase_3| |error| |blank_line|

This rule checks for blank lines or comments above the **end architecture** declaration.

|configuring_blank_lines_link|

**Violation**

.. code-block:: vhdl

     rd_en <= '1';
   end architecture RTL;

**Fix**

.. code-block:: vhdl

     rd_en <= '1';

   end architecture RTL;

architecture_019
################

|phase_6| |error| |case| |case_keyword|

This rule checks the proper case of the **of** keyword in the architecture declaration.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   architecture rtl OF fifo is

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

architecture_020
################

|phase_6| |error| |case| |case_keyword|

This rule checks the proper case of the **is** keyword in the architecture declaration.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   architecture rtl of fifo IS

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

architecture_021
################

|phase_6| |error| |case| |case_keyword|

This rule checks the proper case of the **begin** keyword.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   architecture rtl of fifo is
   BEGIN

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is
   begin

architecture_022
################

|phase_2| |error| |whitespace|

This rule checks for a single space before the entity name in the end architecture declaration.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   end architecture    fifo;

**Fix**

.. code-block:: vhdl

   end architecture fifo;

architecture_024
################

|phase_1| |error| |structure| |structure_optional|

This rule checks for the architecture name in the **end architecture** statement.
It is clearer to the reader to state which architecture the end statement is closing.

|configuring_optional_items_link|

**Violation**

.. code-block:: vhdl

   end architecture;

**Fix**

.. code-block:: vhdl

   end architecture architecture_name;

architecture_025
################

|phase_7| |disabled| |error| |unfixable| |naming|

This rule checks for valid names for the architecture.
Typical architecture names are:  RTL, EMPTY, and BEHAVE.
This rule allows the user to restrict what can be used for an architecture name.
Note that regular expressions are accepted in the **names** field.

.. NOTE:: This rule is disabled by default.
   You can enable and configure the names using the following configuration.

   .. code-block:: yaml

      ---

      rule :
        architecture_025 :
          disable : False
          names :
            - rtl
            - empty
            - behave
            - my_pattern.*

**Violation**

.. code-block:: vhdl

   architecture some_invalid_arch_name of entity1 is

**Fix**

The user is required to decide which is the correct architecture name.

architecture_026
################

|phase_5| |error| |alignment|

This rule checks the colons are in the same column for all declarations in the architecture declarative part.

|configuring_keyword_alignment_rules_link|

**Violation**

.. code-block:: vhdl

   architecture rtl of my_entity is

     signal   wr_en : std_logic;
     signal   rd_en   : std_logic;
     constant c_period : time;

   begin

**Fix**

.. code-block:: vhdl

   architecture rtl of my_entity is

     signal   wr_en    : std_logic;
     signal   rd_en    : std_logic;
     constant c_period : time;

   begin

architecture_027
################

|phase_5| |error| |alignment|

This rule checks the alignment of inline comments in the architecture declarative part.

|configuring_keyword_alignment_rules_link|

**Violation**

.. code-block:: vhdl

   architecture rtl of my_entity is

     signal   wr_en    : std_logic;  -- Comment 1
     signal   rd_en    : std_logic;     -- Comment 2
     constant c_period : time; -- Comment 3

   begin

**Fix**

.. code-block:: vhdl

   architecture rtl of my_entity is

     signal   wr_en    : std_logic; -- Comment 1
     signal   rd_en    : std_logic; -- Comment 2
     constant c_period : time;      -- Comment 3

   begin

architecture_028
################

|phase_6| |error| |case| |case_keyword|

This rule checks the **architecture** keyword in the **end architecture** has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   end ARCHITECTURE;

   end Architecture;

**Fix**

.. code-block:: vhdl

   end architecture;

   end architecture;

architecture_029
################

|phase_5| |error| |alignment|

This rule checks for alignment of names in alias, attribute, type, subtype, constant, signal, variable and file declarations in the architecture declarative region.

|configuring_identifier_alignment_rules_link|

**Violation**

.. code-block:: vhdl

   signal    sig1 : std_logic;
   file some_file :
   variable v_var1 : std_logic;
   type t_myType : std_logic;

**Fix**

.. code-block:: vhdl

   signal   sig1 : std_logic;
   file     some_file :
   variable v_var1 : std_logic;
   type     t_myType : std_logic;

architecture_030
################

|phase_2| |error| |whitespace|

This rule checks for a single space between **architecture** and the name.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   architecture    rtl of fifo is

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

architecture_031
################

|phase_2| |error| |whitespace|

This rule checks for a single space between the name and the **of** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   architecture rtl    of fifo is

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

architecture_032
################

|phase_2| |error| |whitespace|

This rule checks for a single space between the **of** keyword and the entity_name.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   architecture rtl of    fifo is

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

architecture_033
################

|phase_2| |error| |whitespace|

This rule checks for a single space between the entity_name and the **is** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   architecture rtl of fifo    is

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

architecture_200
################

|phase_3| |error| |blank_line|

This rule checks for a blank line below the end architecture statement.

|configuring_blank_lines_link|

**Violation**

.. code-block:: vhdl

   end architecture;
   library ieee;

**Fix**

.. code-block:: vhdl

   end architecture;

   library ieee;

architecture_400
################

|phase_5| |error| |alignment|

This rule checks the colons are in the same column for all attribute specifications.

|configuring_keyword_alignment_rules_link|

**Violation**

.. code-block:: vhdl

     attribute mark_debug of wr_en : signal is "true";
     attribute mark_debug of almost_empty : signal is "true";
     attribute mark_debug of full : signal is "true";

**Fix**

.. code-block:: vhdl

     attribute mark_debug of wr_en        : signal is "true";
     attribute mark_debug of almost_empty : signal is "true";
     attribute mark_debug of full         : signal is "true";

architecture_600
################

|phase_6| |error| |case|

This rule checks for consistent capitalization of generic names in an architecture body.

**Violation**

.. code-block:: vhdl

   entity FIFO is
     generic (
       G_WIDTH : natural := 16
     );
   end entity fifo;

   architecture rtl of fifo is

      signal w_data : std_logic_vector(g_width - 1 downto 0);

   begin

      output <= large_data(g_width - 1 downto 0);

   end architecture rtl;

**Fix**

.. code-block:: vhdl

   entity FIFO is
     generic (
       G_WIDTH : natural := 16
     );
   end entity fifo;

   architecture rtl of fifo is

      signal w_data : std_logic_vector(G_WIDTH - 1 downto 0);

   begin

      output <= large_data(G_WIDTH - 1 downto 0);

   end architecture rtl;

architecture_601
################

|phase_6| |error| |case|

This rule checks for consistent capitalization of port names in an architecture body.

**Violation**

.. code-block:: vhdl

   entity FIFO is
     port (
       I_DATA : in std_logic_vector(31 downto 0)
     );
   end entity fifo;

   architecture rtl of fifo is

   begin

      register <= i_data;

   end architecture rtl;

**Fix**

.. code-block:: vhdl

   entity FIFO is
     port (
       I_DATA : in std_logic_vector(31 downto 0)
     );
   end entity fifo;

   architecture rtl of fifo is

   begin

      register <= I_DATA;

   end architecture rtl;
