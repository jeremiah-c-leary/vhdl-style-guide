.. include:: icons.rst

Port Map Rules
--------------

port_map_001
############

|phase_6| |error| |case| |case_keyword|

This rule checks the **port map** keywords have proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

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

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

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

This rule checks the "(" character is on the same line as the **port map** keywords.

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

Refer to the section `Configuring Move Token Rules <configuring_move_token_rules.html>`_ for information on options.

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

port_map_007
############

|phase_2| |error| |whitespace|

This rule checks for a single space after the **=>** operator in port maps.

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

|phase_1| |error| |structure|

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

