Generic Rules
-------------

generic_001
###########

This rule checks for blank lines above the **generic** keyword.

**Violation**

.. code-block:: vhdl

   entity FIFO is



     generic (

**Fix**

.. code-block:: vhdl

   entity FIFO is
     generic (

generic_002
###########

This rule checks the indent of the **generic** keyword.

**Violation**

.. code-block:: vhdl

   entity FIFO is
        generic (

   entity FIFO is
   generic (

**Fix**

.. code-block:: vhdl

   entity FIFO is
     generic (

   entity FIFO is
     generic (

generic_003
###########

This rule checks for a single space between the **generic** keyword and the (.

**Violation**

.. code-block:: vhdl

   generic    (

   generic(

**Fix**

.. code-block:: vhdl

   generic (

   generic (

generic_004
###########

This rule checks the indent of generic declarations.

**Violation**

.. code-block:: vhdl

   generic (
   WIDTH : integer := 32;
          DEPTH : integer := 512
   )

**Fix**

.. code-block:: vhdl

   generic (
     WIDTH : integer := 32;
     DEPTH : integer := 512
   )

generic_005
###########

This rule checks for a single space after the colon in a generic declaration.

**Violation**

.. code-block:: vhdl

   WIDTH :integer := 32;

**Fix**

.. code-block:: vhdl

   WIDTH : integer := 32;

generic_006
###########

This rule checks for a single space after the default assignment.

**Violation**

.. code-block:: vhdl

   WIDTH : integer :=32;
   DEPTH : integer :=     512;

**Fix**

.. code-block:: vhdl

   WIDTH : integer := 32;
   DEPTH : integer := 512;

generic_007
###########

This rule checks the generic name is uppercase.

**Violation**

.. code-block:: vhdl

   width : integer := 32;

**Fix**

.. code-block:: vhdl

   WIDTH : integer := 32;

generic_008
###########

This rule checks the indent of the closing parenthesis.

**Violation**

.. code-block:: vhdl

   DEPTH : integer := 512
   );

**Fix**

.. code-block:: vhdl

     DEPTH : integer := 512
   );

generic_009
###########

This rule checks the **generic** keyword is lowercase.

**Violation**

.. code-block:: vhdl

   GENERIC (

**Fix**

.. code-block:: vhdl

   generic (

generic_010
###########

This rule checks the closing parenthesis is on a line by itself.

**Violation**

.. code-block:: vhdl

   DEPTH : integer := 512);

**Fix**

.. code-block:: vhdl

     DEPTH : integer := 512
   );

generic_012
###########

This rule checks the alignment of :'s for every generic.

**Violation**

.. code-block:: vhdl

   ADDRESS_WIDTH : integer := 10;
   DATA_WIDTH : integer := 32;
   DEPTH : integer := 512;

**Fix**

.. code-block:: vhdl

   ADDRESS_WIDTH : integer := 10;
   DATA_WIDTH    : integer := 32;
   DEPTH         : integer := 512;

generic_013
###########

This rule checks for the **generic** keyword on the same line as a generic declaration.

**Violation**

.. code-block:: vhdl

   generic (DEPTH : integer := 512;

**Fix**

.. code-block:: vhdl

   generic (
     DEPTH : integer := 512;

generic_014
###########

This rule checks for at least a single space before the :.

**Violation**

.. code-block:: vhdl

   ADDRESS_WIDTH: integer := 10;
   DATA_WIDTH : integer := 32;
   DEPTH: integer := 512;

**Fix**

.. code-block:: vhdl

   ADDRESS_WIDTH : integer := 10;
   DATA_WIDTH : integer := 32;
   DEPTH : integer := 512;

generic_015
###########

This rule checks the alignment of the **:=** operator in generic declarations.

**Violation**

.. code-block:: vhdl

   ADDRESS_WIDTH : integer    := 10;
   DATA_WIDTH    : integer := 32;
   DEPTH         : integer  := 512;

**Fix**

.. code-block:: vhdl

   ADDRESS_WIDTH : integer    := 10;
   DATA_WIDTH    : integer    := 32;
   DEPTH         : integer    := 512;

generic_016
###########

This rule checks for multiple generics defined on a single line.

**Violation**

.. code-block:: vhdl

  generic (
    WIDTH : std_logic := '0';DEPTH : std_logic := '1'
  );

**Fix**

.. code-block:: vhdl

  generic (
    WIDTH : std_logic := '0';
    DEPTH : std_logic := '1'
  );

generic_017
###########

This rule checks the generic type is lowercase if it is a VHDL keyword.

**Violation**

.. code-block:: vhdl

  generic (
    WIDTH : STD_LOGIC := '0';
    DEPTH : Std_logic := '1'
  );


**Fix**

.. code-block:: vhdl

  generic (
    WIDTH : std_logic := '0';
    DEPTH : std_logic := '1'
  );

generic_018
###########

This rule checks the **generic** keyword is on the same line as the (.

**Violation**

.. code-block:: vhdl

  generic 
   (

**Fix**

.. code-block:: vhdl

  generic (

