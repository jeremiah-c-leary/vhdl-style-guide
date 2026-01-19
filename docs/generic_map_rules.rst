.. include:: includes.rst

Generic Map Rules
-----------------

generic_map_001
###############

|phase_6| |error| |case| |case_keyword|

This rule checks the **generic map** keywords have proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   GENERIC MAP (

**Fix**

.. code-block:: vhdl

   generic map (

generic_map_002
###############

|phase_6| |error| |case| |case_name|

This rule checks generic names have proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

     generic map (
       DEPTH => 512,
       WIDTH => 32
     )

**Fix**

.. code-block:: vhdl

     generic map (
       depth => 512,
       width => 32
     )

generic_map_003
###############

|phase_1| |error| |structure|

This rule checks the ( is on the same line as the **map** keyword.

**Violation**

.. code-block:: vhdl

   generic map
   (
     WIDTH => 32,
     DEPTH => 512
   )

**Fix**

Use explicit port mapping.

.. code-block:: vhdl

   generic map (
     WIDTH => 32,
     DEPTH => 512
   )

generic_map_004
###############

|phase_1| |error| |structure|

This rule checks the location of the closing ")" character for the generic map.

The default location is on a line by itself.

|configuring_move_token_rules_link|

**Violation**

.. code-block:: vhdl

     generic map (
       GENERIC_1 => 0,
       GENERIC_2 => TRUE,
       GENERIC_3 => FALSE)

**Fix**

.. code-block:: vhdl

     generic map (
       GENERIC_1 => 0,
       GENERIC_2 => TRUE,
       GENERIC_3 => FALSE
     )

generic_map_005
###############

|phase_1| |error| |structure|

This rule checks if the **generic map** keywords and a generic assignment are on the same line.

**Violation**

.. code-block:: vhdl

     generic map (DEPTH => 512,
       WIDTH => 32
     )

**Fix**

.. code-block:: vhdl

     generic map (
       DEPTH => 512,
       WIDTH => 32
     )

generic_map_006
###############

|phase_2| |error| |whitespace|

This rule checks for a single space between the **map** keyword and the (.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   generic map(

   generic map   (

**Fix**

.. code-block:: vhdl

   generic map (

   generic map (

generic_map_007
###############

|phase_2| |error| |whitespace|

This rule checks for a single space after the **=>** keyword in generic maps.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   generic map
   (
     WIDTH =>    32,
     DEPTH => 512
   )

**Fix**

.. code-block:: vhdl

   generic map
   (
     WIDTH => 32,
     DEPTH => 512
   )

generic_map_008
###############

|phase_1| |error| |unfixable| |structure|

This rule checks for positional generics.
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
     WR_EN    => WR_EN,
     RD_EN    => RD_EN,
     OVERFLOW => OVERFLOW
   );

generic_map_009
###############

|phase_1| |error| |structure|

This rule checks the **map** keyword is on the same line as the **generic** keyword.

**Violation**

.. code-block:: vhdl

   generic
   map (
     WIDTH => 32,
     DEPTH => 512
   )

**Fix**

Use explicit port mapping.

.. code-block:: vhdl

   generic map (

     WIDTH => 32,
     DEPTH => 512
   )

generic_map_100
###############

|phase_2| |error| |whitespace|

This rules checks for whitespace before the assignment operator.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   generic map (
     WIDTH=> 32,
     DEPTH=> 512
   );

**Fix**

.. code-block:: vhdl

   generic map (
     WIDTH => 32,
     DEPTH => 512
   );

generic_map_101
###############

|phase_2| |error| |whitespace|

This rule checks for a single space between the **generic** keyword and the **map** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   generic       map(

**Fix**

.. code-block:: vhdl

   generic map (

generic_map_201
###############

|phase_3| |error| |blank_line|

This rule checks for blank lines in a generic map.

|configuring_blank_lines_link|

**Violation**

.. code-block:: vhdl

  generic map (
    G_GEN_1 => 3,
    G_GEN_2 => 4,

    G_GEN_3 => 5
  )
  port map (
    PORT_1 => w_port_1,
    PORT_2 => w_port_2,
    PORT_3 => w_port_3
  );

**Fix**

.. code-block:: vhdl

  generic map (
    G_GEN_1 => 3,
    G_GEN_2 => 4,
    G_GEN_3 => 5
  )
  port map (
    PORT_1 => w_port_1,
    PORT_2 => w_port_2,
    PORT_3 => w_port_3
  );

generic_map_300
###############

|phase_4| |error| |indent|

This rule checks for the proper indentation of the **generic** keyword in generic maps.

**Violation**

.. code-block:: vhdl

   U_FIFO : FIFO
       generic map (
       G_GEN1 => g_gen1,
       G_GEN2 => g_gen2,
       G_GEN3 => g_gen3
     );

**Fix**

.. code-block:: vhdl

   U_FIFO : FIFO
     generic map (
       G_GEN1 => g_gen1,
       G_GEN2 => g_gen2,
       G_GEN3 => g_gen3
     );

generic_map_301
###############

|phase_4| |error| |indent|

This rule checks for the proper indentation of association elements in generic maps.

**Violation**

.. code-block:: vhdl

   U_FIFO : FIFO
     generic map (
           G_GEN1 => g_gen1,
   G_GEN2 => g_gen2,
         G_GEN3 => g_gen3
     );

**Fix**

.. code-block:: vhdl

   U_FIFO : FIFO
     generic map (
       G_GEN1 => g_gen1,
       G_GEN2 => g_gen2,
       G_GEN3 => g_gen3
     );

generic_map_302
###############

|phase_4| |error| |indent|

This rule checks for the proper indentation of the closing parenthesis in generic maps.

**Violation**

.. code-block:: vhdl

   U_FIFO : FIFO
     generic map (
       G_GEN1 => g_gen1,
       G_GEN2 => g_gen2,
       G_GEN3 => g_gen3
          );

**Fix**

.. code-block:: vhdl

   U_FIFO : FIFO
     generic map (
       G_GEN1 => g_gen1,
       G_GEN2 => g_gen2,
       G_GEN3 => g_gen3
     );

generic_map_600
###############

|phase_7| |disabled| |error| |unfixable| |naming|

This rule checks for valid suffixes on generic identifiers in generic maps
The default generic suffix is *_g*.

|configuring_prefix_and_suffix_rules_link|

**Violation**

.. code-block:: vhdl

   generic map
   (
     WIDTH => 32,
     DEPTH => 512
   )

**Fix**

.. code-block:: vhdl

   generic map
   (
     WIDTH_G => 32,
     DEPTH_G => 512
   )

generic_map_601
###############

|phase_7| |disabled| |error| |unfixable| |naming|

This rule checks for valid prefixes on generic identifiers in generic maps
The default generic suffix is *g_*.

|configuring_prefix_and_suffix_rules_link|

**Violation**

.. code-block:: vhdl

   generic map
   (
     WIDTH => 32,
     DEPTH => 512
   )

**Fix**

.. code-block:: vhdl

   generic map
   (
     G_WIDTH => 32,
     G_DEPTH => 512
   )
