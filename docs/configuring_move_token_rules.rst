
.. _configuring-move-token-rules:

Configuring Move Token Rules
----------------------------

There are rules which will move tokens around to help with the structure of the code.

There is one option for these rules:

.. |new_line| replace::
   :code:`new_line`

.. |move_left| replace::
   :code:`move_left`

.. |action| replace::
   :code:`action`

.. |action__new_line| replace::
   |new_line| = Token will be moved to the next line.

.. |action__move_left| replace::
   |move_left| = Token will be moved left to the next non whitespace token.

.. |values_action| replace::
   |new_line|, |move_left|

+--------------------------------------+-----------------+------------+------------------------------------------------+
| Option                               |   Values        | Default    | Description                                    |
+======================================+=================+============+================================================+
| |action|                             | |values_action| | |new_line| | * |action__new_line|                           |
|                                      |                 |            | * |action__move_left|                          |
+--------------------------------------+-----------------+------------+------------------------------------------------+

This is an example of how to configure the option.

.. code-block:: yaml

   rule :
     port_map_004:
        action: 'new_line'

.. NOTE:: All examples below are using the rule **port_map_004**.

Example: |action| set to |new_line|
###################################

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

Example: |action| set to |move_left|
####################################

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
