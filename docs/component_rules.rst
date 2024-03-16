.. include:: includes.rst

Component Rules
---------------

component_001
#############

|phase_4| |error| |indent|

This rule checks the indentation of the **component** keyword.

**Violation**

.. code-block:: vhdl

   architecture rtl of fifo is
   begin

   component fifo is

        component ram is

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is
   begin

     component fifo is

     component ram is

component_002
#############

|phase_2| |error| |whitespace|

This rule checks for a single space after the **component** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   component    fifo is

**Fix**

.. code-block:: vhdl

   component fifo is

component_003
#############

|phase_3| |error| |blank_line|

This rule checks for blank lines or comments above the **component** declaration.

|configuring_previous_line_rules_link|

The default style is :code:`no_code`.

**Violation**

.. code-block:: vhdl

   end component fifo;
   component ram is

**Fix**

.. code-block:: vhdl

   end component fifo;

   component ram is

component_004
#############

|phase_6| |error| |case| |case_keyword|

This rule checks the **component** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   COMPONENT fifo is

   Component fifo is

**Fix**

.. code-block:: vhdl

   component fifo is

   component fifo is

component_005
#############

|phase_1| |error| |structure|

This rule checks the **is** keyword is on the same line as the **component** keyword.

**Violation**

.. code-block:: vhdl

   component fifo

   component fifo
   is

**Fix**

.. code-block:: vhdl

   component fifo is

   component fifo is

component_006
#############

|phase_6| |error| |case| |case_keyword|

This rule checks the **is** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   component fifo IS

   component fifo Is

**Fix**

.. code-block:: vhdl

   component fifo is

   component fifo is

component_007
#############

|phase_2| |error| |whitespace|

This rule checks for a single space before the **is** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   component fifo    is

**Fix**

.. code-block:: vhdl

   component fifo is

component_008
#############

|phase_6| |error| |case| |case_name|

This rule checks the component name has proper case in the component declaration.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   component FIFO is

**Fix**

.. code-block:: vhdl

   component fifo is

component_009
#############

|phase_4| |error| |indent|

This rule checks the indent of the **end component** keywords.

**Violation**

.. code-block:: vhdl

      overflow : std_logic
    );
        end component fifo;

**Fix**

.. code-block:: vhdl

       overflow : std_logic
     );
   end component fifo;

component_010
#############

|phase_6| |error| |case| |case_keyword|

This rule checks the **end** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   END component fifo;

**Fix**

.. code-block:: vhdl

   end component fifo;

component_011
#############

|phase_2| |error| |whitespace|

This rule checks for single space after the **end** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   end   component fifo;

**Fix**

.. code-block:: vhdl

   end component fifo;

component_012
#############

|phase_6| |error| |case| |case_name|

This rule checks the proper case of the component name in the **end component** line.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   end component FIFO;

**Fix**

.. code-block:: vhdl

   end component fifo;

component_013
#############

|phase_2| |error| |whitespace|

This rule checks for a single space after the **component** keyword in the **end component** line.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   end component    fifo;

**Fix**

.. code-block:: vhdl

   end component fifo;

component_014
#############

|phase_6| |error| |case| |case_keyword|

This rule checks the **component** keyword in the **end component** line has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   end COMPONENT fifo;

**Fix**

.. code-block:: vhdl

   end component fifo;

component_015
#############

This rule has been deprecated.
The **component** keyword is required per the LRM.

component_016
#############

|phase_3| |error| |blank_line|

This rule checks for blank lines above the **end component** line.

|configuring_blank_lines_link|

**Violation**

.. code-block:: vhdl

       overflow : std_logic
     );



   end component fifo;

**Fix**

.. code-block:: vhdl

       overflow : std_logic
     );
   end component fifo;

component_017
#############

|phase_5| |error| |alignment|

This rule checks the alignment of the colon for each generic and port in the component declaration.

Following extra configurations are supported:

* :code:`separate_generic_port_alignment`.

|configuring_keyword_alignment_rules_link|

**Violation**

.. code-block:: vhdl

   component my_component
       generic (
           g_width : positive;
           g_output_delay : positive
       );
       port (
           clk_i : in std_logic;
           data_i : in std_logic;
           data_o : in std_logic
       );
   end component;

**Fix**

.. code-block:: vhdl

   component my_component
       generic (
           g_width        : positive;
           g_output_delay : positive
       );
       port (
           clk_i  : in std_logic;
           data_i : in std_logic;
           data_o : in std_logic
       );
   end component;

component_018
#############

|phase_3| |error| |blank_line|

This rule checks for a blank line below the **end component** line.

|configuring_blank_lines_link|

**Violation**

.. code-block:: vhdl

   end component fifo;
   signal rd_en : std_logic;


**Fix**

.. code-block:: vhdl

   end component fifo;

   signal rd_en : std_logic;

component_019
#############

|phase_1| |error| |structure|

This rule checks for comments at the end of the port and generic clauses in component declarations.
These comments represent additional maintenance.
They will be out of sync with the entity at some point.
Refer to the entity for port types, port directions and purpose.

**Violation**

.. code-block:: vhdl

   wr_en : in    std_logic;  -- Enables write to RAM
   rd_en : out   std_logic; -- Enable reads from RAM

**Fix**

.. code-block:: vhdl

   wr_en : in    std_logic;
   rd_en : out   std_logic;

component_020
#############

|phase_5| |error| |alignment|

This rule checks for alignment of inline comments in the component declaration.

Following extra configurations are supported:

* :code:`separate_generic_port_alignment`.

|configuring_keyword_alignment_rules_link|

**Violation**

.. code-block:: vhdl

   component my_component
       generic (
           g_width        : positive;  -- Data width
           g_output_delay : positive -- Delay at output
       );
       port (
           clk_i  : in std_logic; -- Input clock
           data_i : in std_logic;   -- Data input
           data_o : in std_logic -- Data output
       );
   end my_component;

**Fix**

.. code-block:: vhdl

   component my_component
       generic (
           g_width        : positive; -- Data width
           g_output_delay : positive  -- Delay at output
       );
       port (
           clk_i  : in std_logic; -- Input clock
           data_i : in std_logic; -- Data input
           data_o : in std_logic  -- Data output
       );
   end my_component;

component_021
#############

|phase_1| |error| |structure| |structure_optional|

This rule inserts the optional **is** keyword if it does not exist.

|configuring_optional_items_link|

**Violation**

.. code-block:: vhdl

   component my_component

   end my_component;

**Fix**

.. code-block:: vhdl

   component my_component is

   end my_component;

