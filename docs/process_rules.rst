Process Rules
-------------

process_001
###########
 
This rule checks the indent of the process declaration.

**Violation**

.. code-block:: vhdl

   architecture RTL of FIFO is

   begin

   PROC_A : process (rd_en, wr_en, data_in, data_out,

**Fix**

.. code-block:: vhdl

   architecture RTL of FIFO is

   begin

     PROC_A : process (rd_en, wr_en, data_in, data_out,


process_002
###########
 
This rule checks for a single space after the **process** keyword.

**Violation**

.. code-block:: vhdl

   PROC_A : process(rd_en, wr_en, data_in, data_out,

   PROC_A : process    (rd_en, wr_en, data_in, data_out,

**Fix**

.. code-block:: vhdl

   PROC_A : process (rd_en, wr_en, data_in, data_out,

   PROC_A : process (rd_en, wr_en, data_in, data_out,

process_003
###########
 
This rule checks the indent of the **begin** keyword.

**Violation**

.. code-block:: vhdl

   PROC_A : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is
     begin

**Fix**

.. code-block:: vhdl

   PROC_A : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is
   begin

process_004
###########
 
This rule checks the **begin** keyword has proper case.

.. NOTE:: The default is lowercase.

**Violation**

.. code-block:: vhdl

   PROC_A : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is
   BEGIN

**Fix**

.. code-block:: vhdl

   PROC_A : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is
   begin

process_005
###########
 
This rule checks the **process** keyword has proper case.

.. NOTE:: The default is lowercase.

**Violation**

.. code-block:: vhdl

   PROC_A : PROCESS (rd_en, wr_en, data_in, data_out,

**Fix**

.. code-block:: vhdl

   PROC_A : process (rd_en, wr_en, data_in, data_out,

process_006
###########
 
This rule checks the indent of the **end process** keywords.

**Violation**

.. code-block:: vhdl

   PROC_A : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is
   begin

     end process PROC_A;

**Fix**

.. code-block:: vhdl

   PROC_A : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is
   begin

   end process PROC_A;

process_007
###########
 
This rule checks for a single space after the **end** keyword.

**Violation**

.. code-block:: vhdl

   end   process PROC_A;

**Fix**

.. code-block:: vhdl

   end process PROC_A;

process_008
###########
 
This rule checks the **end** keyword has proper case.

.. NOTE:: The default is lowercase.

   Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   END process PROC_A;

**Fix**

.. code-block:: vhdl

   end process PROC_A;

process_009
###########
 
This rule checks the **process** keyword has proper case in the **end process** line.

.. NOTE:: The default is lowercase.

**Violation**

.. code-block:: vhdl

   end PROCESS PROC_A;

**Fix**

.. code-block:: vhdl

   end process PROC_A;

process_010
###########
 
This rule checks the **begin** keyword is on it's own line.

**Violation**

.. code-block:: vhdl

   PROC_A : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is begin

**Fix**

.. code-block:: vhdl

   PROC_A : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is
   begin

process_011
###########
 
This rule checks for a blank line after the **end process** keyword.

**Violation**

.. code-block:: vhdl

   end process PROC_A;
   WR_EN <= wr_en;

**Fix**

.. code-block:: vhdl

   end process PROC_A;

   WR_EN <= wr_en;

process_012
###########
 
This rule checks for the existence of the **is** keyword on the same line as the closing parenthesis of the sensitivity list.

**Violation**

.. code-block:: vhdl

   PROC_A : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    )
   begin

   PROC_A : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    )
   is begin

**Fix**

.. code-block:: vhdl

   PROC_A : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is
   begin

   PROC_A : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is
   begin

process_013
###########
 
This rule checks the **is** keyword has proper case.

.. NOTE:: The default is lowercase.

**Violation**

.. code-block:: vhdl

   PROC_A : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) IS
   begin

**Fix**

.. code-block:: vhdl

   PROC_A : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is
   begin

process_014
###########
 
This rule checks for a single space before the **is** keyword.

**Violation**

.. code-block:: vhdl

   PROC_A : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    )     is
   begin

**Fix**

.. code-block:: vhdl

   PROC_A : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is
   begin

process_015
###########
 
This rule checks for a blank line or comment above the **process** declaration.

**Violation**

.. code-block:: vhdl

   -- This process performs FIFO operations.   
   PROC_A : process (rd_en, wr_en, data_in, data_out,

   WR_EN <= wr_en;
   PROC_A : process (rd_en, wr_en, data_in, data_out,

**Fix**

.. code-block:: vhdl

   -- This process performs FIFO operations.   
   PROC_A : process (rd_en, wr_en, data_in, data_out,

   WR_EN <= wr_en;

   PROC_A : process (rd_en, wr_en, data_in, data_out,

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

   PROC_A : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is
   begin

process_017
###########
 
This rule checks the process label has proper case.

.. NOTE:: The default is uppercase.

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

process_018
###########
 
This rule checks the **end process** line has a label.
The closing label will be added if the opening process label exists.

**Violation**

.. code-block:: vhdl

   end process;

**Fix**

.. code-block:: vhdl

   end process PROC_A;

process_019
###########
 
This rule checks the **end process** label is uppercase.

**Violation**

.. code-block:: vhdl

   end process proc_a;

**Fix**

.. code-block:: vhdl

   end process PROC_A;

process_020
###########
 
This rule checks the indentation of multiline sensitivity lists.

**Violation**

.. code-block:: vhdl

   PROC_A : process (rd_en, wr_en, data_in, data_out,
                        rd_full, wr_full,
               overflow, underflow
                    ) is begin

**Fix**

.. code-block:: vhdl

   PROC_A : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full,
                     overflow, underflow
                    ) is
   begin

process_021
###########
 
This rule checks for blank lines between the end of the sensitivity list and before the **begin** keyword.

**Violation**

.. code-block:: vhdl

   PROC_A : process (rd_en, wr_en, data_in, data_out,
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

   PROC_A : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is
   begin
     rd_en <= '0';

**Fix**

.. code-block:: vhdl

   PROC_A : process (rd_en, wr_en, data_in, data_out,
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
   end process PROC_A;

**Fix**

.. code-block:: vhdl

     wr_en <= '1';

   end process PROC_A;

process_024
###########
 
This rule checks for a single space after the process label.

**Violation**

.. code-block:: vhdl

   PROC_A: process (rd_en, wr_en, data_in, data_out,
                    rd_full, wr_full
                   ) is
   begin

**Fix**

.. code-block:: vhdl

   PROC_A : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is
   begin

process_025
###########
 
This rule checks for a single space after the : and before the **process** keyword.

**Violation**

.. code-block:: vhdl

   PROC_A :process (rd_en, wr_en, data_in, data_out,
                    rd_full, wr_full
                   ) is begin

**Fix**

.. code-block:: vhdl

   PROC_A : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is
   begin

process_026
###########
 
This rule checks for blank lines between the end of the sensitivity list and process declarative lines.

**Violation**

.. code-block:: vhdl

   PROC_A : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is
     -- Keep track of the number of words in the FIFO
     variable word_count : integer;
   begin

**Fix**

.. code-block:: vhdl

   PROC_A : process (rd_en, wr_en, data_in, data_out,
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

   PROC_A : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    ) is

     -- Keep track of the number of words in the FIFO
     variable word_count : integer;
   begin

**Fix**

.. code-block:: vhdl

   PROC_A : process (rd_en, wr_en, data_in, data_out,
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

   PROC_A : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                       )

**Fix**

.. code-block:: vhdl

   PROC_A : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    )

process_029
###########

This rule checks for the format of clock definitions in clock processes.
The rule can be set to enforce **event** definition:

.. code-block:: vhdl

    if (CLK'event and CLK = '1') then

..or **edge** definition:

.. code-block:: vhdl

    if (rising_edge(CLK)) then

event configuration
^^^^^^^^^^^^^^^^^^^

.. NOTE:: This is the default configuration.

**Violation**

.. code-block:: vhdl

   if (rising_edge(CLK)) then

   if (falling_edge(CLK)) then

**Fix**

.. code-block:: vhdl

   if (CLK'event and CLK = '1') then

   if (CLK'event and CLK = '0') then

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

   if (CLK'event and CLK = '1') then

   if (CLK'event and CLK = '0') then

**Fix**

.. code-block:: vhdl

   if (rising_edge(CLK)) then

   if (falling_edge(CLK)) then

process_030
###########

This rule checks for a single signal per line in a sensitivity list that is not the last one.
The sensitivity list is required by the compiler, but provides no useful information to the reader.
Therefore, the vertical spacing of the sensitivity list should be minimized.
This will help with code readability.

.. NOTE::  This rule is left to the user to fix.

**Violation**

.. code-block:: vhdl

   PROC_A : process (rd_en,
                     wr_en,
                     data_in,
                     data_out,
                     rd_full,
                     wr_full
                    )

**Fix**

.. code-block:: vhdl

   PROC_A : process (rd_en, wr_en, data_in, data_out,
                     rd_full, wr_full
                    )

process_031
###########

This rule checks for alignment of identifiers and colons of constant, variable, and file.

**Violation**

.. code-block:: vhdl

   PROC_1 : process(A) is

    variable     var1 : boolean;
    constant  cons1 : integer;
    file            file1 : load_file_file open read_mode is load_file_name;

   begin

   end process PROC_1;

**Fix**

.. code-block:: vhdl

   PROC_1 : process(A) is

    variable var1  : boolean;
    constant cons1 : integer;
    file     file1 : load_file_file open read_mode is load_file_name;

   begin

   end process PROC_1;

process_032
###########

This rule checks the process label is on the same line as the process keyword.

**Violation**

.. code-block:: vhdl

   PROC_1 :

   process(A) is

**Fix**

.. code-block:: vhdl

   PROC_1 : process(A) is
