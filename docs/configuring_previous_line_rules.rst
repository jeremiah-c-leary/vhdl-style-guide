
.. _configuring-previous-line-rules:

Configuring Previous Line Rules
-------------------------------

There are rules which will check the contents on lines above code structures.
These rules allow enforcement of comments and blank lines.

There are several options to these rules, which can be selected by using the :code:`style` option:

.. |style| replace::
   :code:`style`

.. |no_blank_line| replace::
   :code:`no_blank_line`

.. |require_blank_line| replace::
   :code:`require_blank_line`

.. |no_code| replace::
   :code:`no_code`

.. |allow_comment| replace::
   :code:`allow_comment`

.. |require_comment| replace::
   :code:`require_comment`

.. |no_blank_line_unless_different_library| replace::
   :code:`no_blank_line_unless_different_library`

.. |style_values| replace::
   |no_blank_line|, |require_blank_line|, |no_code|, |allow_comment|, |require_comment|, |require_blank_line|

.. |style__no_blank_line| replace::
   |no_blank_line| = Removes blank lines on the line above.

.. |style__require_blank_line| replace::
   |require_blank_line| = Requires a blank line on the line above.

.. |style__no_code| replace::
   |no_code| = Either a blank line; or comment(s) on the line(s) above.

.. |style__allow_comment| replace::
   |allow_comment| = Either a blank line; or comment(s) on the line(s) above and a blank line above the comment(s).

.. |style__require_comment| replace::
   |require_comment| = Comment(s) required on the line(s) above and a blank line above the comment(s).

.. |style__no_blank_line_unless_different_library| replace::
   |no_blank_line_unless_different_library| = Removes blank lines on lines above unless the library is different.

.. |default_value| replace::
   |require_blank_line|

+----------------------+----------------+-------------------+---------------------------------------------------+
| Option               | Values         | Default Value     | Description                                       |
+======================+================+===================+===================================================+
| |style|              | |style_values| | |default_value|   | * |style__no_blank_line|                          |
|                      |                |                   | * |style__require_blank_line|                     |
|                      |                |                   | * |style__no_code|                                |
|                      |                |                   | * |style__allow_comment|                          |
|                      |                |                   | * |style__require_comment|                        |
|                      |                |                   | * |style__no_blank_line_unless_different_library| |
+----------------------+----------------+-------------------+---------------------------------------------------+

.. NOTE:: Unless stated in the rule description, the default style is :code:`require_blank_line`.

.. WARNING:: It is important to be aware these rules may conflict with rules that enforce blank lines below keywords.
  This can occur when a below rule is applied and then on the next line a previous rule applies.
  Resolve any conflicts by changing the configuration of either rule.

This is an example of how to configure these options.

.. code-block:: yaml

   rule :
     entity_003:
        style : require_blank_line

.. NOTE:: All examples below are using the rule **entity_004**.

Example: |style| set to |no_blank_line|
#######################################

The following code would fail with this option:

.. code-Block:: vhdl

    library fifo_dsn;
    -- Define entity

    entity fifo is

The following code would pass with this option:

.. code-block:: vhdl

    library fifo_dsn;
    -- Define entity
    entity fifo is

Example: |style| set to |require_blank_line|
############################################

The following code would fail with this option:

.. code-Block:: vhdl

    library fifo_dsn;
    -- Define entity
    entity fifo is

The following code would pass with this option:

.. code-block:: vhdl

    library fifo_dsn;
    -- Define entity

    entity fifo is

Example: |style| set to |no_code|
#################################

The following code would fail with this option:

.. code-block:: vhdl

   library fifo_dsn;
   entity fifo is

The following code would pass with this option:

.. code-block:: vhdl

   library fifo_dsn;

   entity fifo is

   library fifo_dsn;
   -- Comment

   entity fifo is

   library fifo_dsn;
   -- Comment
   entity fifo is

Example: |style| set to |allow_comment|
#######################################

The following code would fail with this option:

.. code-block:: vhdl

   library fifo_dsn;
   entity fifo is

   library fifo_dsn;
   -- Comment
   entity fifo is

The following code would pass with this option:

.. code-block:: vhdl

   library fifo_dsn;

   entity fifo is

   library fifo_dsn;
   -- Comment

   entity fifo is

   library fifo_dsn;

   -- Comment
   entity fifo is

Example: |style| set to |require_comment|
#########################################

The following code would fail these options:

.. code-block:: vhdl

   library fifo_dsn;
   entity fifo is

   library fifo_dsn;
   -- Comment
   entity fifo is

The following code would pass these options:

.. code-block:: vhdl

   library fifo_dsn;

   -- Comment
   entity fifo is

Example: |style| set to |no_blank_line_unless_different_library|
################################################################

This option provides grouping of use clauses based on library.

The following code:

.. code-block:: vhdl

   library ieee;

   use ieee.std_logic_1164.all;

   use ieee.numeric_std.all;

   use work.axi4_stream_pkg.all;

   use work.axi4_lite_pkg.all;

will be fixed to:

.. code-block:: vhdl

   library ieee;
   use ieee.std_logic_1164.all;
   use ieee.numeric_std.all;

   use work.axi4_stream_pkg.all;
   use work.axi4_lite_pkg.all;


Rules Enforcing Previous Lines
##############################

* `architecture_003 <architecture_rules.html#architecture-003>`_
* `block_200 <block_rules.html#block-200>`_
* `case_007 <case_rules.html#case-007>`_
* `case_201 <case_rules.html#case-201>`_
* `case_generate_alternative_201 <case_generate_alternative_rules.html#case-generate-alternative-201>`_
* `component_003 <component_rules.html#component-003>`_
* `context_003 <context_rules.html#context-003>`_
* `entity_003 <entity_rules.html#entity-003>`_
* `function_006 <function_rules.html#function-006>`_
* `generate_004 <generate_rules.html#generate-004>`_
* `if_031 <if_rules.html#if-031>`_
* `instantiation_004 <instantiation_rules.html#instantiation-004>`_
* `library_003 <library_rules.html#library-003>`_
* `library_007 <library_rules.html#library-007>`_
* `loop_statement_200 <loop_statement_rules.html#loop-statement-200>`_
* `loop_statement_202 <loop_statement_rules.html#loop-statement-202>`_
* `package_003 <package_rules.html#package-003>`_
* `package_body_200 <package_body_rules.html#package-body-200>`_
* `package_instantiation_200 <package_instantiation_rules.html#package-instantiation-200>`_
* `pragma_400 <pragma_rules.html#pragma-400>`_
* `pragma_402 <pragma_rules.html#pragma-402>`_
* `procedure_200 <procedure_rules.html#procedure-200>`_
* `process_015 <process_rules.html#process-015>`_
* `record_type_definition_201 <record_type_definition_rules.html#record-type-definition-201>`_
* `subtype_201 <subtype_rules.html#subtype-201>`_
* `type_010 <type_rules.html#type-010>`_
