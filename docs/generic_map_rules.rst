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

This rule checks the ( is on the same line as the **generic map** keywords.

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

|phase_1| |error| |structure|

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

generic_map_600
###############

|phase_7| |disabled| |error| |naming|

This rule checks for valid suffixes on generic identifiers in generic maps
The default generic suffix is *\_g*.

Refer to the section `Configuring Prefix and Suffix Rules <configuring.html#configuring-prefix-and-suffix-rules>`_ for information on changing the allowed suffixes.

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

|phase_7| |disabled| |error| |naming|

This rule checks for valid prefixes on generic identifiers in generic maps
The default generic suffix is *\g_*.

Refer to the section `Configuring Prefix and Suffix Rules <configuring.html#configuring-prefix-and-suffix-rules>`_ for information on changing the allowed suffixes.

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

