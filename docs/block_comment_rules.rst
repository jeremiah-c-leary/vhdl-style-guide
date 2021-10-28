.. include:: icons.rst

Block Comment Rules
-------------------

.. NOTE::  All examples in this section are using the following options:

    * header_left = '+'
    * header_left_repeat = '-'
    * header_string = '[ Header ]'
    * header_right_repeat = '='
    * comment_left = '|'
    * footer_left = '+'
    * footer_left_repeat = '-'
    * footer_string = '[ Footer ]'
    * footer_right_repeat = '='
    * min_height = 3
    * header_alignment = 'center'
    * max_header_column = 40
    * footer_alignment = 'right'
    * max_footer_column = 40

block_comment_001
#################

|phase_1| |disabled| |error|

This rule checks the block comment header is correct.

Refer to the section `Configuring Block Comments <configuring.html#configuring-block-comments>`_ for additional information.

**Violation**

.. code-block:: vhdl

   ----------------------------------------
   --   Comment
   --   Comment
   ----------------------------------------

**Fix**

.. code-block:: vhdl

   --+-------------[ Header ]==============
   --   Comment
   --   Comment
   ----------------------------------------

block_comment_002
#################

|phase_1| |disabled| |error|

This rule checks the **comment_left** attribute exists for all comments.

Refer to the section `Configuring Block Comments <configuring.html#configuring-block-comments>`_ for additional information.

**Violation**

.. code-block:: vhdl

   --+-------------[ Header ]==============
   --   Comment
   --   Comment
   ----------------------------------------

**Fix**

.. code-block:: vhdl

   --+-------------[ Header ]==============
   --|  Comment
   --|  Comment
   ----------------------------------------

block_comment_003
#################

|phase_1| |disabled| |error|

This rule checks the block comment footer is correct.

Refer to the section `Configuring Block Comments <configuring.html#configuring-block-comments>`_ for additional information.

**Violation**

.. code-block:: vhdl

   --+-------------[ Header ]==============
   --|  Comment
   --|  Comment
   ----------------------------------------

**Fix**

.. code-block:: vhdl

   --+-------------[ Header ]==============
   --|  Comment
   --|  Comment
   --+--------------------------[ Footer ]=

