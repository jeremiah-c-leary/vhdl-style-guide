.. _configuring-whitespace-after-comment-rules:

Configuring Whitespace After Comment Rules
------------------------------------------

There is a rule which will check for a whitespace after :code:`--` in a single line comment.
This behavior can be modified by using the :code:`exceptions` and :code:`patterns` options.

.. |exceptions_option| replace::
   :code:`exceptions`

.. |patterns_option| replace::
   :code:`patterns`

.. |exceptions_defaults| replace::
   :code:`--!`, :code:`--|`, :code:`--=`, :code:`--+`, :code:`---`

.. |exceptions_description| replace::
   A list of patterns to not insert whitespace after comment characters :code:`--`.
   Each exception must start with :code:`--` and not more than three characters long.
   Exceptions not starting with :code:`--` will be ignored.

.. |patterns_defaults| replace::
   :code:`--!`, :code:`--|`

.. |patterns_description| replace::
   A list of patterns to insert whitespace after comment characters :code:`--`.
   Each pattern must start with :code:`--` and there is no restriction on length.
   Patterns not starting with :code:`--` will be ignored.

+--------------------------+-----------------------+--------------------------+
| Option                   | Default               |  Description             |
+==========================+=======================+==========================+
| |exceptions_option|      | |exceptions_defaults| | |exceptions_description| |
+--------------------------+-----------------------+--------------------------+
| |patterns_option|        | |patterns_defaults|   | |patterns_description|   |
+--------------------------+-----------------------+--------------------------+

This is an example of how to configure these options.

.. code-block:: yaml

   rule :
     comment_100 :
       exceptions :
         - '--!'
         - '--*'
       patterns :
         - '--!'
         - '--*'

Example
#######

Using the default values, the following comments

.. code-block:: vhdl

   --% Comment 1
   --!Comment 2
   -----------

... would be correct to

.. code-block:: vhdl

   -- % Comment 1
   --! Comment 2
   -----------

Rules Enforcing Whitespace After Comment
########################################

* `comment_100 <comment_rules.html#comment-100>`_
