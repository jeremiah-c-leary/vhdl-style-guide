.. _configuring-comment-indenting:

Configuring Comment Indenting
-----------------------------

The desired indenting of comments can vary depending on where the comment occurs.

There is current a single option for configuring indents.

.. |boolean_value| replace::
   :code:`<boolean>`

.. |True| replace::
   :code:`True`

.. |False| replace::
   :code:`False`

.. |align_with_end_of_declarative_part| replace::
   :code:`align_with_end_of_declarative_part`

.. |align_with_end_of_statement_part| replace::
   :code:`align_with_end_of_statement_part`

.. |align_with_end_of_part_default| replace::
   |False|

.. |align_with_end_of_part_True| replace::
   |True| = Sets indent to current indent level.

.. |align_with_end_of_part_False| replace::
   |False| = Sets indent to next indent level.

+--------------------------------------+-----------------+---------------+----------------------------------+
| Option                               |   Values        |  Default      | Description                      |
+======================================+=================+===============+==================================+
| |align_with_end_of_declarative_part| | |boolean_value| | :code:`False` | * |align_with_end_of_part_True|  |
|                                      |                 |               | * |align_with_end_of_part_False| |
+--------------------------------------+-----------------+---------------+----------------------------------+
| |align_with_end_of_statement_part|   | |boolean_value| | :code:`False` | * |align_with_end_of_part_True|  |
|                                      |                 |               | * |align_with_end_of_part_False| |
+--------------------------------------+-----------------+---------------+----------------------------------+

This is an example of how to configure these options.

.. code-block:: yaml

   indent:
     options:
       comment:
         align_with_end_of_declarative_part: False
         align_with_end_of_statement_part: False

The following code snippet is used for all examples.

.. code-block:: vhdl

    architecture rtl of fifo is

      signal a : std_logic;
          -- end of signal declarations

    begin

      o_output <= a;
          -- end of output assignments

    end architecture rtl;

Example: |align_with_end_of_declarative_part| set to |True|
###########################################################

The |align_with_end_of_declarative_part| option controls the indent of comments at the end of a declarative part.
Setting this option to |True| will set the indent of the comment to the previous indent level.

.. code-block:: vhdl

    architecture rtl of fifo is

      signal a : std_logic;
      -- end of signal declarations

    begin

      o_output <= a;
          -- end of output assignments

    end architecture rtl;

Example: |align_with_end_of_declarative_part| set to |False|
############################################################

The |align_with_end_of_declarative_part| option controls the indent of comments at the end of a declarative part.
Setting this option to |False| will set the indent of the comment to the next indent level.

.. code-block:: vhdl

    architecture rtl of fifo is

      signal a : std_logic;
    -- end of signal declarations

    begin

      o_output <= a;
          -- end of output assignments

    end architecture rtl;

Example: |align_with_end_of_statement_part| set to |True|
#########################################################

The |align_with_end_of_statement_part| option controls the indent of comments at the end of a statement part.
Setting this option to |True| will set the indent of the comment to the previous indent level.

.. code-block:: vhdl

    architecture rtl of fifo is

      signal a : std_logic;
          -- end of signal declarations

    begin

      o_output <= a;
      -- end of output assignments

    end architecture rtl;

Example: |align_with_end_of_statement_part| set to |False|
##########################################################

The |align_with_end_of_statement_part| option controls the indent of comments at the end of a statement part.
Setting this option to |False| will set the indent of the comment to the next indent level.

.. code-block:: vhdl

    architecture rtl of fifo is

      signal a : std_logic;
          -- end of signal declarations

    begin

      o_output <= a;
    -- end of output assignments

    end architecture rtl;

Rules Enforcing Comment Indenting
#################################

* `comment_010 <comment_rules.html#comment-010>`_
