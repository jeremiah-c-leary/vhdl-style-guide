Entity Rules
------------

entity_001
##########

This rule checks the indent of the **entity** keyword.

**Violation**

.. code-block:: vhdl

   library ieee;

     entity fifo is

**Fix**

.. code-block:: vhdl

   library ieee;

   entity fifo is


entity_002
##########

This rule checks for a single space after the **entity** keyword.

**Violation**

.. code-block:: vhdl

   entity    fifo is

**Fix**

.. code-block:: vhdl

   entity fifo is

entity_003
##########

This rule checks for a blank line above the entity keyword.

Refer to the section `Configuring Blank Lines <configuring_blank_lines.html>`_ for options regarding comments.

**Violation**

.. code-block:: vhdl

   library ieee;
   entity fifo is

**Fix**

.. code-block:: vhdl

   library ieee;

   entity fifo is

entity_004
##########

This rule checks the **entity** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   ENTITY fifo is

**Fix**

.. code-block:: vhdl

   entity fifo is

entity_005
##########

This rule checks the **is** keyword is on the same line as the **entity** keyword.

**Violation**

.. code-block:: vhdl

   entity fifo

   entity fifo
     is

**Fix**

.. code-block:: vhdl

   entity fifo is

   entity fifo is

entity_006
##########

This rule checks the **is** keyword has proper case in the entity declaration.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   entity fifo IS

**Fix**

.. code-block:: vhdl

   entity fifo is

entity_007
##########

This rule checks for a single space before the **is** keyword.

**Violation**

.. code-block:: vhdl

   entity fifo    is

**Fix**

.. code-block:: vhdl

   entity fifo is

entity_008
##########

This rule checks the entity name has proper case in the entity declaration.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   entity Fifo is

**Fix**

.. code-block:: vhdl

   entity fifo is

entity_009
##########

This rule checks the indent of the **end** keyword.

**Violation**

.. code-block:: vhdl

     wr_en : in    std_logic;
     rd_en : in    std_logic
   );   
     end entity fifo;

**Fix**

.. code-block:: vhdl

       wr_en : in    std_logic;
       rd_en : in    std_logic
     );   
   end entity fifo;

entity_010
##########

This rule checks the **end** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   END entity fifo;

**Fix**

.. code-block:: vhdl

   end entity fifo;

entity_011
##########

This rule checks for a single space after the **end** keyword.

**Violation**

.. code-block:: vhdl

   end    entity fifo;

**Fix**

.. code-block:: vhdl

   end entity fifo;

entity_012
##########

This rule checks the case of the entity name in the **end entity** statement.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   end entity FIFO;

**Fix**

.. code-block:: vhdl

   end entity fifo;

entity_013
##########

This rule checks for a single space after the **entity** keyword in the closing of the entity declaration.

**Violation**

.. code-block:: vhdl

   end entity    fifo;

**Fix**

.. code-block:: vhdl

   end entity fifo;

entity_014
##########

This rule checks the **entity** keyword has proper case in the closing of the entity declaration.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   end ENTITY fifo;

**Fix**

.. code-block:: vhdl

   end entity fifo;

entity_015
##########

This rule checks for the keyword **entity** in the **end entity** statement.

Refer to the section `Configuring Optional Items <configuring_optional_items.html>`_ for options.

**Violation**

.. code-block:: vhdl

   end fifo;

   end;

**Fix**

.. code-block:: vhdl

   end entity fifo;

   end entity;

entity_016
##########

This rule checks for blank lines above the **end entity** keywords.

**Violation**

.. code-block:: vhdl

       wr_en : in    std_logic;
       rd_en : in    std_logic
     );

  
   end entity fifo;


**Fix**

.. code-block:: vhdl

       wr_en : in    std_logic;
       rd_en : in    std_logic
     );   
   end entity fifo;

entity_017
##########

This rule checks the alignment of the **:** for each generic and port in the entity declaration.

Following extra configurations are supported:

* :code:`separate_generic_port_alignment`.

Refer to the section `Configuring Keyword Alignment Rules <configuring_keyword_alignment.html>`_ for information on changing the configurations.

**Violation**

.. code-block:: vhdl

   generic (
       g_width : positive;
       g_output_delay : positive
   );
   port (
       clk_i : in std_logic;
       data_i : in std_logic;
       data_o : in std_logic
   );

**Fix**

.. code-block:: vhdl

   generic (
       g_width        : positive;
       g_output_delay : positive
   );
   port (
       clk_i  : in std_logic;
       data_i : in std_logic;
       data_o : in std_logic
   );

entity_018
##########

This rule checks the alignment of **:=** operator for each generic and port in the entity declaration.

Following extra configurations are supported:

* :code:`separate_generic_port_alignment`.

Refer to the section `Configuring Keyword Alignment Rules <configuring_keyword_alignment.html>`_ for information on changing the configurations.

**Violation**

.. code-block:: vhdl

   generic (
       g_width        : positive := 8;
       g_output_delay : positive      := 5
   );
   port (
       clk_i   : in std_logic;
       data1_i : in std_logic  := 'X';
       data2_i : in std_logic      := 'X';
       data_o  : in std_logic
   );

**Fix**

.. code-block:: vhdl

   generic (
       g_width        : positive := 8;
       g_output_delay : positive := 5
   );
   port (
       clk_i   : in std_logic;
       data1_i : in std_logic := 'X';
       data2_i : in std_logic := 'X';
       data_o  : in std_logic
   );


entity_019
##########

This rule checks for the entity name in the **end entity** statement.

Refer to the section `Configuring Optional Items <configuring_optional_items.html>`_ for options.

**Violation**

.. code-block:: vhdl

   end entity;

**Fix**

.. code-block:: vhdl

   end entity entity_name;

entity_020
##########

This rule checks for alignment of inline comments in the entity declaration.

Following extra configurations are supported:

* :code:`separate_generic_port_alignment`.

Refer to the section `Configuring Keyword Alignment Rules <configuring_keyword_alignment.html>`_ for information on changing the configurations.

**Violation**

.. code-block:: vhdl

   generic (
       g_width        : positive;  -- Data width
       g_output_delay : positive -- Delay at output
   );
   port (
       clk_i  : in std_logic; -- Input clock
       data_i : in std_logic;   -- Data input
       data_o : in std_logic -- Data output
   );

**Fix**

.. code-block:: vhdl

   generic (
       g_width        : positive; -- Data width
       g_output_delay : positive  -- Delay at output
   );
   port (
       clk_i  : in std_logic; -- Input clock
       data_i : in std_logic; -- Data input
       data_o : in std_logic  -- Data output
   );

