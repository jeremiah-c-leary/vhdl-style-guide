Component Rules
---------------


component_001
#############

This rule checks the indentation of the **component** keyword.

**Violation**

.. code-block:: vhdl

   architecture RTL of FIFO is 
   begin

   component FIFO is

        component RAM is  

**Fix**

.. code-block:: vhdl

   architecture RTL of FIFO is 
   begin

     component FIFO is

     component RAM is  

component_002
#############

This rule checks for a single space after the **component** keyword.

**Violation**

.. code-block:: vhdl

   component    FIFO is

**Fix**

.. code-block:: vhdl

   component FIFO is

component_003
#############

This rule checks for a blank line above the **component** declaration.

**Violation**

.. code-block:: vhdl

   end component FIFO;
   component RAM is

**Fix**

.. code-block:: vhdl

   end component FIFO;

   component RAM is

component_004
#############

This rule checks the **component** keyword is lowercase.

**Violation**

.. code-block:: vhdl

   COMPONENT FIFO is

   Component FIFO is

**Fix**

.. code-block:: vhdl

   component FIFO is

   component FIFO is


component_005
#############

This rule checks the **is** keyword is on the same line as the **component** keyword.

**Violation**

.. code-block:: vhdl

   component FIFO

   component FIFO
   is

**Fix**

.. code-block:: vhdl

   component FIFO is

   component FIFO is

component_006
#############

This rule checks the **is** keyword is lowercase.

**Violation**

.. code-block:: vhdl

   componet FIFO IS

   componet FIFO Is

**Fix**

.. code-block:: vhdl

   component FIFO is

   component FIFO is

component_007
#############

This rule checks for a single space before the **is** keyword.

**Violation**

.. code-block:: vhdl

   component FIFO    is

**Fix**

.. code-block:: vhdl

   component FIFO is

component_008
#############

This rule checks the component name is uppercase in the component declaration.

**Violation**

.. code-block:: vhdl

   component fifo is

**Fix**

.. code-block:: vhdl

   component FIFO is

component_009
#############

This rule checks the indent of the **end component** keywords.

**Violation**

.. code-block:: vhdl

      OVERFLOW : std_logic
    );
        end component FIFO;

**Fix**

.. code-block:: vhdl

       OVERFLOW : std_logic
     );
   end component FIFO;


component_010
#############

This rule checks the **end** keyword is lowercase.

**Violation**

.. code-block:: vhdl

   END component FIFO;

**Fix**

.. code-block:: vhdl

   end component FIFO;

component_011
#############

This rule checks for single space after the **end** keyword.

**Violation**

.. code-block:: vhdl

   end   component FIFO;

**Fix**

.. code-block:: vhdl

   end component FIFO;

component_012
#############

This rule checks the component name is uppercase in the **end component** line.

**Violation**

.. code-block:: vhdl

   end component fifo;

**Fix**

.. code-block:: vhdl

   end component FIFO;

component_013
#############

This rule checks for a single space after the **component** keyword in the **end component** line.

**Violation**

.. code-block:: vhdl

   end component    FIFO;

**Fix**

.. code-block:: vhdl

   end component FIFO;

component_014
#############

This rule checks the **component** keyword is lowercase in the **end component** line.

**Violation**

.. code-block:: vhdl

   end COMPONENT FIFO;

**Fix**

.. code-block:: vhdl

   end component FIFO;

component_015
#############

This rule checks for the **component** keyword in the **end component** line.

**Violation**

.. code-block:: vhdl

   end FIFO;

   end;

**Fix**

.. code-block:: vhdl

   end component FIFO;

   end component;

component_016
#############

This rule checks for blank lines above the **end component** line.

**Violation**

.. code-block:: vhdl

       OVERFLOW : std_logic
     );



   end component FIFO;

**Fix**

.. code-block:: vhdl

       OVERFLOW : std_logic
     );
   end component FIFO;

component_017
#############

This rule checks the alignment of the : in port declarations.

**Violation**

.. code-block:: vhdl

   RD_EN : in    std_logic;
   WR_EN   : in    std_logic;
   OVERFLOW : out   std_logic;

**Fix**

.. code-block:: vhdl

   RD_EN    : in    std_logic;
   WR_EN    : in    std_logic;
   OVERFLOW : out   std_logic;

component_018
#############

This rule checks for a blank line below the **end component** line.

**Violation**

.. code-block:: vhdl

   end component FIFO;
   signal rd_en : std_logic;


**Fix**

.. code-block:: vhdl

   end component FIFO;

   signal rd_en : std_logic;

component_019
#############

This rule checks for comments at the end of the port and generic assignments in component declarations.
These comments represent additional maintainence.
They will be out of sync with the entity at some point.
Refer to the entity for port types, port directions and purpose.

**Violation**

.. code-block:: vhdl

   WR_EN : in    std_logic;  -- Enables write to RAM
   RD_EN : out   std_logic; -- Enable reads from RAM

**Fix**

.. code-block:: vhdl

   WR_EN : in    std_logic;
   RD_EN : out   std_logic;

