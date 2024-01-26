
.. _configuring-subprogram-specification-statement-rules:

Configuring Subprogram Specification Statement Rules
-----------------------------------------------------

There are rules which will check indent and formatting of the subprogram specification of a :code:`procedure` or :code:`function`:

.. code-block:: text

    subprogram_specification ::=
        procedure designator [ ( formal_parameter_list ) ]
        | [ pure | impure ] function designator [ ( formal_parameter_list ) ]
            return type_mark

    designator ::= identifier | operator_symbol

    formal_parameter_list ::= parameter_interface_list

    interface_list ::=
        interface_element { ; interface_element }

    interface_element ::= interface_declaration

There are separate rules for the structure of the subprogram specification and the indenting.
Both rules are required to ensure proper formatting of subprogram specification statements.

There are several options to the structure rules:

.. |values| replace::
   :code:`add_new_line`, :code:`remove_new_line`, :code:`ignore`

.. |values2| replace::
   :code:`remove_new_line`, :code:`ignore`

.. |values3| replace::
   :code:`yes`, :code:`no`

.. |no| replace::
   :code:`no`

.. |green_diamond| image:: img/green_diamond.png

.. |red_penta_star| image:: img/red_penta_star.png

.. |orange_triangle| image:: img/orange_triangle.png

.. |add_new_line| replace::
   The setting :code:`add_new_line` enforces a carriage return (alias "new line") [and, consequently by indentation rules kicking in, also (indirectly) enforces the indentation of the new line]

.. |remove_new_line| replace::
   The setting :code:`remove_new_line` enforces the removal of any potential space and carriage return

.. |ignore| replace::
   The setting :code:`ignore` disables the option and hence no formatting check is done at all: spaces and new lines can be anything

.. |default_add_new_line| replace::
   :code:`add_new_line`

.. |default_remove_new_line| replace::
   :code:`remove_new_line`

.. |default_ignore| replace::
   :code:`ignore`

.. |ignore_single_line| replace::
   :code:`ignore_single_line`

.. |ignore_single_line__yes| replace::
   :code:`yes` = Ignore single line expressions.

.. |ignore_single_line__no| replace::
   :code:`no` =  Apply rules to single line expressions.

+----------------------------------+-----------+---------------------+---------------------------+-----------------------------+
| Option                           | Values    | Structural Element  | Default Value             | Description                 |
+==================================+===========+=====================+===========================+=============================+
| :code:`first_open_paren`         | |values|  | opening parenthesis | |default_remove_new_line| | * |add_new_line|            |
+----------------------------------+-----------+---------------------+---------------------------+ * |remove_new_line|         |
| :code:`last_close_paren`         | |values|  | closing parenthesis | |default_add_new_line|    | * |ignore|                  |
+----------------------------------+-----------+---------------------+---------------------------+                             |
| :code:`interface_element`        | |values|  | interface element   | |default_add_new_line|    |                             |
+----------------------------------+-----------+---------------------+---------------------------+                             |
| :code:`interface_list_semicolon` | |values2| | semicolon           | |default_remove_new_line| |                             |
+----------------------------------+-----------+---------------------+---------------------------+-----------------------------+
| :code:`ignore_single_line`       | |values3| | N/A                 | |no|                      | * |ignore_single_line__yes| |
|                                  |           |                     |                           | * |ignore_single_line__no|  |
+----------------------------------+-----------+---------------------+---------------------------+-----------------------------+

.. code-block:: vhdl

   procedure update_test (
       test_number : integer;
       test_result : boolean
   );


The following configuration replicates the above code snippet.

.. code-block:: yaml

   rule :
     procedure_013:
        first_open_paren : 'remove_new_line'
        last_close_paren : 'add_new_line'
        interface_element_semicolon : 'remove_new_line'
        interface_element: 'add_new_line'
        ignore_single_line : 'no'

.. NOTE:: All examples use the above configuration.

Example: :code:`first_open_paren` set to :code:`add_new_line`
#############################################################

Setting the :code:`first_open_paren` option to :code:`add_new_line` will result in the following formatting:

.. code-block:: vhdl

    procedure update_test
    (
      test_number : integer;
      test_result : boolean
    );

Example: :code:`last_close_paren` set to :code:`remove_new_line`
################################################################

Setting the :code:`last_close_paren` option to :code:`remove_new_line` will result in the following formatting:

.. code-block:: vhdl

    procedure update_test (
      test_number : integer;
      test_result : boolean);

Example: :code:`interface_element` set to :code:`remove_new_line`
###################################################################

Setting the :code:`interface_element` option to :code:`remove_new_line` will result in the following formatting:

.. code-block:: vhdl

    procedure update_test (test_number : integer;test_result : boolean
    );

Rules Enforcing Subprogram Specification Structure
##################################################

* `function_019 <function_rules.html#function-019>`_
* `procedure_013 <procedure_rules.html#procedure-013>`_
