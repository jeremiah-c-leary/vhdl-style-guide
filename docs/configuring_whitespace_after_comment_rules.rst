.. _configuring-whitespace-after-comment-rules:

Configuring Whitespace After Comment Rules
------------------------------------------

There are rules which will check for a whitespace after "--" in a single line comment.
The default behavior will add a whitespace after every "--".
This behavior can be disabled by using the **exceptions** option.

+--------------------------+----------------------------------------------------------+
| Option                   | Description                                              |
+==========================+==========================================================+
| exceptions               | Determines the number of whitespace characters to allow. |
+--------------------------+----------------------------------------------------------+

The default value of exceptions is: "--!", "--=", "--+", "--|", and '---'.

The exceptions can be changed using a configuration:

.. code-block:: yaml

   rule :
     comment_100 :
       exceptions :
         - '--!'
         - '--*'

Each exception must start with '--' and be no more than three characters long.

Rules Enforcing Whitespace After Comment
########################################

* `comment_100 <comment_rules.html#comment-100>`_
