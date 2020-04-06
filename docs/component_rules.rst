Component Rules
---------------


component_001
#############

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

This rule checks for a single space after the **component** keyword.

**Violation**

.. code-block:: vhdl

   component    fifo is

**Fix**

.. code-block:: vhdl

   component fifo is

component_003
#############

This rule checks for a blank line above the **component** declaration.

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

This rule checks the **component** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

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

This rule checks the **is** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

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

This rule checks for a single space before the **is** keyword.

**Violation**

.. code-block:: vhdl

   component fifo    is

**Fix**

.. code-block:: vhdl

   component fifo is

component_008
#############

This rule checks the component name has proper case in the component declaration.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   component FIFO is

**Fix**

.. code-block:: vhdl

   component fifo is

component_009
#############

This rule checks the indent of the **end component** keywords.

**Violation**

.. code-block:: vhdl

      overflow : std_logic
    );
        end component FIFO;

**Fix**

.. code-block:: vhdl

       overflow : std_logic
     );
   end component FIFO;


component_010
#############

This rule checks the **end** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   END component fifo;

**Fix**

.. code-block:: vhdl

   end component fifo;

component_011
#############

This rule checks for single space after the **end** keyword.

**Violation**

.. code-block:: vhdl

   end   component fifo;

**Fix**

.. code-block:: vhdl

   end component fifo;

component_012
#############

This rule checks the proper case of the component name in the **end component** line.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   end component FIFO;

**Fix**

.. code-block:: vhdl

   end component fifo;

component_013
#############

This rule checks for a single space after the **component** keyword in the **end component** line.

**Violation**

.. code-block:: vhdl

   end component    fifo;

**Fix**

.. code-block:: vhdl

   end component fifo;

component_014
#############

This rule checks the **component** keyword in the **end component** line has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   end COMPONENT fifo;

**Fix**

.. code-block:: vhdl

   end component fifo;

component_015
#############

This rule checks for the **component** keyword in the **end component** line.

**Violation**

.. code-block:: vhdl

   end fifo;

   end;

**Fix**

.. code-block:: vhdl

   end component fifo;

   end component;

component_016
#############

This rule checks for blank lines above the **end component** line.

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

This rule checks the alignment of the **:** for each generic and port in the component declaration.

Following extra configurations are supported:

* :code:`separate_generic_port_alignment`.

Refer to the section `Configuring Keyword Alignment Rules <configuring_keyword_alignment.html>`_ for information on changing the configurations.

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

This rule checks for a blank line below the **end component** line.

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

This rule checks for comments at the end of the port and generic clauses in component declarations.
These comments represent additional maintainence.
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

This rule checks for alignment of inline comments in the component declaration.

Following extra configurations are supported:

* :code:`separate_generic_port_alignment`.

Refer to the section `Configuring Keyword Alignment Rules <configuring_keyword_alignment.html>`_ for information on changing the configurations.

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

