Block Comment Rules
-------------------

.. NOTE::  All examples in this section are using the following options:

    * header_left = '+'
    * header_left_repeat = '-'
    * header_string = '[ Description ]'
    * header_right_repeat = '='
    * comment_left = '|'
    * footer_left = '+'
    * footer_left_repeat = '-'
    * footer_string = '[ Description ]'
    * footer_right_repeat = '='
    * min_height = 3
    * header_alignment = 'center'
    * max_header_column = 40
    * footer_alignment = 'right'
    * max_footer_column = 40

Structural Rules (000 - 099)
############################

block_comment_001
^^^^^^^^^^^^^^^^^

This rule checks the block comment header is correct.

Refer to the section `Configuring Block Comments <configuring_block_comments.html>`_ for additional information.

**Violation**

.. code-block:: vhdl

   ----------------------------------------
   --   Comment
   --   Comment
   ----------------------------------------

**Fix**

.. code-block:: vhdl

   --+-----------[ Description ]===========
   --   Comment
   --   Comment
   ----------------------------------------

block_comment_002
^^^^^^^^^^^^^^^^^

This rule checks the **comment_left** attribute exists for all comments.

Refer to the section `Configuring Block Comments <configuring_block_comments.html>`_ for additional information.

**Violation**

.. code-block:: vhdl

   --+-----------[ Description ]===========
   --   Comment
   --   Comment
   ----------------------------------------

**Fix**

.. code-block:: vhdl

   --+-----------[ Description ]===========
   --|  Comment
   --|  Comment
   ----------------------------------------

block_comment_003
^^^^^^^^^^^^^^^^^

This rule checks the block comment footer is correct.

Refer to the section `Configuring Block Comments <configuring_block_comments.html>`_ for additional information.

**Violation**

.. code-block:: vhdl

   --+-----------[ Description ]===========
   --|  Comment
   --|  Comment
   ----------------------------------------

**Fix**

.. code-block:: vhdl

   --+-----------[ Description ]===========
   --|  Comment
   --|  Comment
   --+---------------------[ Description ]=

