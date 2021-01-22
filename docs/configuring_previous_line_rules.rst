Configuring Previous Line Rules
-------------------------------

There are rules which will check the contents on lines above code structures.
These rules allow enforcement of comments and blank lines.

There are several options to these rules, which can be selected by using the :code:`method` option:

+---------------------+----------------------------------------------------------+
| Method              | Description                                              |
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

This is an example of how to configure these options.

.. code-block:: yaml

   rule :
     entity_003:
        method : require_blank_line

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
