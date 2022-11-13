
.. _configuring-move-token-rules:

Configuring Move Token Rules
----------------------------

There are rules which will move tokens around to help with the structure of the code.

There are several options to these rules:

+----------------------+---------+-------------+--------------------------------------------------------------------------+
| Method               |   Type  | Default     | Description                                                              |
+======================+=========+=============+==========================================================================+
| action               | string  | 'new_line'  | 'new_line' = Token will be moved to the next line.                       |
|                      |         |             | 'move_left' = Token will be moved left to the next non whitespace token. |
+----------------------+---------+-------------+--------------------------------------------------------------------------+

.. NOTE:: All examples below are using the rule **port_map_004**.

Example: 'new_line'
###################

The following code would fail with this option:

.. code-Block:: vhdl

    U_INST : FIFO
      port map (
        A => B,
        B => C);

The following code would pass with this option:

.. code-block:: vhdl

    U_INST : FIFO
      port map (
        A => B,
        B => C
      );

Example: 'move_left'
####################

The following code would fail with this option:

.. code-block:: vhdl

    U_INST : FIFO
      port map (
        A => B,
        B => C
      );

The following code would pass with this option:

.. code-Block:: vhdl

    U_INST : FIFO
      port map (
        A => B,
        B => C);

Rules Enforcing Move Token
##########################

* `generic_010 <generic_rules.html#generic-010>`_
* `generic_map_004 <generic_map_rules.html#generic-map-004>`_
* `port_014 <port_rules.html#port-014>`_
* `port_map_004 <port_map_rules.html#port-map-004>`_
* `record_type_definition_001 <record_type_definition_rules.html#record-type-definition-001>`_
