Architecture Rules
------------------

architecture_001
################

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

This rule check for a blank lines or comments above the **architecture** declaration.

Refer to `Configuring Previous Line Rules <configuring.html#configuring-previous-line-rules>`_ for options.

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

This rule checks the proper case of the **architecture** keyword in the architecture declaration.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   ARCHITECTURE rtl of fifo is

.. code-block:: vhdl

   architecture rtl of fifo is

architecture_005
################

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

This rule checks the **end** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

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

This rule checks for the keyword **architecture** in the **end architecture** statement.
It is clearer to the reader to state what is ending.

Refer to the section `Configuring Optional Items <configuring.html#configuring-optional-items>`_ for options.

**Violation**

.. code-block:: vhdl

   end architecture_name;

**Fix**

.. code-block:: vhdl

   end architecture architecture_name;

architecture_011
################

This rule checks the architecture name case in the **end architecture** statement.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.


**Violation**

.. code-block:: vhdl

   end architecture ARCHITECTURE_NAME;

**Fix**

.. code-block:: vhdl

   end architecture architecture_name;

architecture_012
################

This rule checks for a single space between **end** and **architecture** keywords.

**Violation**

.. code-block:: vhdl

   end    architecture architecture_name;

**Fix**

.. code-block:: vhdl

   end architecture architecture_name;

architecture_013
################

This rule checks the case of the architecture name in the architecture declaration.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   architecture RTL of fifo is

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

architecture_014
################

This rule checks the case of the entity name in the architecture declaration.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   architecture rtl of FIFO is

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

architecture_015
################

This rule check for blank lines below the architecture declaration.

Refer to `Configuring Blank Lines <configuring.html#configuring-blank-lines>`_ for options.

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

This rule checks for blank lines above the **begin** keyword.

Refer to `Configuring Blank Lines <configuring.html#configuring-blank-lines>`_ for options.

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

This rule checks for a blank line below the **begin** keyword.

Refer to the section `Configuring Blank Lines <configuring.html#configuring-blank-lines>`_ for options regarding comments.

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

This rule checks for blank lines or comments above the **end architecture** declaration.

Refer to `Configuring Blank Lines <configuring.html#configuring-blank-lines>`_ for options.

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

This rule checks the proper case of the **of** keyword in the architecture declaration.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   architecture rtl OF fifo is

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

architecture_020
################

This rule checks the proper case of the **is** keyword in the architecture declaration.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   architecture rtl of fifo IS

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

architecture_021
################

This rule checks the proper case of the **begin** keyword.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

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

This rule checks for a single space before the entity name in the end architecture declaration.

**Violation**

.. code-block:: vhdl

   end architecture    fifo;

**Fix**

.. code-block:: vhdl

   end architecture fifo;

architecture_024
################

This rule checks for the architecture name in the **end architecture** statement.
It is clearer to the reader to state which architecture the end statement is closing.

Refer to the section `Configuring Optional Items <configuring.html#configuring-optional-items>`_ for options.

**Violation**

.. code-block:: vhdl

   end architecture;

**Fix**

.. code-block:: vhdl

   end architecture architecture_name;

architecture_025
################

This rule checks for valid names for the architecture.
Typical architecture names are:  RTL, EMPTY, and BEHAVE.
This rule allows the user to restrict what can be used for an architecture name.

.. NOTE:: This rule is disabled by default.
   You can enable and configure the names using the following configuration.

   .. code-block:: yaml

      ---

      rule :
        architecture_025 :
          disabled : False
          names :
            - rtl
            - empty
            - behave

**Violation**

.. code-block:: vhdl

   architecture some_invalid_arch_name of entity1 is

**Fix**

The user is required to decide which is the correct architecture name.

architecture_026
################

This rule checks the colons are in the same column for all declarations in the architecture declarative part.

Refer to the section `Configuring Keyword Alignment Rules <configuring.html#configuring-keyword-alignment-rules>`_ for information on changing the configurations.

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

This rule checks the alignment of inline comments in the architecture declarative part.

Refer to the section `Configuring Keyword Alignment Rules <configuring.html#configuring-keyword-alignment-rules>`_ for information on changing the configurations.

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

This rule checks the **architecture** keyword in the **end architecture** has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

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

This rule checks for alignment of identifiers in attribute, type, subtype, constant, signal, variable and file declarations in the architecture declarative region.

Refer to the section `Configuring Identifier Alignment Rules <configuring.html#configuring-identifier-alignment-rules>`_ for information on changing the configurations.

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

This rule checks for a single space between **architecture** and the identifier.

**Violation**

.. code-block:: vhdl

   architecture    rtl of fifo is

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

architecture_031
################

This rule checks for a single space between the identifier and the **of** keyword.

**Violation**

.. code-block:: vhdl

   architecture rtl    of fifo is

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

architecture_032
################

This rule checks for a single space between the **of** keyword and the entity_name.

**Violation**

.. code-block:: vhdl

   architecture rtl of    fifo is

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

architecture_033
################

This rule checks for a single space between the entity_name and the **is** keyword.

**Violation**

.. code-block:: vhdl

   architecture rtl of fifo    is

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

Vertical Spacing Rules (200 - 299)
##################################

architecture_200
^^^^^^^^^^^^^^^^

This rule checks for a blank line below the end architecture statement.

Refer to the section `Configuring Blank Lines <configuring.html#configuring-blank-lines>`_ for options regarding comments.

**Violation**

.. code-block:: vhdl

   end architecture;
   library ieee;

**Fix**

.. code-block:: vhdl

   end architecture;

   library ieee;

Naming Convention Rules (600 - 699)
###################################

architecture_600
^^^^^^^^^^^^^^^^

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

