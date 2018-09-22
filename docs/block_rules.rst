Architecture Rules
------------------

block_001
#########

This rule checks for blank spaces before the **block** keyword.

**Violation**

.. code-block:: vhdl

     block RTL of FIFO is
   begin

**Fix**

.. code-block:: vhdl

   block RTL of FIFO is
   begin

block_002
#########

This rule checks for a single space between **block**, **of**, and **is** keywords.

**Violation**

.. code-block:: vhdl

   block  RTL  of    FIFO   is

**Fix**

.. code-block:: vhdl

   block RTL of FIFO is

block_003
#########

This rule check for a blank line above the **block** declaration.

**Violation**

.. code-block:: vhdl

   library ieee;
   block RTL of FIFO is

**Fix**

.. code-block:: vhdl

   library ieee;

   block RTL of FIFO is

block_004
#########

This rule checks the **block** keyword is lower case in the declaration.

**Violation**

.. code-block:: vhdl

   ARCHITECTURE RTL of FIFO is

.. code-block:: vhdl

   block RTL of FIFO is

block_005
#########

This rule checks the **of** keyword is on the same line as the **block** keyword.

**Violation**

.. code-block:: vhdl

   block RTL
     of FIFO is

**Fix**

.. code-block:: vhdl

   block RTL of FIFO is

block_006
#########

This rule checks the **is** keyword is on the same line as the **block** keyword.

**Violation**

.. code-block:: vhdl

   block RTL of FIFO
     is

   block RTL of FIFO

**Fix**

.. code-block:: vhdl

   block RTL of FIFO is

   block RTL of FIFO is

block_007
#########

This rule checks for spaces before the **begin** keyword.

**Violation**

.. code-block:: vhdl

   block RTL of FIFO is
     begin

**Fix**

.. code-block:: vhdl

   block RTL of FIFO is
   begin

block_008
#########

This rule checks for spaces before the **end block** keywords.

**Violation**

.. code-block:: vhdl

   block RTL of FIFO is
   begin
     end block

**Fix**

.. code-block:: vhdl

   block RTL of FIFO is
   begin
   end block

block_009
#########

This rule checks the **end** and **block** keywords are lower case.

**Violation**

.. code-block:: vhdl

   END block;

   end Architecture;

**Fix**

.. code-block:: vhdl

   end block;

   end block;

block_010
#########

This rule checks for the keyword **block** in the **end block** statement.
It is clearer to the reader to state what is ending.

**Violation**

.. code-block:: vhdl

   end ARCHITECTURE_NAME;

**Fix**

.. code-block:: vhdl

   end block ARCHITECTURE_NAME;

block_011
#########

This rule checks the block name is upper case in the **end block** statement.

**Violation**

.. code-block:: vhdl

   end block block_name;

**Fix**

.. code-block:: vhdl

   end block ARCHITECTURE_NAME;

block_012
#########

This rule checks for a single space between **end** and **block** keywords.

**Violation**

.. code-block:: vhdl

   end    block ARCHITECTURE_NAME;

**Fix**

.. code-block:: vhdl

   end block ARCHITECTURE_NAME;
 
block_013
#########

This rule checks the block name is upper case in the block declaration.

**Violation**

.. code-block:: vhdl

   block rtl of FIFO is

**Fix**

.. code-block:: vhdl

   block RTL of FIFO is


block_014
#########

This rule checks the entity name is upper case in the block declaration.

**Violation**

.. code-block:: vhdl

   block RTL of fifo is

**Fix**

.. code-block:: vhdl

   block RTL of FIFO is

block_015
#########

This rule check for a blank line below the block declaration.

**Violation**

.. code-block:: vhdl

   block RTL of FIFO is
     signal wr_en : std_logic;
   begin

**Fix**

.. code-block:: vhdl

   block RTL of FIFO is

     signal wr_en : std_logic;
   begin


block_016
#########

This rule checks for a blank line above the **begin** keyword.

**Violation**

.. code-block:: vhdl

   block RTL of FIFO is

     signal wr_en : std_logic;
   begin

**Fix**

.. code-block:: vhdl

   block RTL of FIFO is

     signal wr_en : std_logic;

   begin


block_017
#########

This rule checks for a blank line below the **begin** keyword.

**Violation**

.. code-block:: vhdl

   begin
     wr_en <= '0';

**Fix**

.. code-block:: vhdl

   begin

     wr_en <= '0';

block_018
#########

This rule checks for a blank line above the **end block** declaration.

**Violation**

.. code-block:: vhdl

     rd_en <= '1';
   end block RTL;

**Fix**

.. code-block:: vhdl

     rd_en <= '1';

   end block RTL;

block_019
#########

This rule checks the **of** keyword is lower case in the block declaration.

**Violation**

.. code-block:: vhdl

   block RTL OF FIFO is

**Fix**

.. code-block:: vhdl

   block RTL of FIFO is

block_020
#########

This rule checks the **is** keyword is lower case in the block declaration.

**Violation**

.. code-block:: vhdl

   block RTL of FIFO IS

**Fix**

.. code-block:: vhdl

   block RTL of FIFO is

block_021
#########

This rule checks the **begin** keyword is lower case.

**Violation**

.. code-block:: vhdl

   block RTL of FIFO is
   BEGIN

**Fix**

.. code-block:: vhdl

   block RTL of FIFO is
   begin
 
block_022
#########

This rule checks for a single space before the entity name in the end block declaration.

**Violation**

.. code-block:: vhdl

   end block    FIFO;

**Fix**

.. code-block:: vhdl

   end block FIFO;
 
block_023
#########

This rule ensures the inline comments are aligned between the block declaration and the **begin** keyword.

**Violation**

.. code-block:: vhdl

   block RTL of FIFO is

     signal wr_en : std_logic;   -- Enables writes to FIFO
     signal rd_en : std_logic;  -- Enables reads from FIFO
     signal overflow : std_logic;    -- Indicates the FIFO has overflowed when asserted

   begin

**Fix**

.. code-block:: vhdl

   block RTL of FIFO is

     signal wr_en : std_logic;       -- Enables writes to FIFO
     signal rd_en : std_logic;       -- Enables reads from FIFO
     signal overflow : std_logic;    -- Indicates the FIFO has overflowed when asserted

   begin
 
block_024
#########

This rule checks for the block name in the **end block** statement.
It is clearer to the reader to state which block the end statement is closing.

**Violation**

.. code-block:: vhdl

   end block;

**Fix**

.. code-block:: vhdl

   end block ARCHITECTURE_NAME;

