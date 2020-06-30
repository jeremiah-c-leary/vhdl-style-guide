Process Rules
-------------

process_001
###########
 
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
 
This rule checks for a single space after the **process** keyword.

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
 
This rule checks the **begin** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

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
 
This rule checks the **process** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   proc_a : PROCESS (rd_en, wr_en, data_in, data_out,

**Fix**

.. code-block:: vhdl

   proc_a : process (rd_en, wr_en, data_in, data_out,

process_006
###########
 
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
 
This rule checks for a single space after the **end** keyword.

**Violation**

.. code-block:: vhdl

   end   process proc_a;

**Fix**

.. code-block:: vhdl

   end process proc_a;

process_008
###########
 
This rule checks the **end** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   END process proc_a;

**Fix**

.. code-block:: vhdl

   end process proc_a;

process_009
###########
 
This rule checks the **process** keyword has proper case in the **end process** line.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   end PROCESS proc_a;

**Fix**

.. code-block:: vhdl

   end process proc_a;

process_010
###########
 
This rule checks the **begin** keyword is on it's own line.

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
 
This rule checks for a blank line after the **end process** keyword.

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
 
This rule checks for the existence of the **is** keyword on the same line as the closing parenthesis of the sensitivity list.

**Violation**

.. code-block:: vhdl

   proc_a : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    )
   begin

   proc_a : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    )
   is begin

**Fix**

.. code-block:: vhdl

   proc_a : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is
   begin

   proc_a : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is
   begin

process_013
###########
 
This rule checks the **is** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

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
 
This rule checks for a single space before the **is** keyword.

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
 
This rule checks for a blank line or comment above the **process** declaration.

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
 
This rule checks the process label has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

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
 
This rule checks the **end process** line has a label.
The closing label will be added if the opening process label exists.

**Violation**

.. code-block:: vhdl

   end process;

**Fix**

.. code-block:: vhdl

   end process proc_a;

process_019
###########
 
This rule checks the **end process** label has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   end process PROC_A;

**Fix**

.. code-block:: vhdl

   end process proc_a;

process_020
###########
 
This rule checks the indentation of multiline sensitivity lists.

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
 
This rule checks for blank lines between the end of the sensitivity list and before the **begin** keyword.

**Violation**

.. code-block:: vhdl

   proc_a : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is



   begin

**Fix**

.. code-block:: vhdl

   PROC_A : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is
   begin

process_022
###########
 
This rule checks for a blank line below the **begin** keyword.

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
 
This rule checks for a blank line above the **end process** keyword.

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
 
This rule checks for a single space after the process label.

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
 
This rule checks for a single space after the : and before the **process** keyword.

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
 
This rule checks for blank lines between the end of the sensitivity list and process declarative lines.

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
 
This rule checks for blank lines between process declarative lines and the **begin** keyword.

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

This rule checks the alignment of the closing parenthesis of a sensitivity list.
Parenthesis on multiple lines should be in the same column.

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

.. NOTE::  Configuration this by setting the *'clock'* attribute to *'edge'*

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

This rule checks for alignment of identifiers in the process declarative region.

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

This rule checks the process label is on the same line as the process keyword.

**Violation**

.. code-block:: vhdl

   proc_1 :

   process(all) is

**Fix**

.. code-block:: vhdl

   proc_1 : process(all) is

process_033
###########

This rule checks the colons are in the same column for all declarations in the process declarative part.
Refer to the section `Configuring Keyword Alignment Rules <configuring_keyword_alignment.html>`_ for information on changing the configurations.

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

This rule aligns inline comments between the end of the process sensitivity list and the process **begin** keyword.
Refer to the section `Configuring Keyword Alignment Rules <configuring_keyword_alignment.html>`_ for information on changing the configurations.

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

This rule checks the alignment of inline comments between the process begin and end process lines.
Refer to the section `Configuring Keyword Alignment Rules <configuring_keyword_alignment.html>`_ for information on changing the configurations.

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
############

This rule checks for valid prefixes on process labels.
The default prefix is *proc\_*.

Refer to the section `Configuring Prefix and Suffix Rules <configuring_prefix_suffix.html>`_ for information on changing the allowed prefixes.

**Violation**

.. code-block:: vhdl

   main: process () is

**Fix**

.. code-block:: vhdl

   proc_main: process () is

process_037
###########

This rule checks for alignment of identifiers in attribute, type, subtype, constant, signal, variable and file declarations in the process declarative region.

Refer to the section `Configuring Identifier Alignment Rules <configuring_declaration_identifier_alignment.html>`_ for information on changing the configurations.

**Violation**

.. code-block:: vhdl

   signal    sig1 : std_logic;
   file some_file : 
   variable v_var1 : std_logic;
   type t_myType : std_logic;
   
**Fix**

.. code-block:: vhdl

   signal   sig1 : std_logic;
   file     some_file : 
   variable v_var1 : std_logic;
   type     t_myType : std_logic;

