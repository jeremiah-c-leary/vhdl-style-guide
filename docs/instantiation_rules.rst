Instantiation Rules
-------------------

instantiation_014
#################

This rule checks for the closing parenthesis *);* on generic maps are on their own line.
Having the parenthesis on it's own line makes the deliniation clearer between the generic map and the port map.

**Violation**

.. code-block:: vhdl

   INSTANCE_NAME : ENTITY_NAME
     generic_map (
       GENERIC_1 => 0,
       GENERIC_2 => TRUE,
       GENERIC_3 => FALSE);

**Fix**

.. code-block:: vhdl

   INSTANCE_NAME : ENTITY_NAME
     generic_map (
       GENERIC_1 => 0,
       GENERIC_2 => TRUE,
       GENERIC_3 => FALSE
     );

instantiation_021
#################

This rule checks multiple port assignments on the same line.
Placing each port assignment on it's own line enhanced clarity.

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


instantiation_023
#################

This rule checks for comments at the end of the port and generic assignments in instantiations.
These comments represent additional maintainence.
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

instantiation_024
#################

This rule checks for positional generics and ports.
Positional ports and generics are subject to problems when the position of the underlying component changes.

**Violation**

.. code-block:: vhdl

   port map (
     WR_EN, RD_EN, OVERFLOW
   );

**Fix**

Use explicit port mapping.

.. code-block:: vhdl

   port map (
     WR_EN    => WR_EN;
     RD_EN    => RD_EN;
     OVERFLOW => OVERFLOW
   );

