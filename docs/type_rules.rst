.. include:: icons.rst

Type Rules
----------

type_001
########

|phase_4| |error| |indent|

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

|phase_6| |error|

This rule checks the **type** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   TYPE state_machine is (idle, write, read, done);

**Fix**

.. code-block:: vhdl

   type state_machine is (idle, write, read, done);

type_003
########

This rule was depricated and replaced with rules:

* `function_015 <function_rules.html#function-015>`_
* `package_019 <package_rules.html#package-019>`_
* `procedure_010 <procedure_rules.html#procedure-010>`_
* `architecture_029 <architecture_rules.html#architecture-029>`_

type_004
########

|phase_6| |error|

This rule checks the type identifier has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   type STATE_MACHINE is (idle, write, read, done);

**Fix**

.. code-block:: vhdl

   type state_machine is (idle, write, read, done);

type_005
########

|phase_4| |error| |indent|

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

|phase_2| |error| |whitespace|

This rule checks for a single space before the **is** keyword.

**Violation**

.. code-block:: vhdl

   type state_machine    is (idle, write, read, done);

**Fix**

.. code-block:: vhdl

   type state_machine is (idle, write, read, done);

type_007
########

|phase_2| |error| |whitespace|

This rule checks for a single space after the **is** keyword.

**Violation**

.. code-block:: vhdl

   type state_machine is     (idle, write, read, done);

**Fix**

.. code-block:: vhdl

   type state_machine is (idle, write, read, done);

type_008
########

|phase_1| |error|

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

|phase_1| |error|

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

|phase_3| |error| |blank_line|

This rule checks for blank lines or comments above the **type** declaration.

Refer to `Configuring Previous Line Rules <configuring.html#configuring-previous-line-rules>`_ for options.

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

|phase_3| |error| |blank_line|

This rule checks for a blank line below the **type** declaration.

Refer to the section `Configuring Blank Lines <configuring.html#configuring-blank-lines>`_ for options regarding comments.

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

|phase_4| |error| |indent|

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

|phase_6| |error|

This rule checks the **is** keyword in type definitions has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

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

|phase_6| |error|

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
########

|phase_7| |disabled| |error|

This rule checks for valid prefixes in user defined type identifiers.
The default new type prefix is *t\_*.

Refer to the section `Configuring Prefix and Suffix Rules <configuring.html#configuring-prefix-and-suffix-rules>`_ for information on changing the allowed prefixes.

**Violation**

.. code-block:: vhdl

   type my_type is range -5 to 5 ;

**Fix**

.. code-block:: vhdl

   type t_my_type is range -5 to 5 ;

type_016
########

|phase_4| |error| |indent|

This rule checks the indent of the closing parenthesis on multiline types.

**Violation**

.. code-block:: vhdl

   architecture rtl of fifo is

     type state_machine is (
       idle, write, read, done
       );

   begin

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

     type state_machine is (
       idle, write, read, done
     );

   begin

type_400
########

|phase_5| |error|

This rule checks the colons are in the same column for all elements in the block declarative part.

Refer to the section `Configuring Keyword Alignment Rules <configuring.html#configuring-keyword-alignment-rules>`_ for information on changing the configurations.

**Violation**

.. code-block:: vhdl

   type t_some_record is record
     element_1 : natural;
     some_other_element : natural;
     yet_another_element : natural;
   end record;

**Fix**

.. code-block:: vhdl

   type t_some_record is record
     element_1           : natural;
     some_other_element  : natural;
     yet_another_element : natural;
   end record;

type_600
########

|phase_7| |disabled| |error|

This rule checks for valid suffixes in user defined type identifiers.
The default new type suffix is *\_t*.

Refer to the section `Configuring Prefix and Suffix Rules <configuring.html#configuring-prefix-and-suffix-rules>`_ for information on changing the allowed suffixes.

**Violation**

.. code-block:: vhdl

   type my_type is range -5 to 5 ;

**Fix**

.. code-block:: vhdl

   type my_type_t is range -5 to 5 ;
