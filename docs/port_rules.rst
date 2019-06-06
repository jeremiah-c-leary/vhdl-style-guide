Port Rules
----------

port_001
########

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

This rule checks for a single space after the : in **in** and **inout** ports.

**Violation**

.. code-block:: vhdl

   port (
     WR_EN    : in    std_logic;
     RD_EN    :   in    std_logic;
     OVERFLOW : out   std_logic;
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

This rule checks for a single space after the : in the **out** ports.

**Violation**

.. code-block:: vhdl

   port (
     WR_EN    : in    std_logic;
     RD_EN    : in    std_logic;
     OVERFLOW :out   std_logic
   );

**Fix**

.. code-block:: vhdl

   port (
     WR_EN    : in    std_logic;
     RD_EN    : in    std_logic;
     OVERFLOW : out   std_logic
   );

port_007
########

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

This rule checks port names are uppercase.
If an index exists on a port, the case of the index will not be checked.

**Violation**

.. code-block:: vhdl

   port (
     wr_en              : in    std_logic;
     rd_en              : in    std_logic;
     OVERFLOW           : out   std_logic;
     underflow(c_index) : out   std_logic
   );

**Fix**

.. code-block:: vhdl

   port (
     WR_EN              : in    std_logic;
     RD_EN              : in    std_logic;
     OVERFLOW           : out   std_logic;
     UNDERFLOW(c_index) : out   std_logic
   );

port_011
########

This rule checks port names have a I\_, O\_, or IO\_ prefixes or _I, _O, or _IO suffixes.
This rule can be configured to enforce prefixes, suffixes, or neither.
The default is neither.

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
     I_WR_EN    : in    std_logic;
     I_RD_EN    : in    std_logic;
     O_OVERFLOW : out   std_logic;
     IO_DATA    : inout std_logic
   );

   port (
     WR_EN_I    : in    std_logic;
     RD_EN_I    : in    std_logic;
     OVERFLOW_O : out   std_logic;
     DATA_IO    : inout std_logic
   );

port_012
########

This rule checks for default assignments on port declarations.

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
     WR_EN_I    : in    std_logic;
     RD_EN_I    : in    std_logic;
     OVERFLOW_O : out   std_logic;
     DATA_IO    : inout std_logic
   );

port_013
########

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

This rule checks the closing parenthesis of the port map are on a line by itself.

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

This rule checks the **port** keyword is lowercase.

**Violation**

.. code-block:: vhdl

   PORT (

**Fix**

.. code-block:: vhdl

   port (

port_018
########

This rule checks the port type is lowercase if it is a VHDL keyword.

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

This rule checks the port direction is lowercase.

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

This rule checks for at least one space before the :.

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
