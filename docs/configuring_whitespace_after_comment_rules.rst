.. _configuring-whitespace-after-comment-rules:

Configuring Whitespace After Comment Rules
------------------------------------------

There are rules which will check for a whitespace after "--" in a single line comment.
This behavior can be disabled by using the **exceptions** option.

+--------------------------+----------------------------------------------------------+
| Option                   | Description                                              |
+==========================+==========================================================+
| exceptions               | A list of patterns to not insert whitespace.             |
+--------------------------+----------------------------------------------------------+
| patterns                 | A list of patterns to insert whitespace after.           |
+--------------------------+----------------------------------------------------------+

The default value of exceptions is: "--!", "--|", "--=", "--+", and '---'.

The default value of patterns is: "--!", "--|".

The options can be changed using a configuration:

.. code-block:: yaml

   rule :
     comment_100 :
       exceptions :
         - '--!'
         - '--*'
       patterns :
         - '--!',
         - '--*'

Each exception must start with '--' and be no more than three characters long.

Each pattern must start with '--' and there are no restrictions on length..

Rules Enforcing Whitespace After Comment
########################################

* `comment_100 <comment_rules.html#comment-100>`_
