.. include:: includes.rst

Instantiation Rules
-------------------

instantiation_001
#################

This rule has been split into the following rules:

* :ref:`instantiation_300`
* :ref:`generic_map_300`
* :ref:`generic_map_301`
* :ref:`generic_map_302`
* :ref:`port_map_300`
* :ref:`port_map_301`
* :ref:`port_map_302`

instantiation_002
#################

|phase_2| |error| |whitespace|

This rule checks for a single space after the colon.

|configuring_whitespace_rules_link|

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

|configuring_whitespace_rules_link|

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

|configuring_previous_line_rules_link|

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

|phase_1| |error| |structure|

This rule checks the **port map** keywords are on their own line.

|configuring_port_map_new_line_link|

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

|phase_6| |error| |case| |case_label|

This rule checks the instance label has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   U_FIFO : fifo

**Fix**

.. code-block:: vhdl

   u_fifo : fifo

instantiation_009
#################

|phase_6| |error| |case| |case_name|

This rule checks the component name has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   u_fifo : FIFO


**Fix**

.. code-block:: vhdl

   u_fifo : fifo

instantiation_010
#################

|phase_5| |error| |alignment|

This rule checks the alignment of the **=>** operator for each generic and port in the instantiation.

Following extra configurations are supported:

* :code:`separate_generic_port_alignment`.

|configuring_keyword_alignment_rules_link|

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

|phase_1| |error| |structure|

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

This rule was deprecated and replaced with rules:

* `generic_map_006 <generic_map_rules.html#generic-map-006>`_.
* `port_map_006 <port_map_rules.html#port-map-006>`_.

instantiation_019
#################

|phase_3| |error| |blank_line|

This rule checks for a blank line below the end of the instantiation declaration.

|configuring_blank_lines_link|

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

This rule has been renamed to `port_map_010 <port_map_rules.html#port-map-010>`_.

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

|phase_6| |error| |case| |case_keyword|

This rule checks the **entity** keyword has proper case in direct instantiations.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   INSTANCE_NAME : ENTITY library.ENTITY_NAME

**Fix**

.. code-block:: vhdl

   INSTANCE_NAME : entity library.ENTITY_NAME

instantiation_028
#################

|phase_6| |error| |case| |case_name|

This rule checks the entity name has proper case in direct instantiations.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   instance_name : entity library.ENTITY_NAME

**Fix**

.. code-block:: vhdl

   instance_name : entity library.entity_name

instantiation_029
#################

|phase_5| |error| |alignment|

This rule checks for alignment of inline comments in an instantiation.

Following extra configurations are supported:

* :code:`separate_generic_port_alignment`.

|configuring_keyword_alignment_rules_link|
**Violation**

**Violation**

.. code-block:: vhdl

       wr_en    => write_enable,        -- Write enable
       rd_en    => read_enable,    -- Read enable
       overflow => overflow,         -- FIFO has overflowed

**Fix**

.. code-block:: vhdl

       wr_en    => write_enable, -- Write enable
       rd_en    => read_enable,  -- Read enable
       overflow => overflow,     -- FIFO has overflowed

instantiation_030
#################

This rule has been renamed to `generic_map_007 <generic_map_rules.html#generic-map-007>`_.

instantiation_031
#################

|phase_6| |error| |case| |case_keyword|

This rule checks the **component** keyword has proper case in component instantiations that use the **component** keyword.

|configuring_uppercase_and_lowercase_rules_link|

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

|configuring_whitespace_rules_link|

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

|phase_1| |error| |structure| |structure_optional|

This rule checks for the **component** keyword for a component instantiation.

|configuring_optional_items_link|

**Violation**

.. code-block:: vhdl

   INSTANCE_NAME : ENTITY_NAME

**Fix**

.. code-block:: vhdl

   INSTANCE_NAME : component ENTITY_NAME

instantiation_034
#################

|phase_1| |error| |unfixable| |structure|

This rule checks for component versus direct instantiations.

|configuring_type_of_instantiations_link|

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

instantiation_035
#################

|phase_1| |error| |structure|

This rule checks the semicolon is not on its own line.

**Violation**

.. code-block:: vhdl

   U_FIFO : FIFO
     port map (
       A => B,
       B => C)
     ;

**Fix**

.. code-block:: vhdl

   U_FIFO : FIFO
     port map (
       A => B,
       B => C);

instantiation_036
#################

|phase_1| |error| |unfixable| |structure| |structure_optional|

This rule checks for the optional architecture specification in entity instantiations.

The default action is "add".

|configuring_optional_items_link|

**Violation**

.. code-block:: vhdl

   cmp_test : entity work.my_module;

**Fix**

.. code-block:: vhdl

   cmp_test : entity work.my_module(rtl);

instantiation_300
#################

|phase_4| |error| |indent|

This rule checks for the proper indentation of instantiations.

**Violation**

.. code-block:: vhdl

   count <= val;
       U_FIFO : FIFO
     port map (
       WR_EN    => wr_en,
       RD_EN    => rd_en,
       OVERFLOW => overflow
     );

**Fix**

.. code-block:: vhdl

   count <= val;
   U_FIFO : FIFO
     port map (
       WR_EN    => wr_en,
       RD_EN    => rd_en,
       OVERFLOW => overflow
     );

instantiation_500
#################

|phase_6| |error| |case| |case_name|

This rule checks the component library name has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   u_fifo : entity WORK.FIFO

**Fix**

.. code-block:: vhdl

   u_fifo : entity work.FIFO

instantiation_600
#################

|phase_7| |disabled| |error| |unfixable| |naming|

This rule checks for valid suffixes on instantiation labels.
The default suffix is *_inst*.

|configuring_prefix_and_suffix_rules_link|

**Violation**

.. code-block:: vhdl

   fifo_32x2k : FIFO

**Fix**

.. code-block:: vhdl

   fifo_32x2k_inst : FIFO

instantiation_601
#################

|phase_7| |disabled| |error| |unfixable| |naming|

This rule checks for valid prefixes on instantiation labels.
The default prefix is *inst_*.

|configuring_prefix_and_suffix_rules_link|

**Violation**

.. code-block:: vhdl

   fifo_32x2k : FIFO

**Fix**

.. code-block:: vhdl

   inst_fifo_32x2k : FIFO
