.. include:: icons.rst

Generic Rules
-------------

generic_001
###########

|phase_3| |error| |blank_line|

This rule checks for blank lines above the **generic** keyword.

**Violation**

.. code-block:: vhdl

   entity fifo is



     generic (

**Fix**

.. code-block:: vhdl

   entity fifo is
     generic (

generic_002
###########

|phase_4| |error| |indent|

This rule checks the indent of the **generic** keyword.

**Violation**

.. code-block:: vhdl

   entity fifo is
        generic (

   entity fifo is
   generic (

**Fix**

.. code-block:: vhdl

   entity fifo is
     generic (

   entity fifo is
     generic (

generic_003
###########

|phase_2| |error| |whitespace|

This rule checks for a single space between the **generic** keyword and the (.

**Violation**

.. code-block:: vhdl

   generic    (

   generic(

**Fix**

.. code-block:: vhdl

   generic (

   generic (

generic_004
###########

|phase_4| |error| |indent|

This rule checks the indent of generic declarations.

**Violation**

.. code-block:: vhdl

   generic (
   g_width : integer := 32;
          g_depth : integer := 512
   )

**Fix**

.. code-block:: vhdl

   generic (
     g_width : integer := 32;
     g_depth : integer := 512
   )

generic_005
###########

|phase_2| |error| |whitespace|

This rule checks for a single space after the colon in a generic declaration.

**Violation**

.. code-block:: vhdl

   g_width :integer := 32;

**Fix**

.. code-block:: vhdl

   g_width : integer := 32;

generic_006
###########

|phase_2| |error| |whitespace|

This rule checks for a single space after the default assignment.

**Violation**

.. code-block:: vhdl

   g_width : integer :=32;
   g_depth : integer :=     512;

**Fix**

.. code-block:: vhdl

   g_width : integer := 32;
   g_depth : integer := 512;

generic_007
###########

|phase_6| |error|

This rule checks the generic names have proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   G_WIDTH : integer := 32;

**Fix**

.. code-block:: vhdl

   g_width : integer := 32;

generic_008
###########

|phase_4| |error| |indent|

This rule checks the indent of the closing parenthesis.

**Violation**

.. code-block:: vhdl

   g_depth : integer := 512
   );

**Fix**

.. code-block:: vhdl

     g_depth : integer := 512
   );

generic_009
###########

|phase_6| |error|

This rule checks the **generic** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   GENERIC (

**Fix**

.. code-block:: vhdl

   generic (

generic_010
###########

|phase_1| |error|

This rule checks the closing parenthesis is on a line by itself.

**Violation**

.. code-block:: vhdl

   g_depth : integer := 512);

**Fix**

.. code-block:: vhdl

     g_depth : integer := 512
   );

generic_013
###########

|phase_1| |error|

This rule checks for the **generic** keyword on the same line as a generic declaration.

**Violation**

.. code-block:: vhdl

   generic (g_depth : integer := 512;

**Fix**

.. code-block:: vhdl

   generic (
     g_depth : integer := 512;

generic_014
###########

|phase_2| |error|

This rule checks for at least a single space before the colon.

**Violation**

.. code-block:: vhdl

   g_address_width: integer := 10;
   g_data_width : integer := 32;
   g_depth: integer := 512;

**Fix**

.. code-block:: vhdl

   g_address_width : integer := 10;
   g_data_width : integer := 32;
   g_depth : integer := 512;

generic_016
###########

|phase_1| |error|

This rule checks for multiple generics defined on a single line.

**Violation**

.. code-block:: vhdl

  generic (
    g_width : std_logic := '0';g_depth : std_logic := '1'
  );

**Fix**

.. code-block:: vhdl

  generic (
    g_width : std_logic := '0';
    g_depth : std_logic := '1'
  );

generic_017
###########

|phase_6| |error|

This rule checks the generic type has proper case if it is a VHDL keyword.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

  generic (
    g_width : STD_LOGIC := '0';
    g_depth : Std_logic := '1'
  );

**Fix**

.. code-block:: vhdl

  generic (
    g_width : std_logic := '0';
    g_depth : std_logic := '1'
  );

generic_018
###########

|phase_1| |error|

This rule checks the **generic** keyword is on the same line as the (.

**Violation**

.. code-block:: vhdl

  generic
   (

**Fix**

.. code-block:: vhdl

  generic (

generic_019
###########

|phase_3| |error| |blank_line|

This rule checks for blank lines before the ); of the generic declaration.

**Violation**

.. code-block:: vhdl

  generic (
    g_width : std_logic := '0';
    g_depth : Std_logic := '1'


  );

**Fix**

.. code-block:: vhdl

  generic (
    g_width : std_logic := '0';
    g_depth : Std_logic := '1'
  );

generic_020
###########

|phase_7| |disabled| |error|

This rule checks for valid prefixes on generic identifiers.
The default generic prefix is *g\_*.

Refer to the section `Configuring Prefix and Suffix Rules <configuring.html#configuring-prefix-and-suffix-rules>`_ for information on changing the allowed prefixes.

**Violation**

.. code-block:: vhdl

   generic(my_generic : integer);

**Fix**

.. code-block:: vhdl

   generic(g_my_generic : integer);

generic_600
###########

|phase_7| |disabled| |error|

This rule checks for valid suffixes on generic identifiers.
The default generic suffix is *\_g*.

Refer to the section `Configuring Prefix and Suffix Rules <configuring.html#configuring-prefix-and-suffix-rules>`_ for information on changing the allowed suffixes.

**Violation**

.. code-block:: vhdl

   generic(my_generic : integer);

**Fix**

.. code-block:: vhdl

   generic(my_generic_g : integer);

