Constant Rules
--------------

constant_001
############

This rule checks the indent of a constant declaration.

**Violation**

.. code-block:: vhdl

   architecture RTL of FIFO is

   constant size : integer := 1;
       constant width : integer := 32

**Fix**

.. code-block:: vhdl

   architecture RTL of FIFO is

     constant size : integer := 1;
     constant width : integer := 32


constant_002
############

This rule checks the **constant** keyword is lowercase.

**Violation**

.. code-block:: vhdl

   CONSTANT size : integer := 1;

**Fix**

.. code-block:: vhdl

   constant size : integer := 1;

constant_003
############

This rule checks for a single space after the **constant** keyword.

**Violation**

.. code-block:: vhdl

   constant    size : integeri := 1;

**Fix**

.. code-block:: vhdl

   constant size : integer := 1;

constant_004
############

This rule checks the constant name is lower case.

**Violation**

.. code-block:: vhdl

   constant SIZE : integer := 1;

**Fix**

.. code-block:: vhdl

   constant size : integer := 1;

constant_005
############

This rule checks for a single space after the :.

**Violation**

.. code-block:: vhdl

   constant size  :integer := 1;
   constant wdith :     integer := 32;

**Fix**

.. code-block:: vhdl

   constant size  : integer := 1;
   constant width : integer := 32;

constant_006
############

This rule checks for at least a single space before the :.

**Violation**

.. code-block:: vhdl

   constant size: integer := 1;
   constant width     : integer := 32;

**Fix**

.. code-block:: vhdl

   constant size : integer := 1;
   constant width     : integer := 32;

constant_007
############

This rule checks the **:=** is on the same line at the **constant** keyword.

**Violation**

.. code-block:: vhdl

   constant size : integer
      := 1;

**Fix**

.. code-block:: vhdl

   constant size : integer := 1;

constant_009
############

This rule checks the :'s are in the same column for all constants in the architecture declarative region.

**Violation**

.. code-block:: vhdl

   constant size : integer := 1;
   constant width   : integer := 32

**Fix**

.. code-block:: vhdl

   constant size    : integer := 1;
   constant width   : integer := 32


constant_010
############

This rule checks for at least a single space before the := keyword in constant declarations.
Having a space makes it clearer where the assignment occurs on the line.

**Violation**

.. code-block:: vhdl

   constant size : integer:= 1;

**Fix**

.. code-block:: vhdl

   constant size : integer := 1;

constant_011
############

This rule checks the constant type is lowercase.

**Violation**

.. code-block:: vhdl

   constant size : INTEGER := 1;

**Fix**

.. code-block:: vhdl

   constant size : integer := 1;

constant_012
############

This rule checks the indent of multiline constants.

**Violation**

.. code-block:: vhdl

   constant rom : romq_type :=
   (
            0,
        65535,
        32768
     );

**Fix**

.. code-block:: vhdl

   constant rom : romq_type :=
   (
     0,
     65535,
     32768
   );

