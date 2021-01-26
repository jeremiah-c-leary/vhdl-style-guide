Configuring Previous Line Rules
-------------------------------

There are rules which will check the contents on lines above code structures.
These rules allow enforcement of comments and blank lines.

There are several options to these rules, which can be selected by using the :code:`style` option:

+---------------------+----------------------------------------------------------+
| Style               | Description                                              |
+=====================+==========================================================+
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

Example: require_blank_line
###########################

The following code would fail with this option:

.. code-Block:: vhdl

    library fifo_dsn;
    -- Bring in libraries
    entity fifo is

The following code would pass with this option:

.. code-block:: vhdl

    library fifo_dsn;
    -- Bring in libraries

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

* `architecture_003 <architecture_rules.html#architecture_003>`_
* `architecture_016 <architecture_rules.html#architecture_016>`_
* `architecture_018 <architecture_rules.html#architecture_018>`_
* `block_200 <block_rules.html#block_200>`_
* `block_202 <block_rules.html#block_202>`_
* `block_204 <block_rules.html#block_204>`_
* `case_007 <case_rules.html#case_007>`_
* `case_009 <case_rules.html#case_009>`_
* `component_003 <component_rules.html#component_003>`_
* `context_003 <context_rules.html#context_003>`_
* `context_024 <context_rules.html#context_024>`_
* `entity_003 <entity_rules.html#entity_003>`_
* `function_006 <function_rules.html#function_006>`_
* `generate_004 <generate_rules.html#generate_004>`_
* `if_031 <if_rules.html#if_031>`_
* `instantiation_004 <instantiation_rules.html#instantiation_004>`_
* `library_003 <library_rules.html#library_003>`_
* `package_003 <package_rules.html#package_003>`_
* `package_012 <package_rules.html#package_012>`_
* `package_body_200 <package_body_rules.html#package_body_200>`_
* `package_body_202 <package_body_rules.html#package_body_202>`_
* `process_015 <process_rules.html#process_015>`_
* `process_023 <process_rules.html#process_023>`_
* `type_010 <type_rules.html#type_010>`_
