.. include:: includes.rst

Port Rules
----------

port_001
########

|phase_3| |error| |blank_line|

This rule checks for a blank line above the **port** keyword.

|configuring_blank_lines_link|

**Violation**

.. code-block:: vhdl

   entity FIFO is

     port (

**Fix**

.. code-block:: vhdl

   entity FIFO is
     port (

port_002
########

|phase_4| |error| |indent|

This rule checks the indent of the **port** keyword.

**Violation**

.. code-block:: vhdl

   entity FIFO is
   port (

**Fix**

.. code-block:: vhdl

   entity FIFO is
     port (

port_003
########

|phase_2| |error| |whitespace|

This rule checks for a single space after the **port** keyword and (.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   port   (

   port(

**Fix**

.. code-block:: vhdl

   port (

   port (

port_004
########

|phase_4| |error| |indent|

This rule checks the indent of port declarations.

**Violation**

.. code-block:: vhdl

   port (
   WR_EN    : in    std_logic;
        RD_EN    : in    std_logic;
     OVERFLOW : out   std_logic
   );

**Fix**

.. code-block:: vhdl

   port (
     WR_EN    : in    std_logic;
     RD_EN    : in    std_logic;
     OVERFLOW : out   std_logic
   );

port_005
########

This rule has been deprecated and its function has been included in rules **port_007**, **port_008** and **port_009**.

port_006
########

This rule has been deprecated and its function was include in rule **port_005**.

port_007
########

|phase_2| |error| |whitespace|

This rule checks for spaces before and after the **in** mode keyword.

|configuring_port_mode_alignment_link|

**Violation**

.. code-block:: vhdl

   port (
     WR_EN    : in std_logic;
     RD_EN    : in        std_logic;
     OVERFLOW : out   std_logic
   );

**Fix**

.. code-block:: vhdl

   port (
     WR_EN    : in    std_logic;
     RD_EN    : in    std_logic;
     OVERFLOW : out   std_logic
   );

port_008
########

|phase_2| |error| |whitespace|

This rule checks for spaces before and after the **out** mode keyword.

|configuring_port_mode_alignment_link|

**Violation**

.. code-block:: vhdl

   port (
     WR_EN    : in    std_logic;
     RD_EN    : in    std_logic;
     OVERFLOW : out   std_logic
   );

**Fix**

.. code-block:: vhdl

   port (
     WR_EN    : in    std_logic;
     RD_EN    : in    std_logic;
     OVERFLOW : out std_logic
   );

port_009
########

|phase_2| |error| |whitespace|

This rule checks for spaces before and after the **inout** mode keyword.

|configuring_port_mode_alignment_link|

**Violation**

.. code-block:: vhdl

   port (
     WR_EN    : in    std_logic;
     RD_EN    : in    std_logic;
     DATA     : inout    std_logic
   );

**Fix**

.. code-block:: vhdl

   port (
     WR_EN    : in    std_logic;
     RD_EN    : in    std_logic;
     DATA     : inout std_logic
   );

port_010
########

|phase_6| |error| |case| |case_name|

This rule checks the port names have proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   port (
     wr_en     : in    std_logic;
     rd_en     : in    std_logic;
     OVERFLOW  : out   std_logic;
     underflow : out   std_logic
   );

**Fix**

.. code-block:: vhdl

   port (
     wr_en     : in    std_logic;
     rd_en     : in    std_logic;
     overflow  : out   std_logic;
     underflow : out   std_logic
   );

port_011
########

|phase_7| |disabled| |error| |unfixable| |naming|

This rule checks for valid prefixes on port identifiers.
The default port prefixes are: *i_*, *o_*, *io_*.

|configuring_prefix_and_suffix_rules_link|

**Violation**

.. code-block:: vhdl

   port (
     wr_en    : in    std_logic;
     rd_en    : in    std_logic;
     overflow : out   std_logic;
     data     : inout std_logic
   );


**Fix**

.. code-block:: vhdl

   port (
     i_wr_en    : in    std_logic;
     i_rd_en    : in    std_logic;
     o_overflow : out   std_logic;
     io_data    : inout std_logic
   );

port_012
########

|phase_1| |error| |unfixable| |structure|

This rule checks for default assignments on port declarations.

This rule is defaulted to not fixable and can be overridden with a configuration to remove the default assignments.

**Violation**

.. code-block:: vhdl

   port (
     I_WR_EN    : in    std_logic := '0';
     I_RD_EN    : in    std_logic := '0';
     O_OVERFLOW : out   std_logic;
     IO_DATA    : inout std_logic := (others => 'Z')
   );

**Fix**

.. code-block:: vhdl

   port (
     I_WR_EN    : in    std_logic;
     I_RD_EN    : in    std_logic;
     O_OVERFLOW : out   std_logic;
     IO_DATA    : inout std_logic
   );

port_013
########

|phase_1| |error| |structure|

This rule checks for multiple ports declared on a single line.

**Violation**

.. code-block:: vhdl

   port (
     WR_EN    : in    std_logic;RD_EN    : in    std_logic;
     OVERFLOW : out   std_logic;DATA     : inout std_logic
   );

**Fix**

.. code-block:: vhdl

   port (
     WR_EN    : in    std_logic;
     RD_EN    : in    std_logic;
     OVERFLOW : out   std_logic;
     DATA     : inout std_logic
   );

port_014
########

|phase_1| |error| |structure|

This rule checks the location of the closing ")" character for the port clause.

The default location is on a line by itself.

|configuring_move_token_rules_link|

**Violation**

.. code-block:: vhdl

   port (
     WR_EN    : in    std_logic;
     RD_EN    : in    std_logic;
     OVERFLOW : out   std_logic;
     DATA     : inout std_logic);

**Fix**

.. code-block:: vhdl

   port (
     WR_EN    : in    std_logic;
     RD_EN    : in    std_logic;
     OVERFLOW : out   std_logic;
     DATA     : inout std_logic
   );

port_015
########

|phase_4| |error| |indent|

This rule checks the indent of the closing parenthesis for port clauses.

**Violation**

.. code-block:: vhdl

   port (
     WR_EN    : in    std_logic;
     RD_EN    : in    std_logic;
     OVERFLOW : out   std_logic;
     DATA     : inout std_logic
     );

**Fix**

.. code-block:: vhdl

   port (
     WR_EN    : in    std_logic;
     RD_EN    : in    std_logic;
     OVERFLOW : out   std_logic;
     DATA     : inout std_logic
   );

port_016
########

|phase_1| |error| |structure|

This rule checks for a port definition on the same line as the **port** keyword.

**Violation**

.. code-block:: vhdl

   port (WR_EN    : in    std_logic;
     RD_EN    : in    std_logic;
     OVERFLOW : out   std_logic;
     DATA     : inout std_logic
   );

**Fix**

.. code-block:: vhdl

   port (
     WR_EN    : in    std_logic;
     RD_EN    : in    std_logic;
     OVERFLOW : out   std_logic;
     DATA     : inout std_logic
   );

port_017
########

|phase_6| |error| |case| |case_keyword|

This rule checks the **port** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   PORT (

**Fix**

.. code-block:: vhdl

   port (

port_018
########

This rule was deprecated and replaced with the following rule:

* :ref:`type_mark_500`

port_019
########

|phase_6| |error| |case| |case_keyword|

This rule checks the port direction has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   port (
     WR_EN    : IN    std_logic;
     RD_EN    : in    std_logic;
     OVERFLOW : OUT   std_logic;
     DATA     : INOUT std_logic
   );

**Fix**

.. code-block:: vhdl

   port (
     WR_EN    : in    std_logic;
     RD_EN    : in    std_logic;
     OVERFLOW : out   std_logic;
     DATA     : inout std_logic
   );

port_020
########

|phase_2| |error| |whitespace|

This rule checks for at least one space before the colon.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   port (
     WR_EN    : in    std_logic;
     RD_EN    : in    std_logic;
     OVERFLOW: out   std_logic;
     DATA     : inout std_logic
   );

**Fix**

.. code-block:: vhdl

   port (
     WR_EN    : in    std_logic;
     RD_EN    : in    std_logic;
     OVERFLOW : out   std_logic;
     DATA     : inout std_logic
   );

port_021
########

|phase_1| |error| |structure|

This rule checks the **port** keyword is on the same line as the (.

**Violation**

.. code-block:: vhdl

   port
   (

**Fix**

.. code-block:: vhdl

   port (

port_022
########

|phase_3| |error| |blank_line|

This rule checks for blank lines after the **port** keyword.

**Violation**

.. code-block:: vhdl

   port (


     WR_EN    : in    std_logic;
     RD_EN    : in    std_logic;
     OVERFLOW: out   std_logic;
     DATA     : inout std_logic
   );

**Fix**

.. code-block:: vhdl

   port (
     WR_EN    : in    std_logic;
     RD_EN    : in    std_logic;
     OVERFLOW : out   std_logic;
     DATA     : inout std_logic
   );

port_023
########

|phase_1| |error| |unfixable| |structure|

This rule checks for missing modes in port declarations.

.. NOTE:: This must be fixed by the user.  VSG makes no assumption on the direction of the port.

**Violation**

.. code-block:: vhdl

   port (
     WR_EN    : std_logic;
     RD_EN    : std_logic;
     OVERFLOW : std_logic;
     V_TEST   : some_view;
     DATA     : inout std_logic
   );

**Fix**

.. code-block:: vhdl

   port (
     WR_EN    : in    std_logic;
     RD_EN    : in    std_logic;
     OVERFLOW : out   std_logic;
     V_TEST   : view  some_view;
     DATA     : inout std_logic
   );

port_024
########

|phase_3| |error| |blank_line|

This rule checks for blank lines before the close parenthesis in port declarations.

**Violation**

.. code-block:: vhdl

   port (
     WR_EN    : std_logic;
     RD_EN    : std_logic;
     OVERFLOW : std_logic;
     DATA     : inout std_logic


   );

**Fix**

.. code-block:: vhdl

   port (
     WR_EN    : in    std_logic;
     RD_EN    : in    std_logic;
     OVERFLOW : out   std_logic;
     DATA     : inout std_logic
   );

port_025
########

|phase_7| |disabled| |error| |unfixable| |naming|

This rule checks for valid suffixes on port identifiers.
The default port suffixes are *_i*, *_o*, *_io*.

|configuring_prefix_and_suffix_rules_link|

**Violation**

.. code-block:: vhdl

   port (
     wr_en    : in    std_logic;
     rd_en    : in    std_logic;
     overflow : out   std_logic;
     data     : inout std_logic
   );

**Fix**

.. code-block:: vhdl

   port (
     wr_en_i    : in    std_logic;
     rd_en_i    : in    std_logic;
     overflow_o : out   std_logic;
     data_io    : inout std_logic
   );

port_026
########

|phase_1| |error| |structure|

This rule checks for multiple identifiers on port declarations.

Any comments are not replicated.

**Violation**

.. code-block:: vhdl

   port (
     wr_en, rd_en : in    std_logic;  -- Comment
     data     : inout std_logic;
     overflow, empty : out   std_logic -- Other comment
   );

**Fix**

.. code-block:: vhdl

   port (
     wr_en    : in    std_logic;
     rd_en    : in    std_logic;  -- Comment
     data    : inout std_logic
     overflow : out   std_logic;
     empty : out   std_logic -- Other comment
   );

port_027
########

|phase_1| |error| |structure|

This rule checks the semicolon is not on its own line.

**Violation**

.. code-block:: vhdl

   U_FIFO : FIFO
     port (
       I_WIDTH : in integer
     )
     ;

**Fix**

.. code-block:: vhdl

   U_FIFO : FIFO
     generic (
       I_WIDTH : in integer
     );

port_100
########

|phase_2| |error| |whitespace|

This rule checks for at least a single space before the assignment.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   I_WIDTH : in integer:= 32;

**Fix**

.. code-block:: vhdl

   I_WIDTH : in integer := 32;

port_101
########

|phase_2| |error| |whitespace|

This rule checks for a single space after the assignment.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   I_WIDTH : in integer :=32;
   I_DEPTH : in integer :=    256;

**Fix**

.. code-block:: vhdl

   I_WIDTH : in integer := 32;
   I_DEPTH : in integer := 256;

port_600
########

|phase_7| |disabled| |error| |unfixable| |naming|

This rule checks for valid prefixes on port identifiers for input ports.

The default prefix is: *i_*.

|configuring_prefix_and_suffix_rules_link|

**Violation**

.. code-block:: vhdl

   port (
     wr_en    : in    std_logic;
     rd_en    : in    std_logic
   );


**Fix**

.. code-block:: vhdl

   port (
     i_wr_en    : in    std_logic;
     i_rd_en    : in    std_logic
   );

port_601
########

|phase_7| |disabled| |error| |unfixable| |naming|

This rule checks for valid prefixes on port identifiers for output ports.

The default prefix is: *o_*.

|configuring_prefix_and_suffix_rules_link|

**Violation**

.. code-block:: vhdl

   port (
     wr_en    : out    std_logic;
     rd_en    : out    std_logic
   );


**Fix**

.. code-block:: vhdl

   port (
     o_wr_en    : out    std_logic;
     o_rd_en    : out    std_logic
   );

port_602
########

|phase_7| |disabled| |error| |unfixable| |naming|

This rule checks for valid prefixes on port identifiers for inout ports.

The default prefix is: *io_*.

|configuring_prefix_and_suffix_rules_link|

**Violation**

.. code-block:: vhdl

   port (
     wr_en    : inout    std_logic;
     rd_en    : inout    std_logic
   );


**Fix**

.. code-block:: vhdl

   port (
     io_wr_en    : inout    std_logic;
     io_rd_en    : inout    std_logic
   );

port_603
########

|phase_7| |disabled| |error| |unfixable| |naming|

This rule checks for valid prefixes on port identifiers for buffer ports.

The default prefix is: *b_*.

|configuring_prefix_and_suffix_rules_link|

**Violation**

.. code-block:: vhdl

   port (
     wr_en    : buffer    std_logic;
     rd_en    : buffer    std_logic
   );


**Fix**

.. code-block:: vhdl

   port (
     b_wr_en    : buffer    std_logic;
     b_rd_en    : buffer    std_logic
   );

port_604
########

|phase_7| |disabled| |error| |unfixable| |naming|

This rule checks for valid prefixes on port identifiers for linkage ports.

The default prefix is: *l_*.

|configuring_prefix_and_suffix_rules_link|

**Violation**

.. code-block:: vhdl

   port (
     wr_en    : linkage    std_logic;
     rd_en    : linkage    std_logic
   );


**Fix**

.. code-block:: vhdl

   port (
     l_wr_en    : linkage    std_logic;
     l_rd_en    : linkage    std_logic
   );

port_605
########

|phase_7| |disabled| |error| |unfixable| |naming|

This rule checks for valid suffixes on port identifiers for input ports.

The default suffix is: *_i*.

|configuring_prefix_and_suffix_rules_link|

**Violation**

.. code-block:: vhdl

   port (
     wr_en    : in    std_logic;
     rd_en    : in    std_logic
   );


**Fix**

.. code-block:: vhdl

   port (
     wr_en_i    : in    std_logic;
     rd_en_i    : in    std_logic
   );

port_606
########

|phase_7| |disabled| |error| |unfixable| |naming|

This rule checks for valid suffixes on port identifiers for output ports.

The default suffix is: *_o*.

|configuring_prefix_and_suffix_rules_link|

**Violation**

.. code-block:: vhdl

   port (
     wr_en    : out    std_logic;
     rd_en    : out    std_logic
   );

**Fix**

.. code-block:: vhdl

   port (
     wr_en_o    : out    std_logic;
     rd_en_o    : out    std_logic
   );

port_607
########

|phase_7| |disabled| |error| |unfixable| |naming|

This rule checks for valid suffixes on port identifiers for inout ports.

The default suffix is: *_io*.

|configuring_prefix_and_suffix_rules_link|

**Violation**

.. code-block:: vhdl

   port (
     wr_en    : inout    std_logic;
     rd_en    : inout    std_logic
   );

**Fix**

.. code-block:: vhdl

   port (
     wr_en_io    : inout    std_logic;
     rd_en_io    : inout    std_logic
   );

port_608
########

|phase_7| |disabled| |error| |unfixable| |naming|

This rule checks for valid suffixes on port identifiers for buffer ports.

The default suffix is: *_b*.

|configuring_prefix_and_suffix_rules_link|

**Violation**

.. code-block:: vhdl

   port (
     wr_en    : buffer    std_logic;
     rd_en    : buffer    std_logic
   );

**Fix**

.. code-block:: vhdl

   port (
     wr_en_b    : buffer    std_logic;
     rd_en_b    : buffer    std_logic
   );

port_609
########

|phase_7| |disabled| |error| |unfixable| |naming|

This rule checks for valid suffixes on port identifiers for linkage ports.

The default suffix is: *_l*.

|configuring_prefix_and_suffix_rules_link|

**Violation**

.. code-block:: vhdl

   port (
     wr_en    : linkage    std_logic;
     rd_en    : linkage    std_logic
   );

**Fix**

.. code-block:: vhdl

   port (
     wr_en_l    : linkage    std_logic;
     rd_en_l    : linkage    std_logic
   );
