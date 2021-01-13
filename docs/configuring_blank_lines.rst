Configuring Blank Lines
-----------------------

There are rules which will check for blank lines above or below a line.
These rules are designed to improve readability by separating code using blank lines.

However, there is always a question of comments.

The blank line rules allow for comments by configuring two options

+---------------------+---------+--------------------------------------------------+
| Option              | Values  | Description                                      |
+=====================+=========+==================================================+
| allow_comment       | Boolean | Allows comments in the line above.               |
+---------------------+---------+--------------------------------------------------+
| blank_above_comment | Boolean | Enforces a blank line above comments.            |
|                     |         | Only valid when allow_comment is True            |
+---------------------+---------+--------------------------------------------------+

This is an example of how to configure the options.

.. code-block:: yaml

   rule :
     library_003:
        allow_comments : True
        blank_above_comment : False

If :code:`allow_comments` is set to true, and :code:`blank_above_comment` is set to false then the following is valid:

.. code-Block:: vhdl

    library fifo_dsn
    -- Bring in libraries
    library ieee;

If :code:`allow_comments` is set to true, and :code:`blank_above_comment` is set to true then the following is valid:

.. code-Block:: vhdl

    library fifo_dsn

    -- Bring in libraries
    library ieee;

If :code:`allow_comments` is set to false, then comments are not allowed on the preceding line:

.. code-Block:: vhdl

    -- Bring in libraries

    library ieee;
