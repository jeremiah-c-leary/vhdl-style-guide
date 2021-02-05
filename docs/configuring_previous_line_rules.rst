Configuring Previous Line Rules
-------------------------------

There are rules which will check the contents on lines above code structures.
These rules allow enforcement of comments and blank lines.

There are several options to these rules, which can be selected by using the :code:`style` option:

+---------------------+----------------------------------------------------------+
| Style               | Description                                              |
+=====================+==========================================================+
| no_blank_line       | Removes blank lines on the line above.                   |
+---------------------+----------------------------------------------------------+
| require_blank_line  | Requires a blank line on the line above.                 |
+---------------------+----------------------------------------------------------+
| no_code             | Either a blank line; or comment(s) on the line(s) above. |
+---------------------+----------------------------------------------------------+
| allow_comment       | Either a blank line; or comment(s) on the line(s) above  |
|                     | and a blank line above the comment(s).                   |
+---------------------+----------------------------------------------------------+
| require_comment     | Comment(s) required on the line(s) above and a           |
|                     | blank line above the comment(s).                         |
+---------------------+----------------------------------------------------------+

.. NOTE:: Unless stated in rule description, the default style is :code:`require_blank_line`.

This is an example of how to configure these options.

.. code-block:: yaml

   rule :
     entity_003:
        style : require_blank_line

.. NOTE:: All examples below are using the rule **entity_004**.

Example: no_blank
#################

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

Example: require_blank_line
###########################

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

Example: no_code
################

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

Example: allow_comment
######################

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

Example: require_comment
########################

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

Rules Enforcing Previous Lines
##############################

* `architecture_003 <architecture_rules.html#architecture-003>`_
* `block_200 <block_rules.html#block-200>`_
* `case_007 <case_rules.html#case-007>`_
* `component_003 <component_rules.html#component-003>`_
* `context_003 <context_rules.html#context-003>`_
* `entity_003 <entity_rules.html#entity-003>`_
* `function_006 <function_rules.html#function-006>`_
* `generate_004 <generate_rules.html#generate-004>`_
* `if_031 <if_rules.html#if-031>`_
* `instantiation_004 <instantiation_rules.html#instantiation-004>`_
* `library_003 <library_rules.html#library-003>`_
* `package_003 <package_rules.html#package-003>`_
* `package_body_200 <package_body_rules.html#package-body-200>`_
* `process_015 <process_rules.html#process-015>`_
* `type_010 <type_rules.html#type-010>`_
