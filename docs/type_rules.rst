Type Rules
----------

type_001
########

This rule checks the indent of the **type** declaration.

**Violation**

.. code-block:: vhdl

   architecture rtl of fifo is

       type state_machine is (idle, write, read, done);

   begin

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

     type state_machine is (idle, write, read, done);

   begin

type_002
########

This rule checks the **type** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   TYPE state_machine is (idle, write, read, done);

**Fix**

.. code-block:: vhdl

   type state_machine is (idle, write, read, done);

type_003
########

This rule was depricated and replaced with rules:  function_015, package_019, procedure_010, architecture_029 and process_037.

type_004
########

This rule checks the type name has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   type STATE_MACHINE is (idle, write, read, done);

**Fix**

.. code-block:: vhdl

   type state_machine is (idle, write, read, done);

type_005
########

This rule checks the indent of multiline enumerated types.

**Violation**

.. code-block:: vhdl

   type state_machine is (
   idle,
     write,
   read,
      done);

**Fix**

.. code-block:: vhdl

   type state_machine is (
     idle,
     write,
     read,
     done);

type_006
########

This rule checks for a single space before the **is** keyword.

**Violation**

.. code-block:: vhdl

   type state_machine    is (idle, write, read, done);

**Fix**

.. code-block:: vhdl

   type state_machine is (idle, write, read, done);

type_007
########

This rule checks for a single space after the **is** keyword.

**Violation**

.. code-block:: vhdl

   type state_machine is     (idle, write, read, done);

**Fix**

.. code-block:: vhdl

   type state_machine is (idle, write, read, done);

type_008
########

This rule checks the closing parenthesis of multiline enumerated types is on it's own line.

**Violation**

.. code-block:: vhdl

   type state_machine is (
     idle,
     write,
     read,
     done);

**Fix**

.. code-block:: vhdl

   type state_machine is (
     idle,
     write,
     read,
     done
   );

type_009
########

This rule checks for an enumerate type after the open parenthesis on multiline enumerated types.

**Violation**

.. code-block:: vhdl

   type state_machine is (idle,
     write,
     read,
     done
   );

**Fix**

.. code-block:: vhdl

   type state_machine is (
     idle,
     write,
     read,
     done
   );

type_010
########

This rule checks for a blank line above the **type** declaration.

**Violation**

.. code-block:: vhdl

   signal wr_en : std_logic;
   type state_machine is (idle, write, read, done);

**Fix**

.. code-block:: vhdl

   signal wr_en : std_logic;

   type state_machine is (idle, write, read, done);

type_011
########

This rule checks for a blank line below the **type** declaration.

**Violation**

.. code-block:: vhdl

   type state_machine is (idle, write, read, done);
   signal sm : state_machine;

**Fix**

.. code-block:: vhdl

   type state_machine is (idle, write, read, done);

   signal sm : state_machine;

type_012
########

This rule checks the indent of record elements in record type declarations.

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

This rule checks the **is** keyword in type definitions has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

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

type_014
########

This rule checks for consistent capitalization of type names.

**Violation**

.. code-block:: vhdl

   type state_machine is (idle, write, read, done);

   signal sm : State_Machine;

**Fix**

.. code-block:: vhdl

   type state_machine is (idle, write, read, done);

   signal sm : state_machine;

type_015
##########

This rule checks for valid prefixes in user defined type identifiers.
The default new type prefix is *t\_*.

Refer to the section `Configuring Prefix and Suffix Rules <configuring_prefix_suffix.html>`_ for information on changing the allowed prefixes.

**Violation**

.. code-block:: vhdl

   type my_type is range -5 to 5 ;

**Fix**

.. code-block:: vhdl

   type t_my_type is range -5 to 5 ;
