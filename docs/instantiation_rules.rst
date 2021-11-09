.. include:: icons.rst

Instantiation Rules
-------------------

instantiation_001
#################

|phase_4| |error| |indent|

This rule checks for the proper indentation of instantiations.

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

instantiation_002
#################

|phase_2| |error| |whitespace|

This rule checks for a single space after the colon.

**Violation**

.. code-block:: vhdl

   U_FIFO :FIFO

**Fix**

.. code-block:: vhdl

   U_FIFO : FIFO

instantiation_003
#################

|phase_2| |error| |whitespace|

This rule checks for a single space before the colon.

**Violation**

.. code-block:: vhdl

   U_FIFO: FIFO

**Fix**

.. code-block:: vhdl

   U_FIFO : FIFO

instantiation_004
#################

|phase_3| |error| |blank_line|

This rule checks for blank lines or comments above the instantiation.

Refer to `Configuring Previous Line Rules <configuring.html#configuring-previous-line-rules>`_ for options.

The default style is :code:`no_code`.

**Violation**

.. code-block:: vhdl

   WR_EN <= '1';
   U_FIFO : FIFO

   -- Instantiate another FIFO
   U_FIFO2 : FIFO

**Fix**

.. code-block:: vhdl

   WR_EN <= '1';

   U_FIFO : FIFO

   -- Instantiate another FIFO
   U_FIFO2 : FIFO

instantiation_005
#################

|phase_1| |error|

This rule checks the **port map** keywords are on their own line.

**Violation**

.. code-block:: vhdl

   U_FIFO : FIFO port map (

**Fix**

.. code-block:: vhdl

   U_FIFO : FIFO
     port map (

instantiation_006
#################

This rule has been renamed to `port_map_001 <port_map_rules.html#port-map-001>`_.

instantiation_007
#################

This rule has been renamed to `port_map_004 <port_map_rules.html#port-map-004>`_.

instantiation_008
#################

|phase_6| |error|

This rule checks the instance label has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   U_FIFO : fifo

**Fix**

.. code-block:: vhdl

   u_fifo : fifo

instantiation_009
#################

|phase_6| |error|

This rule checks the component name has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   u_fifo : FIFO


**Fix**

.. code-block:: vhdl

   u_fifo : fifo

instantiation_010
#################

|phase_5| |error|

This rule checks the alignment of the **=>** operator for each generic and port in the instantiation.

Following extra configurations are supported:

* :code:`separate_generic_port_alignment`.

Refer to the section `Configuring Keyword Alignment Rules <configuring.html#configuring-keyword-alignment-rules>`_ for information on changing the configurations.

**Violation**

.. code-block:: vhdl

   U_FIFO : FIFO
     generic map (
       g_width => 8,
       g_delay    => 2
     )
     port map (
       wr_en => wr_en,
       rd_en => rd_en,
       overflow => overflow
     );

**Fix**

.. code-block:: vhdl

   U_FIFO : FIFO
     generic map (
       g_width => 8,
       g_delay => 2
     )
     port map (
       wr_en    => wr_en,
       rd_en    => rd_en,
       overflow => overflow
     );

instantiation_011
#################

This rule has been renamed to `port_map_002 <port_map_rules.html#port-map-002>`_.

instantiation_012
#################

|phase_1| |error|

This rule checks the instantiation declaration and the **generic map** keywords are not on the same line.

**Violation**

.. code-block:: vhdl

   U_FIFO : FIFO generic map (

**Fix**

.. code-block:: vhdl

   U_FIFO : FIFO
     generic map (

instantiation_013
#################

This rule has been renamed to `generic_map_001 <generic_map_rules.html#generic-map-001>`_.

instantiation_014
#################

This rule has been renamed to `generic_map_004 <generic_map_rules.html#generic-map-004>`_.

instantiation_016
#################

This rule has been renamed to `generic_map_002 <generic_map_rules.html#generic-map-002>`_.

instantiation_017
#################

This rule has been renamed to `generic_map_005 <generic_map_rules.html#generic-map-005>`_.

instantiation_018
#################

This rule has been renamed to `generic_map_006 <generic_map_rules.html#generic-map-006>`_.

instantiation_019
#################

|phase_3| |error| |blank_line|

This rule checks for a blank line below the end of the instantiation declaration.

Refer to the section `Configuring Blank Lines <configuring.html#configuring-blank-lines>`_ for options regarding comments.

**Violation**

.. code-block:: vhdl

   U_FIFO : FIFO
     port map (
       WR_EN    => wr_en,
       RD_EN    => rd_en,
       OVERFLOW => overflow
     );
   U_RAM : RAM

**Fix**

.. code-block:: vhdl

   U_FIFO : FIFO
     port map (
       WR_EN    => wr_en,
       RD_EN    => rd_en,
       OVERFLOW => overflow
     );

   U_RAM : RAM

instantiation_020
#################

This rule has been renamed to `port_map_005 <port_map_rules.html#port-map-005>`_.

instantiation_021
#################

This rule has been renamed to `port_map_009 <port_map_rules.html#port-map-009>`_.

instantiation_022
#################

This rule has been renamed to `port_map_007 <port_map_rules.html#port-map-007>`_.

instantiation_023
#################

|phase_1| |error|

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

This rule has been split into:

* `generic_map_008 <generic_map_rules.html#generic-map-008>`_
* `port_map_008 <port_map_rules.html#port-map-008>`_

instantiation_025
#################

This rule has been renamed to `port_map_003 <port_map_rules.html#port-map-003>`_.

instantiation_026
#################

This rule has been renamed to `generic_map_003 <generic_map_rules.html#generic-map-003>`_.

instantiation_027
#################

|phase_6| |error|

This rule checks the **entity** keyword has proper case in direct instantiations.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   INSTANCE_NAME : ENTITY library.ENTITY_NAME

**Fix**

.. code-block:: vhdl

   INSTANCE_NAME : entity library.ENTITY_NAME

instantiation_028
#################

|phase_6| |error|

This rule checks the entity name has proper case in direct instantiations.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   instance_name : entity library.ENTITY_NAME

**Fix**

.. code-block:: vhdl

   instance_name : entity library.entity_name

instantiation_029
#################

|phase_5| |error|

This rule checks for alignment of inline comments in an instantiation.

Following extra configurations are supported:

* :code:`separate_generic_port_alignment`.

Refer to the section `Configuring Keyword Alignment Rules <configuring.html#configuring-keyword-alignment-rules>`_ for information on changing the configurations.
**Violation**

**Violation**

.. code-block:: vhdl

       wr_en    => write_enable,        -- Wrte enable
       rd_en    => read_enable,    -- Read enable
       overflow => overflow,         -- FIFO has overflowed

**Fix**

.. code-block:: vhdl

       wr_en    => write_enable, -- Wrte enable
       rd_en    => read_enable,  -- Read enable
       overflow => overflow,     -- FIFO has overflowed

instantiation_030
#################

This rule has been renamed to `generic_map_007 <generic_map_rules.html#generic-map-007>`_.

instantiation_031
#################

|phase_6| |error|

This rule checks the component keyword has proper case in component instantiations that use the **component** keyword.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   instance_name : COMPONENT entity_name

**Fix**

.. code-block:: vhdl

   instance_name : component entity_name

instantiation_032
#################

|phase_2| |error| |whitespace|

This rule checks for a single space after the **component** keyword if it is used.

**Violation**

.. code-block:: vhdl

   INSTANCE_NAME : component ENTITY_NAME
   INSTANCE_NAME : component   ENTITY_NAME
   INSTANCE_NAME : component  ENTITY_NAME

**Fix**

.. code-block:: vhdl

   INSTANCE_NAME : component ENTITY_NAME
   INSTANCE_NAME : component ENTITY_NAME
   INSTANCE_NAME : component ENTITY_NAME

instantiation_033
#################

|phase_1| |error|

This rule checks for the **component** keyword for a component instantiation.

Refer to the section `Configuring Optional Items <configuring.html#configuring-optional-items>`_ for options.

**Violation**

.. code-block:: vhdl

   INSTANCE_NAME : ENTITY_NAME

**Fix**

.. code-block:: vhdl

   INSTANCE_NAME : component ENTITY_NAME

instantiation_034
#################

|phase_1| |error|

This rule checks for component versus direct instantiations.

Refer to the section `Configuring Type of Instantiation <configuring.html#configuring-type-of-instantiations>`_ for options to configure the allowed configuration.

component instantiation
^^^^^^^^^^^^^^^^^^^^^^^

.. NOTE:: This is the default configuration

**Violation**

.. code-block:: vhdl

   U_FIFO : entity fifo_dsn.FIFO(RTL)


entity instantiation
^^^^^^^^^^^^^^^^^^^^

**Violation**

.. code-block:: vhdl

   U_FIFO : component FIFO

   U_FIFO : FIFO

instantiation_600
#################

|phase_7| |disabled| |error|

This rule checks for valid suffixes on instantiation labels.
The default suffix is *_inst*.

Refer to the section `Configuring Prefix and Suffix Rules <configuring.html#configuring-prefix-and-suffix-rules>`_ for information on changing the allowed suffixes.

**Violation**

.. code-block:: vhdl

   fifo_32x2k : FIFO

**Fix**

.. code-block:: vhdl

   fifo_32x2k_inst : FIFO

instantiation_601
#################

|phase_7| |disabled| |error|

This rule checks for valid prefixes on instantiation labels.
The default prefix is *inst_*.

Refer to the section `Configuring Prefix and Suffix Rules <configuring.html#configuring-prefix-and-suffix-rules>`_ for information on changing the allowed prefixes.

**Violation**

.. code-block:: vhdl

   fifo_32x2k : FIFO

**Fix**

.. code-block:: vhdl

   inst_fifo_32x2k : FIFO

