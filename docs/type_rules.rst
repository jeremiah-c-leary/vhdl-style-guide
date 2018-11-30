Type Rules
----------

type_001
########

This rule checks the indent of the **type** declaration.

**Violation**

.. code-block:: vhdl

   architecture RTL of FIFO is

       type state_machine is (IDLE, WRITE, READ, DONE);

   begin

**Fix**

.. code-block:: vhdl

   architecture RTL of FIFO is

     type state_machine is (IDLE, WRITE, READ, DONE);

   begin

type_002
########

This rule checks the **type** keyword is lowercase.

**Violation**

.. code-block:: vhdl

   TYPE state_machine is (IDLE, WRITE, READ, DONE);

**Fix**

.. code-block:: vhdl

   type state_machine is (IDLE, WRITE, READ, DONE);

type_003
########

This rule checks for a single space after the **type** keyword.

**Violation**

.. code-block:: vhdl

   type   state_machine is (IDLE, WRITE, READ, DONE);

**Fix**

.. code-block:: vhdl

   type state_machine is (IDLE, WRITE, READ, DONE);

type_004
########

This rule checks the type name is lowercase.

**Violation**

.. code-block:: vhdl

   type STATE_MACHINE is (IDLE, WRITE, READ, DONE);

**Fix**

.. code-block:: vhdl

   type state_machine is (IDLE, WRITE, READ, DONE);

type_005
########

This rule checks the indent of multiline enumerated types.

**Violation**

.. code-block:: vhdl

   type state_machine is (
   IDLE,
     WRITE,
   READ,
      DONE);

**Fix**

.. code-block:: vhdl

   type state_machine is (
     IDLE,
     WRITE,
     READ,
     DONE);

type_006
########

This rule checks for a single space before the **is** keyword.

**Violation**

.. code-block:: vhdl

   type state_machine    is (IDLE, WRITE, READ, DONE);

**Fix**

.. code-block:: vhdl

   type state_machine is (IDLE, WRITE, READ, DONE);

type_007
########

This rule checks for a single space after the **is** keyword.

**Violation**

.. code-block:: vhdl

   type state_machine is     (IDLE, WRITE, READ, DONE);

**Fix**

.. code-block:: vhdl

   type state_machine is (IDLE, WRITE, READ, DONE);

type_008
########

This rule checks the closing parenthesis of multiline enumerated types is on it's own line.

**Violation**

.. code-block:: vhdl

   type state_machine is (
     IDLE,
     WRITE,
     READ,
     DONE);

**Fix**

.. code-block:: vhdl

   type state_machine is (
     IDLE,
     WRITE,
     READ,
     DONE
   );

type_009
########

This rule checks for an enumerate type after the open parenthesis on multiline enumerated types.

**Violation**

.. code-block:: vhdl

   type state_machine is (IDLE,
     WRITE,
     READ,
     DONE
   );

**Fix**

.. code-block:: vhdl

   type state_machine is (
     IDLE,
     WRITE,
     READ,
     DONE
   );

type_010
########

This rule checks for a blank line above the **type** declaration.

**Violation**

.. code-block:: vhdl

   signal wr_en : std_logic;
   type state_machine is (IDLE, WRITE, READ, DONE);

**Fix**

.. code-block:: vhdl

   signal wr_en : std_logic;

   type state_machine is (IDLE, WRITE, READ, DONE);

type_011
########

This rule checks for a blank line below the **type** declaration.

**Violation**

.. code-block:: vhdl

   type state_machine is (IDLE, WRITE, READ, DONE);
   signal sm : state_machine;

**Fix**

.. code-block:: vhdl

   type state_machine is (IDLE, WRITE, READ, DONE);

   signal sm : state_machine;

type_012
########

This rule checks the indent of record elements in record types.

**Violation**

.. code-block:: vhdl

   type interface is record
     data : std_logic_vector(31 downto 0);
   chip_select : std_logic;
       wr_en : std_logic;
   end record;

**Fix**

.. code-block:: vhdl

   type interface is record
     data : std_logic_vector(31 downto 0);
     chip_select : std_logic;
     wr_en : std_logic;
   end record;

type_013
########

This rule checks the **is** keyword is lower case in type definitions.

**Violation**

.. code-block:: vhdl

   type interface IS record
   type interface Is record
   type interface is record

**Fix**

.. code-block:: vhdl

   type interface is record
   type interface is record
   type interface is record
