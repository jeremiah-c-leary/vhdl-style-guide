
.. _configuring-block-comments:

Configuring Block Comments
--------------------------

Block comments are sequential comment lines with a header and footer.
Below are several examples of a block comments:

.. code-block:: vhdl

    ----------------------------------
    -- Comment
    -- Comment
    ----------------------------------

    --================================
    -- Comment
    -- Comment
    --================================

    --+-------------------------------
    --| Comment
    --| Comment
    --+-------------------------------

    --+---------< header >------------
    --| Comment
    --| Comment
    --+---------< footer >------------

Block Comment Structure
#######################

The above examples can be generalized into the following:

.. code-block:: text

   --<header_left><header_left_repeat><header_string><header_right_repeat>
   --<comment_left>
   --<footer_left><footer_left_repeat><footer_string><footer_right_repeat>

Where:

+---------------------+---------+---------+-------------------------------------------------------------+
| Attribute           | Values  | Default | Description                                                 |
+=====================+=========+=========+=============================================================+
| header_left         | String  | None    | The string to place to the right of the --                  |
|                     | None    |         |                                                             |
+---------------------+---------+---------+-------------------------------------------------------------+
| header_left_repeat  | String  |   \-    | A character to repeat between header_left and header_string |
+---------------------+---------+---------+-------------------------------------------------------------+
| header_string       | String  | None    | A string to place in the header.                            |
|                     | None    |         |                                                             |
+---------------------+---------+---------+-------------------------------------------------------------+
| header_right_repeat | String  | None    | A character to repeat after the header-string               |
|                     | None    |         |                                                             |
+---------------------+---------+---------+-------------------------------------------------------------+
| comment_left        | String  | None    | A string which should exist to the right of the --          |
|                     | None    |         |                                                             |
+---------------------+---------+---------+-------------------------------------------------------------+
| footer_left         | String  | None    | The string to place to the right of the --                  |
|                     | None    |         |                                                             |
+---------------------+---------+---------+-------------------------------------------------------------+
| footer_left_repeat  | String  |   \-    | A character to repeat between footer_left and footer_string |
+---------------------+---------+---------+-------------------------------------------------------------+
| footer_string       | String  | None    | A string to place in the footer.                            |
|                     | None    |         |                                                             |
+---------------------+---------+---------+-------------------------------------------------------------+
| footer_right_repeat | String  | None    | A character to repeat after the footer_string               |
|                     | None    |         |                                                             |
+---------------------+---------+---------+-------------------------------------------------------------+

There are additional options for configuring block comments:

+---------------------+----------+----------+------------------------------------------------------------------+
| Attribute           | Values   | Default  | Description                                                      |
+=====================+==========+==========+==================================================================+
| min_height          | Integer  |    3     | Sets minimum number of consecutive comment lines before          |
|                     |          |          | being considered a block comment.                                |
+---------------------+----------+----------+------------------------------------------------------------------+
| header_alignment    | "left"   |          | Sets horizontal position of header string.                       |
|                     | "center" | "center" |                                                                  |
|                     | "right"  |          |                                                                  |
+---------------------+----------+----------+------------------------------------------------------------------+
| max_header_column   | Integer  |   120    | Sets the maximum length of the combined header.                  |
+---------------------+----------+----------+------------------------------------------------------------------+
| footer_alignment    | "left"   |          | Sets horizontal position of footer string.                       |
|                     | "center" | "center" |                                                                  |
|                     | "right"  |          |                                                                  |
+---------------------+----------+----------+------------------------------------------------------------------+
| max_footer_column   | Integer  |   120    | Sets the maximum length of the combined footer.                  |
+---------------------+----------+----------+------------------------------------------------------------------+
| allow_indenting     | "yes"    |  "yes"   | Allows indented block comments. Setting this to :code:`no` will  |
|                     | "no"     |          | only detect block comments starting at column 0.                 |
+---------------------+----------+----------+------------------------------------------------------------------+

With these options, a block comment can be validated by VSG.

Examples
########

It is important to note the rules are disabled by default.
They must enabled using a configuration.

Simple Block Comment
^^^^^^^^^^^^^^^^^^^^

To configure the following example...

.. code-block:: vhdl

    ----------------------------------
    -- Comment
    -- Comment
    ----------------------------------

...the configuration would be:

.. code-block:: yaml

   rule:
     block_comment_001:
       allow_indenting: true
       disable: false
       header_left:
       header_left_repeat: '-'
       header_string:
       header_right_repeat:
     block_comment_002:
       allow_indenting: true
       disable: false
       comment_left:
     block_comment_003:
       allow_indenting: true
       disable: false
       footer_left:
       footer_left_repeat: '-'
       footer_string:
       footer_right_repeat:

Complex Block Comment
^^^^^^^^^^^^^^^^^^^^^

To configure the following example...

.. code-block:: vhdl

    --+-<Header>==============================
    --| Purpose:
    --| Author:
    --+------------------------------<Footer>=

...the configuration would be:

.. code-block:: yaml

   rule:
     block_comment_001:
       disable : False
       header_left : '+'
       header_left_repeat : '-'
       header_string : '<Header>'
       header_right_repeat : '='
       header_alignment : 'left'
     block_comment_002:
       disable : False
       comment_left : '|'
     block_comment_003:
       disable : False
       footer_left : '+'
       footer_left_repeat : '-'
       footer_string : '<Footer>'
       footer_right_repeat : '='
       footer_alignment : 'right'


Doxygen Block Comment
^^^^^^^^^^^^^^^^^^^^^

Doxygen comments use an exclamation mark.
To configure a block comment for Doxygen...

.. code-block:: vhdl

    ----------------------------------
    --! Comment
    --! Comment
    ----------------------------------

...the configuration would be:

.. code-block:: yaml

   rule:
     block_comment_001:
       disable : False
       header_left : '-'
       header_left_repeat : '-'
       header_string : ''
       header_right_repeat : ''
     block_comment_002:
       disable : False
       comment_left : '!'
     block_comment_003:
       disable : False
       footer_left : '-'
       footer_left_repeat : '-'
       footer_string : ''
       footer_right_repeat : ''

Rules Enforcing Block Comments
##############################

* `block_comment_001 <block_comment_rules.html#block-comment-001>`_
* `block_comment_002 <block_comment_rules.html#block-comment-002>`_
* `block_comment_003 <block_comment_rules.html#block-comment-003>`_
