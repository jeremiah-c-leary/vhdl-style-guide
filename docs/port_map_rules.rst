Port Map Rules
--------------

port_map_001 (instantiation_006)
################################

This rule checks the **port map** keywords have proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   PORT MAP (

**Fix**

.. code-block:: vhdl

   port map (

port_map_002 (instantiation_011)
################################

This rule checks the port name is uppercase.
Indexes on ports will not be uppercased.

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
       WR_EN              => wr_en,
       RD_EN              => rd_en,
       OVERFLOW           => overflow,
       UNDERFLOW(c_index) => underflow
     );

port_map_003 (instantiation_025)
################################

This rule checks the ( is on the same line as the **port map** keywords.

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

port_map_004 (instantiation_007)
################################

This rule checks the closing ) for the port map is on it's own line.

**Violation**

.. code-block:: vhdl

    port map (
      WR_EN => wr_en);

**Fix**

.. code-block:: vhdl

    port map (
      WR_EN => wr_en
    );

port_map_005 (instantiation_020)
################################

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

port_map_007 (instantiation_022)
################################

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

port_map_008 (instantiation_024)
################################

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

port_map_009 (instantiation_021)
################################

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
