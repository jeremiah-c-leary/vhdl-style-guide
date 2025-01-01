
.. _configuring-port-map-new-line:

Configuring Port Map New Line
-----------------------------

There is a rule which will check for new lines before the **port** keyword in port map aspects relative to what preceded it.

.. code-block:: text

    block_header ::=
        [ generic_clause [ generic_map_aspect ; ] ]
        [ port_clause [ port_map_aspect ; ] ]

    component_instantiation_statement ::=
        instantiation_label :
            instantiated_unit
                [ generic_map_aspect ]
                [ port_map_aspect ]

There are separate rules for the structure of the constraint and the indenting.
Both rules are required to ensure proper formatting of multiline constraints.

There are several options to the structure rules:

.. |values| replace::
   :code:`add_new_line`, :code:`remove_new_line`

.. |add_new_line| replace::
   The setting :code:`add_new_line` enforces a carriage return (alias "new line") [and, consequently by indentation rules kicking in, also (indirectly) enforces the indentation of the new line]

.. |remove_new_line| replace::
   The setting :code:`remove_new_line` enforces the removal of any potential space and carriage return

.. |default_value| replace::
   :code:`add_new_line`

+---------------------------------------+-----------+----------------------------+----------------------------+
| Option                                | Values    | Default Value              | Description                |
+=======================================+===========+============================+============================+
| :code:`after_port_clause`             | |values|  | |default_value|            | * |add_new_line|           |
+---------------------------------------+           |                            | * |remove_new_line|        |
| :code:`after_instantiated_unit`       |           |                            |                            |
+---------------------------------------+           |                            |                            |
| :code:`after_generic_map_aspect`      |           |                            |                            |
+---------------------------------------+-----------+----------------------------+----------------------------+

Example: :code:`after_port_clause` set to :code:`remove_new_line`
#################################################################

Setting the :code:`after_port_clause` option to :code:`remove_new_line` will result in the following formatting:

.. code-block:: vhdl

    port (
    ); port map (
    )

Example: :code:`after_port_clause` set to :code:`add_new_line`
##############################################################

Setting the :code:`after_port_clause` option to :code:`add_new_line` will result in the following formatting:

.. code-block:: vhdl

   port (
   );
   port map (
   )

Example: :code:`after_instantiated_unit` set to :code:`remove_new_line`
#######################################################################

Setting the :code:`after_instantiated_unit` option to :code:`remove_new_line` will result in the following formatting:

.. code-block:: vhdl

   U_FIFO : FIFO port map (
   )

Example: :code:`after_instantiated_unit` set to :code:`add_new_line`
####################################################################

Setting the :code:`after_instantiated_unit` option to :code:`add_new_line` will result in the following formatting:

.. code-block:: vhdl

   U_FIFO : FIFO
   port map (
   )

Example: :code:`after_generic_map_aspect` set to :code:`remove_new_line`
########################################################################

Setting the :code:`after_generic_map_aspect` option to :code:`remove_new_line` will result in the following formatting:

.. code-block:: vhdl

   generic map (
   ) port map (
   )

Example: :code:`after_generic_map_aspect` set to :code:`add_new_line`
#####################################################################

Setting the :code:`after_generic_map_aspect` option to :code:`add_new_line` will result in the following formatting:

.. code-block:: vhdl

   generic map (
   )
   port map (
   )

Rules Enforcing This Configuration
##################################

* `instantiation_005 <instantiation_rules.html#instantiation-005>`_
