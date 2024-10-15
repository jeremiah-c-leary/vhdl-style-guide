.. include:: includes.rst

Subtype Rules
-------------

subtype_001
###########

|phase_4| |error| |indent|

This rule checks for indentation of the **subtype** keyword.

**Violation**

.. code-block:: vhdl

   architecture rtl of fifo is

        subtype read_size is range 0 to 9;
   subtype write_size is range 0 to 9;

   begin

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

     subtype read_size is range 0 to 9;
     subtype write_size is range 0 to 9;

   begin


subtype_002
###########

|phase_6| |error| |case|

This rule checks for consistent capitalization of subtype names.

**Violation**

.. code-block:: vhdl

   subtype read_size is range 0 to 9;
   subtype write_size is range 0 to 9;

   signal read  : READ_SIZE;
   signal write : write_size;

   constant read_sz  : read_size := 8;
   constant write_sz : WRITE_size := 1;


**Fix**

.. code-block:: vhdl

   subtype read_size is range 0 to 9;
   subtype write_size is range 0 to 9;

   signal read  : read_size;
   signal write : write_size;

   constant read_sz  : read_size := 8;
   constant write_sz : write_size := 1;

subtype_003
###########

This rule was deprecated and replaced with rules:

* `function_015 <function_rules.html#function-015>`_
* `package_019 <package_rules.html#package-019>`_
* `procedure_010 <procedure_rules.html#procedure-010>`_
* `architecture_029 <architecture_rules.html#architecture-029>`_

subtype_004
###########

|phase_7| |disabled| |error| |unfixable| |naming|

This rule checks for valid prefixes in subtype identifiers.
The default new subtype prefix is *st_*.

|configuring_prefix_and_suffix_rules_link|

**Violation**

.. code-block:: vhdl

   subtype my_subtype is range 0 to 9;

**Fix**

.. code-block:: vhdl

   subtype st_my_subtype is range 0 to 9;

subtype_005
###########

|phase_1| |error| |structure|

This rule checks the identifier is on the same line as the **subtype** keyword.

**Violation**

.. code-block:: vhdl

   subtype
   st_counter is

**Fix**

.. code-block:: vhdl

   subtype st_counter
   is

subtype_006
###########

|phase_1| |error| |structure|

This rule checks the **is** keyword is on the same line as the identifier.

**Violation**

.. code-block:: vhdl

   subtype st_counter
   is

**Fix**

.. code-block:: vhdl

   subtype st_counter is

subtype_100
###########

|phase_2| |disabled| |error| |whitespace|

This rule checks for a single space before the identifier.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   subtype         my_subtype is range 0 to 9;

**Fix**

.. code-block:: vhdl

   subtype my_subtype is range 0 to 9;

subtype_101
###########

|phase_2| |error| |whitespace|

This rule checks for a single space before the **is** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   subtype counter    is unsigned(4 downto 0);

**Fix**

.. code-block:: vhdl

   subtype counter is unsigned(4 downto 0);

subtype_102
###########

|phase_2| |error| |whitespace|

This rule checks for a single space after the **is** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   subtype counter is     unsigned(4 downto 0);

**Fix**

.. code-block:: vhdl

   subtype counter is unsigned(4 downto 0);

subtype_200
###########

|phase_3| |disabled| |error| |blank_line|

This rule checks for a blank line below a **subtype** declaration unless there is another **subtype** declaration.

|configuring_blank_lines_link|

**Violation**

.. code-block:: vhdl

   subtype counter_t is unsigned(4 downto 0);
   subtype counter is unsigned(4 downto 0);
   constant width : integer := 32;

**Fix**

.. code-block:: vhdl

   subtype counter_t is unsigned(4 downto 0);
   subtype counter is unsigned(4 downto 0);

   constant width : integer := 32;

subtype_201
###########

|phase_3| |error| |blank_line|

This rule checks for blank lines or comments above the **subtype** declaration.

|configuring_previous_line_rules_link|

**Violation**

.. code-block:: vhdl

   signal wr_en : std_logic;
   subtype counter is unsigned(4 downto 0);

**Fix**

.. code-block:: vhdl

   signal wr_en : std_logic;

   subtype counter is unsigned(4 downto 0);

subtype_202
###########

|phase_3| |error| |blank_line|

This rule checks for a blank line below the **subtype** declaration.

|configuring_blank_lines_link|

**Violation**

.. code-block:: vhdl

   subtype counter is unsigned(4 downto 0);
   signal sm : state_machine;

**Fix**

.. code-block:: vhdl

   subtype counter is unsigned(4 downto 0);

   signal sm : state_machine;

subtype_500
###########

|phase_6| |error| |case| |case_keyword|

This rule checks the **subtype** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   SUBTYPE interface is record
   Subtype interface is record
   subtype interface is record

**Fix**

.. code-block:: vhdl

   subtype interface is record
   subtype interface is record
   subtype interface is record

subtype_501
###########

|phase_6| |error| |case| |case_name|

This rule checks the identifier has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   subtype INTERFACE is record
   subtype Interface is record
   subtype interface is record

**Fix**

.. code-block:: vhdl

   subtype interface is record
   subtype interface is record
   subtype interface is record

subtype_502
###########

|phase_6| |error| |case| |case_keyword|

This rule checks the **is** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   subtype interface IS record
   subtype interface Is record
   subtype interface is record

**Fix**

.. code-block:: vhdl

   subtype interface is record
   subtype interface is record
   subtype interface is record

subtype_600
###########

|phase_7| |disabled| |error| |unfixable| |naming|

This rule checks for valid suffixes in subtype identifiers.
The default new subtype suffix is *_st*.

|configuring_prefix_and_suffix_rules_link|

**Violation**

.. code-block:: vhdl

   subtype my_subtype is range 0 to 9;

**Fix**

.. code-block:: vhdl

   subtype my_subtype_st is range 0 to 9;
