.. include:: includes.rst

Port Map Rules
--------------

port_map_001
############

|phase_6| |error| |case| |case_keyword|

This rule checks the **port map** keywords have proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   PORT MAP (

**Fix**

.. code-block:: vhdl

   port map (

port_map_002
############

|phase_6| |error| |case| |case_name|

This rule checks the port names have proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

     port map (
       wr_en              => wr_en,
       rd_en              => rd_en,
       OVERFLOW           => overflow,
       underflow(c_index) => underflow
     );

**Fix**

.. code-block:: vhdl

     port map (
       wr_en              => wr_en,
       rd_en              => rd_en,
       overflow           => overflow,
       underflow(c_index) => underflow
     );

port_map_003
############

|phase_1| |error| |structure|

This rule checks the "(" character is on the same line as the **map** keyword.

**Violation**

.. code-block:: vhdl

   port map
   (
     WR_EN    => WR_EN,
     RD_EN    => RD_EN,
     OVERFLOW => OVERFLOW
   );

**Fix**

Use explicit port mapping.

.. code-block:: vhdl

   port map (

     WR_EN    => WR_EN,
     RD_EN    => RD_EN,
     OVERFLOW => OVERFLOW
   );

port_map_004
############

|phase_1| |error| |structure|

This rule checks the location of the closing ")" character for the port map.

The default location is on a line by itself.

|configuring_move_token_rules_link|

**Violation**

.. code-block:: vhdl

    port map (
      WR_EN => wr_en);

**Fix**

.. code-block:: vhdl

    port map (
      WR_EN => wr_en
    );

port_map_005
############

|phase_1| |error| |structure|

This rule checks for a port assignment on the same line as the **port map** keyword.

**Violation**

.. code-block:: vhdl

     port map (WR_EN    => wr_en,
       RD_EN    => rd_en,
       OVERFLOW => overflow
     );

**Fix**

.. code-block:: vhdl

     port map (
       WR_EN    => wr_en,
       RD_EN    => rd_en,
       OVERFLOW => overflow
     );

port_map_006
############

|phase_2| |error| |whitespace|

This rule checks for a single space between the **map** keyword and the (.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   port map(

   port map   (

**Fix**

.. code-block:: vhdl

   port map (

   port map (

port_map_007
############

|phase_2| |error| |whitespace|

This rule checks for a single space after the **=>** operator in port maps.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   U_FIFO : FIFO
     port map (
       WR_EN    =>   wr_en,
       RD_EN    =>rd_en,
       OVERFLOW =>     overflow
     );

**Fix**

.. code-block:: vhdl

   U_FIFO : FIFO
     port map (
       WR_EN    => wr_en,
       RD_EN    => rd_en,
       OVERFLOW => overflow
     );

port_map_008
############

|phase_1| |error| |unfixable| |structure|

This rule checks for positional ports.
Positional ports are subject to problems when the position of the underlying component changes.

**Violation**

.. code-block:: vhdl

   port map (
     WR_EN, RD_EN, OVERFLOW
   );

**Fix**

Use explicit port mapping.

.. code-block:: vhdl

   port map (
     WR_EN    => WR_EN,
     RD_EN    => RD_EN,
     OVERFLOW => OVERFLOW
   );

port_map_009
############

|phase_1| |error| |structure|

This rule checks multiple port assignments on the same line.

**Violation**

.. code-block:: vhdl

   port map (
     WR_EN => w_wr_en, RD_EN => w_rd_en,
     OVERFLOW => w_overflow
   );

**Fix**

.. code-block:: vhdl

   port map (
     WR_EN => w_wr_en,
     RD_EN => w_rd_en,
     OVERFLOW => w_overflow
   );

port_map_010
############

|phase_1| |error| |structure|

This rule checks for comments at the end of the port and generic assignments in instantiations.
These comments represent additional maintenance.
They will be out of sync with the entity at some point.
Refer to the entity for port types, port directions and purpose.

**Violation**

.. code-block:: vhdl

   WR_EN => w_wr_en;   -- out : std_logic
   RD_EN => w_rd_en;   -- Reads data when asserted

**Fix**

.. code-block:: vhdl

   WR_EN => w_wr_en;
   RD_EN => w_rd_en;

port_map_011
############

|phase_1| |error| |structure|

This rule checks the **map** keyword is on the same line as the **port** keyword.

**Violation**

.. code-block:: vhdl

   port
   map (
     WR_EN    => WR_EN,
     RD_EN    => RD_EN,
     OVERFLOW => OVERFLOW
   );

**Fix**

Use explicit port mapping.

.. code-block:: vhdl

   port map (

     WR_EN    => WR_EN,
     RD_EN    => RD_EN,
     OVERFLOW => OVERFLOW
   );

port_map_100
############

|phase_2| |error| |whitespace|

This rules checks for whitespace before the assignment operator.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   port map (
     WR_EN=> w_wr_en,
     RD_EN=> w_rd_en,
     OVERFLOW => w_overflow
   );

**Fix**

.. code-block:: vhdl

   port map (
     WR_EN => w_wr_en,
     RD_EN => w_rd_en,
     OVERFLOW => w_overflow
   );

port_map_101
############

|phase_2| |error| |whitespace|

This rule checks for a single space between the **port** keyword and the **map** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   port   map (

**Fix**

.. code-block:: vhdl

   port map (

port_map_200
############

|phase_3| |error| |blank_line|

This rule checks for a blank line below the open parenthesis in a port map.

|configuring_blank_lines_link|

**Violation**

.. code-block:: vhdl

  port map (

    WR_EN => w_wr_en,
    RD_EN => w_rd_en,
    OVERFLOW => w_overflow
  );

**Fix**

.. code-block:: vhdl

  port map (
    WR_EN => w_wr_en,
    RD_EN => w_rd_en,
    OVERFLOW => w_overflow
  );

port_map_201
############

|phase_3| |error| |blank_line|

This rule checks for blank lines in a port map.

|configuring_blank_lines_link|

**Violation**

.. code-block:: vhdl

  port map (
    WR_EN => w_wr_en,

    RD_EN => w_rd_en,
    OVERFLOW => w_overflow
  );

**Fix**

.. code-block:: vhdl

  port map (
    WR_EN => w_wr_en,
    RD_EN => w_rd_en,
    OVERFLOW => w_overflow
  );


port_map_300
############

|phase_4| |error| |indent|

This rule checks for the proper indentation of the **port** keyword in port maps.

**Violation**

.. code-block:: vhdl

   U_FIFO : FIFO
       port map (
       WR_EN    => wr_en,
       RD_EN    => rd_en,
       OVERFLOW => overflow
     );

**Fix**

.. code-block:: vhdl

   U_FIFO : FIFO
     port map (
       WR_EN    => wr_en,
       RD_EN    => rd_en,
       OVERFLOW => overflow
     );

port_map_301
############

|phase_4| |error| |indent|

This rule checks for the proper indentation of association elements in port maps.

**Violation**

.. code-block:: vhdl

   U_FIFO : FIFO
     port map (
           WR_EN    => wr_en,
   RD_EN    => rd_en,
         OVERFLOW => overflow
     );

**Fix**

.. code-block:: vhdl

   U_FIFO : FIFO
     port map (
       WR_EN    => wr_en,
       RD_EN    => rd_en,
       OVERFLOW => overflow
     );

port_map_302
############

|phase_4| |error| |indent|

This rule checks for the proper indentation of the closing parenthesis in port maps.

**Violation**

.. code-block:: vhdl

   U_FIFO : FIFO
     port map (
       WR_EN    => wr_en,
       RD_EN    => rd_en,
       OVERFLOW => overflow
          );

**Fix**

.. code-block:: vhdl

   U_FIFO : FIFO
     port map (
       WR_EN    => wr_en,
       RD_EN    => rd_en,
       OVERFLOW => overflow
     );
