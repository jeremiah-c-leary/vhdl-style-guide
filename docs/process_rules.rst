.. include:: includes.rst

Process Rules
-------------

process_001
###########

|phase_4| |error| |indent|

This rule checks the indent of the process declaration.

**Violation**

.. code-block:: vhdl

   architecture rtl of fifo is

   begin

   proc_a : process (rd_en, wr_en, data_in, data_out,

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

   begin

     proc_a : process (rd_en, wr_en, data_in, data_out,

process_002
###########

|phase_2| |error| |whitespace|

This rule checks for a single space after the **process** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   proc_a : process(rd_en, wr_en, data_in, data_out,

   proc_a : process    (rd_en, wr_en, data_in, data_out,

**Fix**

.. code-block:: vhdl

   proc_a : process (rd_en, wr_en, data_in, data_out,

   proc_a : process (rd_en, wr_en, data_in, data_out,

process_003
###########

|phase_4| |error| |indent|

This rule checks the indent of the **begin** keyword.

**Violation**

.. code-block:: vhdl

   proc_a : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is
     begin

**Fix**

.. code-block:: vhdl

   proc_a : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is
   begin

process_004
###########

|phase_6| |error| |case| |case_keyword|

This rule checks the **begin** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   proc_a : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is
   BEGIN

**Fix**

.. code-block:: vhdl

   proc_a : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is
   begin

process_005
###########

|phase_6| |error| |case| |case_keyword|

This rule checks the **process** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   proc_a : PROCESS (rd_en, wr_en, data_in, data_out,

**Fix**

.. code-block:: vhdl

   proc_a : process (rd_en, wr_en, data_in, data_out,

process_006
###########

|phase_4| |error| |indent|

This rule checks the indent of the **end process** keywords.

**Violation**

.. code-block:: vhdl

   proc_a : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is
   begin

     end process proc_a;

**Fix**

.. code-block:: vhdl

   proc_a : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is
   begin

   end process proc_a;

process_007
###########

|phase_2| |error| |whitespace|

This rule checks for a single space after the **end** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   end   process proc_a;

**Fix**

.. code-block:: vhdl

   end process proc_a;

process_008
###########

|phase_6| |error| |case| |case_keyword|

This rule checks the **end** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   END process proc_a;

**Fix**

.. code-block:: vhdl

   end process proc_a;

process_009
###########

|phase_6| |error| |case| |case_keyword|

This rule checks the **process** keyword has proper case in the **end process** line.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   end PROCESS proc_a;

**Fix**

.. code-block:: vhdl

   end process proc_a;

process_010
###########

|phase_1| |error| |structure|

This rule checks the **begin** keyword is on its own line.

**Violation**

.. code-block:: vhdl

   proc_a : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is begin

**Fix**

.. code-block:: vhdl

   proc_a : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is
   begin

process_011
###########

|phase_3| |error| |blank_line|

This rule checks for a blank line below the **end process** keyword.

|configuring_blank_lines_link|

**Violation**

.. code-block:: vhdl

   end process proc_a;
   wr_en <= wr_en;

**Fix**

.. code-block:: vhdl

   end process proc_a;

   wr_en <= wr_en;

process_012
###########

|phase_1| |error| |structure| |structure_optional|

This rule checks for the existence of the **is** keyword.

|configuring_optional_items_link|

**Violation**

.. code-block:: vhdl

   proc_a : process
   begin
   end process;

   proc_a : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    )
   begin
   end process;


**Fix**

.. code-block:: vhdl

   proc_a : process is
   begin
   end process;


   proc_a : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is
   begin
   end process;

process_013
###########

|phase_6| |error| |case| |case_keyword|

This rule checks the **is** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   proc_a : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) IS
   begin

**Fix**

.. code-block:: vhdl

   proc_a : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is
   begin

process_014
###########

|phase_2| |error| |whitespace|

This rule checks for a single space before the **is** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   proc_a : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    )     is
   begin

**Fix**

.. code-block:: vhdl

   proc_a : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is
   begin

process_015
###########

|phase_3| |error| |blank_line|

This rule checks for blank lines or comments above the **process** declaration.

|configuring_previous_line_rules_link|

The default style is :code:`no_code`.

**Violation**

.. code-block:: vhdl

   -- This process performs FIFO operations.
   proc_a : process (rd_en, wr_en, data_in, data_out,

   wr_en <= wr_en;
   proc_a : process (rd_en, wr_en, data_in, data_out,

**Fix**

.. code-block:: vhdl

   -- This process performs FIFO operations.
   proc_a : process (rd_en, wr_en, data_in, data_out,

   wr_en <= wr_en;

   proc_a : process (rd_en, wr_en, data_in, data_out,

process_016
###########

|phase_1| |error| |unfixable| |structure|

This rule checks the process has a label.

**Violation**

.. code-block:: vhdl

   process (rd_en, wr_en, data_in, data_out,
            rd_full, wr_full
           ) is
   begin

**Fix**

.. code-block:: vhdl

   proc_a : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is
   begin

process_017
###########

|phase_6| |error| |case| |case_label|

This rule checks the process label has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   PROC_A : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is
   begin

**Fix**

.. code-block:: vhdl

   proc_a : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is
   begin

process_018
###########

|phase_1| |error| |structure| |structure_optional|

This rule checks the **end process** line has a label.
The closing label will be added if the opening process label exists.

|configuring_optional_items_link|

**Violation**

.. code-block:: vhdl

   end process;

**Fix**

.. code-block:: vhdl

   end process proc_a;

process_019
###########

|phase_6| |error| |case| |case_label|

This rule checks the **end process** label has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   end process PROC_A;

**Fix**

.. code-block:: vhdl

   end process proc_a;

process_020
###########

|phase_4| |error| |alignment|

This rule checks the indentation of multiline sensitivity lists.

|configuring_multiline_indent_rules_link|

**Violation**

.. code-block:: vhdl

   proc_a : process (rd_en, wr_en, data_in, data_out,
                        rd_full, wr_full,
               overflow, underflow
                    ) is begin

**Fix**

.. code-block:: vhdl

   proc_a : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full,
                     overflow, underflow
                    ) is
   begin

process_021
###########

|phase_1| |error| |blank_line|

This rule checks for blank lines above the **begin** keyword if there are no process declarative items.

|configuring_blank_lines_link|

**Violation**

.. code-block:: vhdl

   proc_a : process

   begin


   proc_a : process (rd_en, wr_en)

   begin


   proc_a : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is



   begin

**Fix**

.. code-block:: vhdl

   proc_a : process
   begin


   proc_a : process (rd_en, wr_en)
   begin


   proc_a : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is
   begin

process_022
###########

|phase_3| |error| |blank_line|

This rule checks for a blank line below the **begin** keyword.

|configuring_blank_lines_link|

**Violation**

.. code-block:: vhdl

   proc_a : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is
   begin
     rd_en <= '0';

**Fix**

.. code-block:: vhdl

   proc_a : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is
   begin

     rd_en <= '0';

process_023
###########

|phase_3| |error| |blank_line|

This rule checks for a blank line above the **end process** keyword.

|configuring_blank_lines_link|

**Violation**

.. code-block:: vhdl

     wr_en <= '1';
   end process proc_a;

**Fix**

.. code-block:: vhdl

     wr_en <= '1';

   end process proc_a;

process_024
###########

|phase_2| |error| |whitespace|

This rule checks for a single space after the process label.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   proc_a: process (rd_en, wr_en, data_in, data_out,
                    rd_full, wr_full
                   ) is
   begin

**Fix**

.. code-block:: vhdl

   proc_a : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is
   begin

process_025
###########

|phase_2| |error| |whitespace|

This rule checks for a single space after the colon and before the **process** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   proc_a :process (rd_en, wr_en, data_in, data_out,
                    rd_full, wr_full
                   ) is begin

**Fix**

.. code-block:: vhdl

   proc_a : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is
   begin

process_026
###########

|phase_3| |error| |blank_line|

This rule checks for blank lines above the first declarative line, if it exists.

|configuring_blank_lines_link|

**Violation**

.. code-block:: vhdl

   proc_a : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is
     -- Keep track of the number of words in the FIFO
     variable word_count : integer;
   begin

**Fix**

.. code-block:: vhdl

   proc_a : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is

     -- Keep track of the number of words in the FIFO
     variable word_count : integer;
   begin

process_027
###########

|phase_3| |error| |blank_line|

This rule checks for blank lines above the **begin** keyword if a declarative item exists.

|configuring_blank_lines_link|

**Violation**

.. code-block:: vhdl

   proc_a : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is

     -- Keep track of the number of words in the FIFO
     variable word_count : integer;
   begin

**Fix**

.. code-block:: vhdl

   proc_a : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is

     -- Keep track of the number of words in the FIFO
     variable word_count : integer;

   begin

process_028
###########

|phase_5| |error| |alignment|

This rule checks the alignment of the closing parenthesis of a sensitivity list.
Parenthesis on multiple lines should be in the same column.

|configuring_keyword_alignment_rules_link|

**Violation**

.. code-block:: vhdl

   proc_a : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                       )

**Fix**

.. code-block:: vhdl

   proc_a : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    )

process_029
###########

|phase_1| |disabled| |error| |structure|

This rule checks for the format of clock definitions in clock processes.
The rule can be set to enforce **event** definition:

.. code-block:: vhdl

    if (clk'event and clk = '1') then

..or **edge** definition:

.. code-block:: vhdl

    if (rising_edge(clk)) then

event configuration
^^^^^^^^^^^^^^^^^^^

.. NOTE:: This is the default configuration.

**Violation**

.. code-block:: vhdl

   if (rising_edge(clk)) then

   if (falling_edge(clk)) then

**Fix**

.. code-block:: vhdl

   if (clk'event and clk = '1') then

   if (clk'event and clk = '0') then

edge configuration
^^^^^^^^^^^^^^^^^^

.. NOTE::  Configure this by setting the *'clock'* attribute to *'edge'*.

   .. code-block:: json

      {
        "rule":{
          "process_029":{
             "clock":"edge"
          }
        }
      }

**Violation**

.. code-block:: vhdl

   if (clk'event and clk = '1') then

   if (clk'event and clk = '0') then

**Fix**

.. code-block:: vhdl

   if (rising_edge(clk)) then

   if (falling_edge(clk)) then

process_030
###########

|phase_1| |error| |unfixable| |structure|

This rule checks for a single signal per line in a sensitivity list that is not the last one.
The sensitivity list is required by the compiler, but provides no useful information to the reader.
Therefore, the vertical spacing of the sensitivity list should be minimized.
This will help with code readability.

.. NOTE::  This rule is left to the user to fix.

**Violation**

.. code-block:: vhdl

   proc_a : process (rd_en,
                     wr_en,
                     data_in,
                     data_out,
                     rd_full,
                     wr_full
                    )

**Fix**

.. code-block:: vhdl

   proc_a : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    )

process_031
###########

|phase_5| |error| |alignment|

This rule checks for alignment of identifiers in the process declarative region.

|configuring_keyword_alignment_rules_link|

**Violation**

.. code-block:: vhdl

   proc_1 : process(all) is

    variable     var1 : boolean;
    constant  cons1 : integer;
    file            file1  : load_file_file open read_mode is load_file_name;

   begin

   end process proc_1;

**Fix**

.. code-block:: vhdl

   proc_1 : process(all) is

    variable var1 : boolean;
    constant cons1 : integer;
    file     file1  : load_file_file open read_mode is load_file_name;

   begin

   end process proc_1;

process_032
###########

This rule has been replaced with the following rules:

* `process_037 <process_rules.html#process-037>`_
* `process_038 <process_rules.html#process-038>`_

process_033
###########

|phase_5| |error| |alignment|

This rule checks the colons are in the same column for all declarations in the process declarative part.

|configuring_keyword_alignment_rules_link|

**Violation**

.. code-block:: vhdl

   variable var1 : natural;
   variable var2  : natural;
   constant c_period : time;
   file my_test_input : my_file_type;

**Fix**

.. code-block:: vhdl

   variable var1      : natural;
   variable var2      : natural;
   constant c_period  : time;
   file my_test_input : my_file_type;

process_034
###########

|phase_5| |error| |alignment|

This rule aligns inline comments between the end of the process sensitivity list and the process **begin** keyword.
|configuring_keyword_alignment_rules_link|

**Violation**

.. code-block:: vhdl

   proc_1 : process () is

      variable counter : integer range 0 to 31;     -- Counts the number of frames received
      variable width   : natural range 0 to 255; -- Keeps track of the data word size

      variable size    : natural range 0 to 7; -- Keeps track of the frame size

   begin

**Fix**

.. code-block:: vhdl

   proc_1 : process () is

      variable counter : integer range 0 to 31;  -- Counts the number of frames received
      variable width   : natural range 0 to 255; -- Keeps track of the data word size

      variable size    : natural range 0 to 7;   -- Keeps track of the frame size

   begin

process_035
###########

|phase_5| |error| |alignment|

This rule checks the alignment of inline comments between the process begin and end process lines.
|configuring_keyword_alignment_rules_link|

**Violation**

.. code-block:: vhdl

   proc_1: process () is
   begin

     a <= '1';   -- Assert
     b <= '0';       -- Deassert
     c <= '1'; -- Enable

   end process proc_1;

**Fix**

.. code-block:: vhdl

   proc_1: process () is
   begin

     a <= '1'; -- Assert
     b <= '0'; -- Deassert
     c <= '1'; -- Enable

   end process proc_1;

process_036
###########

|phase_7| |disabled| |error| |unfixable| |naming|

This rule checks for valid prefixes on process labels.
The default prefix is *proc_*.

|configuring_prefix_and_suffix_rules_link|

**Violation**

.. code-block:: vhdl

   main: process () is

**Fix**

.. code-block:: vhdl

   proc_main: process () is

process_037
###########

|phase_1| |error| |structure|

This rule checks a label and the colon are on the same line.

**Violation**

.. code-block:: vhdl

   label
   :

**Fix**

.. code-block:: vhdl

   label :

process_038
###########

|phase_1| |error| |structure|

This rule checks a label colon is on the same line as the **process** or **postponed** keyword.

**Violation**

.. code-block:: vhdl

   label :
   process

**Fix**

.. code-block:: vhdl

   label
   : process

process_039
###########

|phase_1| |error| |structure|

This rule checks a **postponed** keyword is on the same line at the **process** keyword.

**Violation**

.. code-block:: vhdl

   label : postponed
   process

**Fix**

.. code-block:: vhdl

   label :
   postponed process

process_400
###########

|phase_5| |error| |alignment|

This rule checks the alignment of the **<=** and **:=** operators over consecutive sequential assignments in the process_statement_part.

Following extra configurations are supported:

* :code:`if_control_statements_ends_group`,
* :code:`case_control_statements_ends_group`.
* :code:`case_keyword_statements_ends_group`.
* :code:`loop_control_statements_ends_group`,

|configuring_keyword_alignment_rules_link|

**Violation**

.. code-block:: vhdl

   wr_en <= '1';
   rd_en   <= '0';
   v_variable := 10;

**Fix**

.. code-block:: vhdl

   wr_en      <= '1';
   rd_en      <= '0';
   v_variable := 10;

process_401
###########

|phase_5| |error| |alignment|

This rule checks the colons are in the same column for all attribute specifications.

|configuring_keyword_alignment_rules_link|

**Violation**

.. code-block:: vhdl

     attribute mark_debug of wr_en : signal is "true";
     attribute mark_debug of almost_empty : signal is "true";
     attribute mark_debug of full : signal is "true";

**Fix**

.. code-block:: vhdl

     attribute mark_debug of wr_en        : signal is "true";
     attribute mark_debug of almost_empty : signal is "true";
     attribute mark_debug of full         : signal is "true";

process_600
###########

|phase_7| |disabled| |error| |unfixable| |naming|

This rule checks for valid suffixes on process labels.
The default suffix is *_proc*.

|configuring_prefix_and_suffix_rules_link|

**Violation**

.. code-block:: vhdl

   main: process () is

**Fix**

.. code-block:: vhdl

   main_proc: process () is
