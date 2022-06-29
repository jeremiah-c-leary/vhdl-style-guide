.. include:: includes.rst

Signal Rules
------------

signal_001
##########

|phase_4| |error| |indent|

This rule checks the indent of signal declarations.

**Violation**

.. code-block:: vhdl

   architecture rtl of fifo is

   signal wr_en : std_logic;
        signal rd_en : std_logic;

   begin

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

     signal wr_en : std_logic;
     signal rd_en : std_logic;

   begin

signal_002
##########

|phase_6| |error| |case| |case_keyword|

This rule checks the **signal** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   SIGNAL wr_en : std_logic;

**Fix**

.. code-block:: vhdl

   signal wr_en : std_logic;

signal_003
##########

This rule was depricated and replaced with rules:

* `function_015 <function_rules.html#function-015>`_
* `package_019 <package_rules.html#package-019>`_
* `procedure_010 <procedure_rules.html#procedure-010>`_
* `architecture_029 <architecture_rules.html#architecture-029>`_

signal_004
##########

|phase_6| |error| |case| |case_name|

This rule checks the signal name has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   signal WR_EN : std_logic;

**Fix**

.. code-block:: vhdl

   signal wr_en : std_logic;

signal_005
##########

|phase_2| |error| |whitespace|

This rule checks for a single space after the colon.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   signal wr_en :    std_logic;
   signal rd_en :std_logic;

**Fix**

.. code-block:: vhdl

   signal wr_en : std_logic;
   signal rd_en : std_logic;

signal_006
##########

|phase_2| |error| |whitespace|

This rule checks for at least a single space before the colon.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   signal wr_en: std_logic;
   signal rd_en   : std_logic;

**Fix**

.. code-block:: vhdl

   signal wr_en : std_logic;
   signal rd_en   : std_logic;

signal_007
##########

|phase_1| |error| |structure|

This rule checks for default assignments in signal declarations.

.. NOTE:: This rule requires the user to remove the default assignments.

**Violation**

.. code-block:: vhdl

   signal wr_en : std_logic := '0';

**Fix**

.. code-block:: vhdl

   signal wr_en : std_logic;

signal_008
##########

|phase_7| |disabled| |error| |naming|

This rule checks for valid prefixes on signal identifiers.
Default signal prefix is *s\_*.

|configuring_prefix_and_suffix_rules_link|

**Violation**

.. code-block:: vhdl

   signal wr_en : std_logic;
   signal rd_en : std_logic;

**Fix**

.. code-block:: vhdl

   signal s_wr_en : std_logic;
   signal s_rd_en : std_logic;

signal_010
##########

The function of this rule has been moved to rule ieee_500.

signal_011
##########

The function of this rule has been superceeded by the following rules:

* ieee_500
* subtype_002
* type_014

signal_012
##########

|phase_5| |error| |alignment|

This rule checks multiple signal declarations on a single line are column aligned.

.. NOTE::
    This rule will only cover two signals on a single line.

**Violation**

.. code-block:: vhdl

   signal wr_en, wr_en_f             : std_logic;
   signal rd_en_f, rd_en             : std_logic;
   signal chip_select, chip_select_f : t_user_defined_type;

**Fix**

.. code-block:: vhdl

   signal wr_en,       wr_en_f       : std_logic;
   signal rd_en_f,     rd_en         : std_logic;
   signal chip_select, chip_select_f : t_user_defined_type;

signal_014
##########

|phase_6| |error| |case|

This rule checks for consistent capitalization of signal names.

**Violation**

.. code-block:: vhdl

   architecture rtl of entity1 is

     signal sig1 : std_logic;
     signal sig2 : std_logic;

   begin

     proc_name : process (siG2) is
     begin

       siG1 <= '0';

       if (SIG2 = '0') then
         sIg1 <= '1';
       elisif (SiG2 = '1') then
         SIg1 <= '0';
       end if;

     end process proc_name;

   end architecture rtl;

**Fix**

.. code-block:: vhdl

   architecture rtl of entity1 is

     signal sig1 : std_logic;
     signal sig2 : std_logic;

     proc_name : process (sig2) is
     begin

       sig1 <= '0';

       if (sig2 = '0') then
         sig1 <= '1';
       elisif (sig2 = '1') then
         sig1 <= '0';
       end if;

     end process proc_name;

   end architecture rtl;

signal_015
##########

|phase_1| |error| |structure|

This rule checks for multiple signal names defined in a single signal declaration.
By default, this rule will only flag more than two signal declarations.

|configuring_number_of_signals_in_signal_declaration_link|

**Violation**

.. code-block:: vhdl

   signal sig1, sig2
     sig3, sig4,
     sig5
     : std_logic;

**Fix**

.. code-block:: vhdl

   signal sig1 : std_logic;
   signal sig2 : std_logic;
   signal sig3 : std_logic;
   signal sig4 : std_logic;
   signal sig5 : std_logic;

signal_016
##########

This rule was depricated and replaced with rule:

* `signal_017 <signal_rules.html#signal-017>`_

signal_017
##########

|phase_1| |error| |structure|

This rule checks the structure of signal constraints.

|configuring_multiline_constraint_rules_link|

.. NOTE:: The indenting of multiline signal constraints is handled by the rule `signal_400 <signal_rules.html#signal-400>`_.

**Violation**

.. code-block:: vhdl

   signal sig_a : my_record(element1(7 downto 0), element2(3 downto 0));

**Fix**

.. code-block:: vhdl

   signal sig_a : my_record(
       element1(7 downto 0),
       element2(3 downto 0)
     );

signal_400
##########

|phase_5| |error| |alignment|

This rule checks alignment of multiline constraints in signal declarations.

|configuring_multiline_indent_rules_link|

**Violation**

.. code-block:: vhdl

   signal sig_a : my_record(
            element1(7 downto 0),
   element2(3 downto 0)
           );

**Fix**

.. code-block:: vhdl

   signal sig_a : my_record(
       element1(7 downto 0),
       element2(3 downto 0)
     );

signal_600
##########

|phase_7| |disabled| |error| |naming|

This rule checks for valid suffixes on signal identifiers.
Default signal suffix is *\_s*.

|configuring_prefix_and_suffix_rules_link|

**Violation**

.. code-block:: vhdl

   signal wr_en : std_logic;
   signal rd_en : std_logic;

**Fix**

.. code-block:: vhdl

   signal wr_en_s : std_logic;
   signal rd_en_s : std_logic;

