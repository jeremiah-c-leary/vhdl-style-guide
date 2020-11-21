Configuring Blank Lines
-----------------------

There are rules which will check for blank lines above or below a line.
These rules are designed to improve readability by separating code using blank lines.

However, there is always a question of comments.

The blank line rules allow for comments by configuring the option :code:`allow_comments`.

.. code-block:: yaml

   ---

   rule :
     library_003:
        allow_comments : True

iF :code:`allow_comments` is set to true, then comments are allowed on the preceding line:

.. code-Block:: vhdl

    -- Bring in libraries
    library ieee;

If :code:`allow_comments` is set to false, then comments are not allowed on the preceding line:

.. code-Block:: vhdl

    -- Bring in libraries

    library ieee;
