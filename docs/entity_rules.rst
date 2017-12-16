Entity Rules
------------

entity_001
##########

This rule checks the indent of the **entity** keyword.

**Violation**

.. code-block:: vhdl

   library ieee;

     entity FIFO is

**Fix**

.. code-block:: vhdl

   library ieee;

   entity FIFO is


entity_002
##########

This rule checks for a single space after the **entity** keyword.

**Violation**

.. code-block:: vhdl

   entity    FIFO is

**Fix**

.. code-block:: vhdl

   entity FIFO is

entity_003
##########

This rule checks for a blank line above the entity keyword.

**Violation**

.. code-block:: vhdl

   library ieee;
   entity FIFO is

**Fix**

.. code-block:: vhdl

   library ieee;

   entity FIFO is

entity_004
##########

This rule checks the **entity** keyword is lowercase.

**Violation**

.. code-block:: vhdl

   ENTITY FIFO is

**Fix**

.. code-block:: vhdl

   entity FIFO is

entity_005
##########

This rule checks the **is** keyword is on the same line as the **entity** keyword.

**Violation**

.. code-block:: vhdl

   entity FIFO

   entity FIFO
     is

**Fix**

.. code-block:: vhdl

   entity FIFO is

   entity FIFO is

entity_006
##########

This rule checks the **is** keyword is lowercase.

**Violation**

.. code-block:: vhdl

   entity FIFO IS

**Fix**

.. code-block:: vhdl

   entity FIFO is

entity_007
##########

This rule checks for a single space before the **is** keyword.

**Violation**

.. code-block:: vhdl

   entity FIFO    is

**Fix**

.. code-block:: vhdl

   entity FIFO is

entity_008
##########

This rule checks the entity name is uppercase in the entity declaration.

**Violation**

.. code-block:: vhdl

   entity fifo is

**Fix**

.. code-block:: vhdl

   entity FIFO is

entity_009
##########

This rule checks the indent of the **end** keyword.

**Violation**

.. code-block:: vhdl

     WR_EN : in    std_logic;
     RD_EN : in    std_logic
   );   
     end entity FIFO;

**Fix**

.. code-block:: vhdl

       WR_EN : in    std_logic;
       RD_EN : in    std_logic
     );   
   end entity FIFO;

entity_010
##########

This rule checks the **end** keyword is lowercase.

**Violation**

.. code-block:: vhdl

   END entity FIFO;

**Fix**

.. code-block:: vhdl

   end entity FIFO;

entity_011
##########

This rule checks for a single space after the **end** keyword.

**Violation**

.. code-block:: vhdl

   end    entity FIFO;

**Fix**

.. code-block:: vhdl

   end entity FIFO;

entity_012
##########

This rule checks the entity name in the **end entity** statement is uppercase.
Uppercasing the entity name makes it stand out.

**Violation**

.. code-block:: vhdl

   end entity fifo;

**Fix**

.. code-block:: vhdl

   end entity FIFO;

entity_013
##########

This rule checks for a single space after the **entity** keyword in the closing of the entity declaration.

**Violation**

.. code-block:: vhdl

   end entity    FIFO;

**Fix**

.. code-block:: vhdl

   end entity FIFO;

entity_014
##########

This rule checks the **entity** keyword is lower case in the closing of the entity declaration.

**Violation**

.. code-block:: vhdl

   end ENTITY FIFO;

**Fix**

.. code-block:: vhdl

   end entity FIFO;

entity_015
##########

This rule checks for the keyword **entity** in the **end entity** statement.

**Violation**

.. code-block:: vhdl

   end FIFO;

   end;

**Fix**

.. code-block:: vhdl

   end entity FIFO;

   end entity;

entity_016
##########

This rule checks for blank lines above the **end entity** keywords.

**Violation**

.. code-block:: vhdl

       WR_EN : in    std_logic;
       RD_EN : in    std_logic
     );

  
   end entity FIFO;


**Fix**

.. code-block:: vhdl

       WR_EN : in    std_logic;
       RD_EN : in    std_logic
     );   
   end entity FIFO;

entity_017
##########

This rule checks for alignment of the :'s in for every port in the entity.

**Violation**

.. code-block:: vhdl

       WR_EN : in    std_logic;
       RD_EN : in    std_logic;
       OVERLFLOW : out   std_logic;

**Fix**

.. code-block:: vhdl

       WR_EN     : in    std_logic;
       RD_EN     : in    std_logic;
       OVERLFLOW : out   std_logic;

entity_018
##########

This rule checks for alignment of inline comments in the entity

**Violation**

.. code-block:: vhdl

       WR_EN     : in    std_logic;      -- Wrte enable
       RD_EN     : in    std_logic; -- Read enable
       OVERLFLOW : out   std_logic;   -- FIFO has overflowed

**Fix**

.. code-block:: vhdl

       WR_EN     : in    std_logic;      -- Wrte enable
       RD_EN     : in    std_logic;      -- Read enable
       OVERLFLOW : out   std_logic;      -- FIFO has overflowed

entity_019
##########

This rule checks for the entity name in the **end entity** statement.

**Violation**

.. code-block:: vhdl

   end entity;

**Fix**

.. code-block:: vhdl

   end entity ENTITY_NAME;

