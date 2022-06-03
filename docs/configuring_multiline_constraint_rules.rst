
.. _configuring-multiline-constraint-rules:

Configuring Multiline Constraint Rules
--------------------------------------

There are rules which will check indent and formatting of constraints as part of a subtype_indication:

.. code-block:: text

    subtype_indication ::=
        [ resolution_indication ] type_mark [ constraint ]

    constraint ::=
        range_constraint
      | array_constraint
      | record_constraint

There are separate rules for the structure of the constraint and the indenting.
Both rules are required to ensure proper formatting of multiline constraints.

There are several options to the structure rules:

.. |values| replace::
   add_new_line, remove_new_line, ignore

.. |values2| replace::
   remove_new_line, ignore

.. |values3| replace::
   all_in_one_line, one_line_per_dimension, ignore

.. |green_diamond| image:: img/green_diamond.png

.. |red_penta_star| image:: img/red_penta_star.png

.. |purple_hexa_star| image:: img/purple_hexa_star.png

.. |orange_triangle| image:: img/orange_triangle.png

.. |grey_box| image:: img/grey_box.png

.. |add_new_line| replace::
   The setting "add_new_line" enforces a carriage return (alias "new line") [and, consequently by indentation rules kicking in, also (indirectly) enforces the indentation of the new line]

.. |remove_new_line| replace::
   The setting "remove_new_line" enforces the removal of any potential space and carriage return

.. |ignore| replace::
   The setting "ignore" disables the option and hence no formatting check is done at all: spaces and new lines can be anything

.. |all_in_one_line| replace::
   The setting "all_in_one_line" will combine array_constraints into a single line

.. |one_line_per_dimension| replace::
   The setting "one_line_per_dimension" will place each dimension on it's own line

+-------------------------------+--------------------+-----------+------------------------+----------------------------+
| Option                        | Symbol             | Values    | Structural Element     | Description                |
+===============================+====================+===========+========================+============================+
| record_constraint_open_paren  | |green_diamond|    | |values|  | opening parenthesis    | * |add_new_line|           |
+-------------------------------+--------------------+-----------+------------------------+ * |remove_new_line|        |
| record_constraint_close_paren | |red_penta_star|   | |values|  | closing parenthesis    | * |ignore|                 |
+-------------------------------+--------------------+-----------+------------------------+                            |
| record_constraint_comma       | |purple_hexa_star| | |values2| | comma                  |                            |
+-------------------------------+--------------------+-----------+------------------------+                            |
| record_constraint_element     | |orange_triangle|  | |values|  | new element            |                            |
+-------------------------------+--------------------+-----------+------------------------+----------------------------+
| array_constraint              | |grey_box|         | |values3| | array range indication | * |all_in_one_line|        |
|                               |                    |           |                        | * |one_line_per_dimension| |
|                               |                    |           |                        | * |ignore|                 |
+-------------------------------+--------------------+-----------+------------------------+----------------------------+

.. other table:
.. 
.. +-------------------------------+---------+-----------------+------------------+------------------------+
.. | Option                        |  Type   | Default         | Symbol           | structural element     |
.. +===============================+=========+=================+==================+========================+
.. | record_constraint_open_paren  | string  | add_new_line    | green diamond    | opening parenthesis    |
.. +-------------------------------+---------+-----------------+------------------+------------------------+
.. | record_constraint_close_paren | string  | add_new_line    | red penta-star   | closing_parenthesis    |
.. +-------------------------------+---------+-----------------+------------------+------------------------+
.. | record_constraint_comma       | string  | remove_new_line | purple hexa-star | comma                  |
.. +-------------------------------+---------+-----------------+------------------+------------------------+
.. | record_constraint_element     | string  | add_new_line    | orange triangle  | new element            |
.. +-------------------------------+---------+-----------------+------------------+------------------------+
.. | array_constraint              | string  | all_in_one_line | grey box         | array range indication |
.. +-------------------------------+---------+-----------------+------------------+------------------------+

The following figure illustrates a multiline constraint and where the options will be applied.

.. image:: img/constraints_code.png

.. The options :code:`record_constraint_open_paren`, :code:`record_constraint_close_paren`, and :code:`record_constraint_element` allow for three values:
.. 
.. +----------------------+--------------------------------------------------------------------+
.. | Option Value         | Action                                                             |
.. +======================+====================================================================+
.. | add_new_line         | Adds a carriage return before the structural element.              |
.. +----------------------+--------------------------------------------------------------------+
.. | remove_new_line      | Removes whitespace and carriage returns before structural element. |
.. +----------------------+--------------------------------------------------------------------+
.. | ignore               | Disables the option and no formatting checks will be performed.    |
.. +----------------------+--------------------------------------------------------------------+
.. 
.. The option :code:`record_constraint_comma` allows for two values:
.. 
.. +----------------------+--------------------------------------------------------------------+
.. | Option Value         | Action                                                             |
.. +======================+====================================================================+
.. | remove_new_line      | Removes whitespace and carriage returns before structural element. |
.. +----------------------+--------------------------------------------------------------------+
.. | ignore               | Disables the option and no formatting checks will be performed.    |
.. +----------------------+--------------------------------------------------------------------+
.. 
.. The :code:`array_constraint` option allows the following values:
.. 
.. +------------------------+--------------------------------------------------------------------+
.. | Option Value           | Action                                                             |
.. +========================+====================================================================+
.. | all_in_one_line        | Combine array_constraint into a single line.                       |
.. +------------------------+--------------------------------------------------------------------+
.. | one_line_per_dimension | Place each dimension on it's own line.                             |
.. +------------------------+--------------------------------------------------------------------+
.. | ignore                 | Disables the option and no formatting checks will be performed.    |
.. +------------------------+--------------------------------------------------------------------+


The following configuration replicates the above code snippet.

.. code-block:: yaml

   rule :
     signal_016:
        record_constraint_open_paren : 'add_new_line'
        record_constraint_close_paren : 'add_new_line'
        record_constraint_comma : 'remove_new_line'
        record_constraint_element : 'add_new_line'
        array_constraint : 'all_in_one_line'

.. NOTE:: All examples use the above configuration.

Example: record_constraint_open_paren set to 'remove_new_line'
##############################################################

Setting the `record_constraint_open_paren` option to `remove_new_line` will result in the following formatting:

.. code-block:: vhdl

   signal sig8 : record_type_3(
     element1(7 downto 0),
     element2(4 downto 0)(7 downto 0)(
       elementA(7 downto 0),
       elementB(3 downto 0)
     ),
     element3(3 downto 0)(
       elementC(4 downto 1),
       elementD(1 downto 0)
     ),
     element5(
       elementE(3 downto 0),
       elementF(7 downto 0)
     ),
     element6(4 downto 0),
     element7(7 downto 0)
   );

Example: record_constraint_close_paren set to 'remove_new_line'
###############################################################

Setting the `record_constraint_close_paren` option to `remove_new_line` will result in the following formatting:

.. code-block:: vhdl

   signal sig8 : record_type_3
   (
     element1(7 downto 0),
     element2(4 downto 0)(7 downto 0)
       (
         elementA(7 downto 0),
         elementB(3 downto 0)),
     element3(3 downto 0)
       (
         elementC(4 downto 1),
         elementD(1 downto 0)),
     element5
       (
         elementE(3 downto 0),
         elementF(7 downto 0)),
     element6(4 downto 0),
     element7(7 downto 0));

Example: record_constraint_element set to 'remove_new_line'
###########################################################

Setting the `record_constraint_element` option to `remove_new_line` will result in the following formatting:

.. code-block:: vhdl

   signal sig8 : record_type_3
   (element1(7 downto 0), element2(4 downto 0)(7 downto 0)
       (elementA(7 downto 0), elementB(3 downto 0)
       ), element3(3 downto 0)
       (elementC(4 downto 1), elementD(1 downto 0)
       ), element5
       (elementE(3 downto 0), elementF(7 downto 0)
       ), element6(4 downto 0), element7(7 downto 0)
   );

Example: array_constraint set to 'one_line_per_dimension'
#########################################################

Setting the `array_constraint` option to `one_line_per_dimension` will result in the following formatting:

.. code-block:: vhdl

   signal sig8 : record_type_3
   (
     element1
       (7 downto 0),
     element2
       (4 downto 0)
       (7 downto 0)
       (
         elementA
           (7 downto 0),
         elementB
           (3 downto 0)
       ),
     element3
       (3 downto 0)
       (
         elementC
           (4 downto 1),
         elementD
           (1 downto 0)
       ),
     element5
       (
         elementE
           (3 downto 0),
         elementF
           (7 downto 0)
       ),
     element6
       (4 downto 0),
     element7
       (7 downto 0)
   );

Rules Enforcing Multiline Constraint Rules
##########################################
.. 
.. * `constant_016 <constant_rules.html#constant-016>`_
.. * `signal_016 <signal_rules.html#signal-016>`_
