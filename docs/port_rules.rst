.. include:: icons.rst

Port Rules
----------

port_001
########

|phase_3| |error|

This rule checks for a blank line above the **port** keyword.

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

|phase_4| |error|

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

|phase_2| |error|

This rule checks for a single space after the **port** keyword and (.

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

|phase_4| |error|

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

|phase_2| |error|

This rule checks for a single space after the colon.

**Violation**

.. code-block:: vhdl

   port (
     WR_EN    : in    std_logic;
     RD_EN    :   in    std_logic;
     OVERFLOW :out   std_logic;
     DATA     :inout std_logic
   );

**Fix**

.. code-block:: vhdl

   port (
     WR_EN    : in    std_logic;
     RD_EN    : in    std_logic;
     OVERFLOW : out   std_logic;
     DATA     : inout std_logic
   );

port_006
########

This rule has been depricated and it's function was include in rule **port_005**.


port_007
########

|phase_2| |error|

This rule checks for four spaces after the **in** keyword.

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

|phase_2| |error|

This rule checks for three spaces after the **out** keyword.

**Violation**

.. code-block:: vhdl

   port (
     WR_EN    : in    std_logic;
     RD_EN    : in    std_logic;
     OVERFLOW : out std_logic
   );


**Fix**

.. code-block:: vhdl

   port (
     WR_EN    : in    std_logic;
     RD_EN    : in    std_logic;
     OVERFLOW : out   std_logic
   );

port_009
########

|phase_2| |error|

This rule checks for a single space after the **inout** keyword.

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

|phase_6| |error|

This rule checks the port names have proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

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

|phase_7| |disabled| |error|

This rule checks for valid prefixes on port identifiers.
The default port prefixes are: *i\_*, *o\_*, *io\_*.

Refer to the section `Configuring Prefix and Suffix Rules <configuring.html#configuring-prefix-and-suffix-rules>`_ for information on changing the allowed prefixes.

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

|phase_1| |error|

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

|phase_1| |error|

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

|phase_1| |error|

This rule checks the closing parenthesis of the port map is on a line by itself.

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

|phase_4| |error|

This rule checks the indent of the closing parenthesis for port maps.

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

|phase_1| |error|

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

|phase_6| |error|

This rule checks the **port** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   PORT (

**Fix**

.. code-block:: vhdl

   port (

port_018
########

|phase_6| |error|

This rule checks the port type has proper case if it is a VHDL keyword.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.


**Violation**

.. code-block:: vhdl

   port (
     WR_EN    : in    STD_LOGIC;
     RD_EN    : in    std_logic;
     OVERFLOW : out   t_OVERFLOW;
     DATA     : inout STD_LOGIC_VECTOR(31 downto 0)
   );

**Fix**

.. code-block:: vhdl

   port (
     WR_EN    : in    std_logic;
     RD_EN    : in    std_logic;
     OVERFLOW : out   t_OVERFLOW;
     DATA     : inout std_logic_vector(31 downto 0)
   );

port_019
########

|phase_6| |error|

This rule checks the port direction has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

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

|phase_2| |error|

This rule checks for at least one space before the colon.

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

|phase_1| |error|

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

|phase_3| |error|

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

|phase_1| |error|

This rule checks for missing modes in port declarations.

.. NOTE:: This must be fixed by the user.  VSG makes no assumption on the direction of the port.

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

port_024
########

|phase_3| |error|

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

|phase_7| |disabled| |error|

This rule checks for valid suffixes on port identifiers.
The default port suffixes are *_i*, *_o*, *_io*.

Refer to the section `Configuring Prefix and Suffix Rules <configuring.html#configuring-prefix-and-suffix-rules>`_ for information on changing the allowed suffixes.

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

|phase_1| |error|

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
