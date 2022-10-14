.. include:: includes.rst

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

|phase_6| |error| |case| |case_keyword|

This rule checks the **type** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   TYPE state_machine is (idle, write, read, done);

**Fix**

.. code-block:: vhdl

   type state_machine is (idle, write, read, done);

type_003
########

This rule was deprecated and replaced with rules:

* `function_015 <function_rules.html#function-015>`_
* `package_019 <package_rules.html#package-019>`_
* `procedure_010 <procedure_rules.html#procedure-010>`_
* `architecture_029 <architecture_rules.html#architecture-029>`_

type_004
########

|phase_6| |error| |case| |case_name|

This rule checks the type identifier has proper case.

|configuring_uppercase_and_lowercase_rules_link|

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

|configuring_whitespace_rules_link|

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

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   type state_machine is     (idle, write, read, done);

**Fix**

.. code-block:: vhdl

   type state_machine is (idle, write, read, done);

type_008
########

|phase_1| |error| |structure|

This rule checks the closing parenthesis of multiline enumerated types is on its own line.

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

|phase_1| |error| |structure|

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

|configuring_previous_line_rules_link|

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

|configuring_blank_lines_link|

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

|phase_6| |error| |case| |case_keyword|

This rule checks the **is** keyword in type definitions has proper case.

|configuring_uppercase_and_lowercase_rules_link|

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

|phase_6| |error| |case|

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

|phase_7| |disabled| |error| |naming|

This rule checks for valid prefixes in user defined type identifiers.
The default new type prefix is *t\_*.

|configuring_prefix_and_suffix_rules_link|

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

type_017
########

|phase_1| |error| |structure|

This rule checks the identifier is on the same line as the type keyword.

**Violation**

.. code-block:: vhdl

   type
   t_record is

**Fix**

.. code-block:: vhdl

   type t_record
   is

type_018
########

|phase_1| |error| |structure|

This rule checks the **is** keyword is on the same line as the identifier.

**Violation**

.. code-block:: vhdl

   type t_record
   is

**Fix**

.. code-block:: vhdl

   type t_record is

type_400
########

|phase_5| |error| |alignment|

This rule checks the colons are in the same column for all elements in the block declarative part.

|configuring_keyword_alignment_rules_link|

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

|phase_7| |disabled| |error| |naming|

This rule checks for valid suffixes in user defined type identifiers.
The default new type suffix is *\_t*.

|configuring_prefix_and_suffix_rules_link|

**Violation**

.. code-block:: vhdl

   type my_type is range -5 to 5 ;

**Fix**

.. code-block:: vhdl

   type my_type_t is range -5 to 5 ;

