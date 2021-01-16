Configuring Previous Line Rules
-------------------------------

There are rules which will check the contents on lines above code structures.
These rules allow enforcement of comments and blank lines.

There are several options to these rules, but they fall into two categories:  allow and require.
Require options will check the feature exists above the line in question.
Allow options provide exceptions to the require options.

+---------------------+---------+---------+--------------------------------------------------+
| Option              | Values  | Default | Description                                      |
+=====================+=========+=========+==================================================+
| require_blank_line  | Boolean |  True   | Requires a blank line on the line above.         |
+---------------------+---------+---------+--------------------------------------------------+
| allow_comment       | Boolean |  False  | Allows comments in the line above.               |
+---------------------+---------+---------+--------------------------------------------------+
| require_comment     | Boolean |  False  | Requires a comment on the line above.            |
+---------------------+---------+---------+--------------------------------------------------+
| blank_above_comment | Boolean |  False  | Enforces a blank line above comments.            |
|                     |         |         | Only valid when allow_comment is True            |
+---------------------+---------+---------+--------------------------------------------------+

.. NOTE:: require_blank_line and require_comment are mutually exclusive

This is an example of how to configure these options.

.. code-block:: yaml

   rule :
     entity_003:
        require_blank_line : True
        allow_comment : False
        require_comment : False
        blank_above_comment : False

.. NOTE:: All examples below are using the rule **entity_004**.

Example: require_blank_line
###########################

Using :code:`require_blank_line` enforces a blank line above the entity keyword.

The following code would fail because of the comment.

.. code-Block:: vhdl

    library fifo_dsn;
    -- Bring in libraries
    entity fifo is

The fix for this is to add a blank line after the comment:

.. code-block:: vhdl

    library fifo_dsn;
    -- Bring in libraries

    entity fifo is

Example: require_blank_line and allow_comment
#############################################

Using :code:`allow_comment` with :code:`require_blank_line` allows for an exception to :code:`require_blank_line`.
This combination will enforce a blank line above the entity keyword unless there is a comment.

The following code would pass these combinations:

.. code-block:: vhdl

   library fifo_dsn;

   entity fifo is

   library fifo_dsn;
   -- Comment

   entity fifo is

   library fifo_dsn;
   -- Comment
   entity fifo is

The following code would fail these options:

.. code-block:: vhdl

   library fifo_dsn;
   entity fifo is

Example: require_blank_line and allow_comment and blank_above_comment
#####################################################################

Using :code:`blank_above_comment` with both :code:`allow_comment` and :code:`require_blank_line` allows for an exception to :code:`require_blank_line` and enforces a blank line above comments.
This combination will enforce a blank line above the entity keyword unless there is a comment.
If there is a comment, then a blank line must exist above it.

The following code would pass these options:

.. code-block:: vhdl

   library fifo_dsn;

   entity fifo is

   library fifo_dsn;
   -- Comment

   entity fifo is

   library fifo_dsn;

   -- Comment
   entity fifo is

The following code would fail these options:

.. code-block:: vhdl

   library fifo_dsn;
   entity fifo is

   library fifo_dsn;
   -- Comment
   entity fifo is

Example: require_comment
########################

Using :code:`require_comment` will require a comment to start the line above the entity keyword.

The following code would pass this option:

.. code-block:: vhdl

   library fifo_dsn;

   -- Comment
   entity fifo is

   library fifo_dsn;
   -- Comment
   entity fifo is

The following code would fail this option:

.. code-block:: vhdl

   library fifo_dsn;

   entity fifo is

   library fifo_dsn;
   -- Comment

   entity fifo is

Example: require_comment and blank_above_comment
################################################

Using :code:`blank_above_comment` with :code:`require_comment` enforces a blank line above the required comment.

The following code would pass these options:

.. code-block:: vhdl

   library fifo_dsn;

   -- Comment
   entity fifo is

The following code would fail these options:

.. code-block:: vhdl

   library fifo_dsn;
   entity fifo is

   library fifo_dsn;
   -- Comment
   entity fifo is
