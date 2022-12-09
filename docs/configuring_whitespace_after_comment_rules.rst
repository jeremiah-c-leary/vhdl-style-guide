.. _configuring-whitespace-after-comment-rules:

Configuring Whitespace After Comment Rules
------------------------------------------

There is a rule which will check for a whitespace after :code:`--` in a single line comment.
This behavior can be modified by using the :code:`exceptions` and :code:`patterns` options.

.. |exceptions_defaults| replace::
   :code:`--!`, :code:`--|`, :code:`--=`, :code:`--+`, :code:`---`

.. |exceptions_description| replace::
   A list of patterns to not insert whitespace after comment characters :code:`--`.

.. |patterns_defaults| replace::
   :code:`--!`, :code:`--|`

.. |patterns_description| replace::
   A list of patterns to insert whitespace after comment characters :code:`--`.

+--------------------------+-----------------------+--------------------------+
| Option                   | Default               |  Description             |
+==========================+=======================+==========================+
| exceptions               | |exceptions_defaults| | |exceptions_description| |
+--------------------------+-----------------------+--------------------------+
| patterns                 | |patterns_defaults|   | |patterns_description|   | 
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

.. NOTE::
   Each exception and pattern must start with :code:`--` and not more than three characters long.

   Each pattern must start with :code:`--` and there are no restrictions on length.

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
