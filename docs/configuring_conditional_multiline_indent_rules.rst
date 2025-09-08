.. _configuring-conditional-multiline-indent-rules:

Configuring Conditional Multiline Indent Rules
----------------------------------------------

There are rules which will check alignment of multiline conditional expressions and conditional waveforms.

There are several options to these rules:

.. |align_left| replace::
   :code:`align_left`

.. |align_left__yes| replace::
   :code:`yes` = Lines will be aligned left.

.. |align_left__no| replace::
   :code:`no` = Lines will be aligned to assignment operator.

.. |align_paren| replace::
   :code:`align_paren`

.. |align_paren__yes| replace::
   :code:`yes` = Align to unbalanced open parenthesis.

.. |align_paren__no| replace::
   :code:`no` = Each unbalanced open parenthesis will add an indent.

.. |align_when_keywords| replace::
   :code:`align_when_keywords`

.. |align_when_keywords__yes| replace::
   :code:`yes` = Column align :code:`when` keywords.

.. |align_when_keywords__no| replace::
   :code:`no` = Ignore alignment of :code:`when` keywords.

.. |wrap_at_when| replace::
   :code:`wrap_at_when`

.. |wrap_at_when__yes| replace::
   :code:`yes` = Indent multiline condition at :code:`when` keyword.

.. |wrap_at_when__no| replace::
   :code:`no` = Disable wrapping at :code:`when` keyword.

.. |align_else_keywords| replace::
   :code:`align_else_keywords`

.. |align_else_keywords__yes| replace::
   :code:`yes` = Column align :code:`else` keywords.

.. |align_else_keywords__no| replace::
   :code:`no` = Ignore alignment of :code:`else` keywords.

.. |values| replace::
   :code:`yes`, :code:`no`

.. |default_yes| replace::
   :code:`yes`

.. |default_no| replace::
   :code:`no`

+-----------------------+----------+---------------+------------------------------+
| Option                | Values   | Default       | Description                  |
+=======================+==========+===============+==============================+
| |align_left|          | |values| | |default_no|  | * |align_left__yes|          |
|                       |          |               | * |align_left__no|           |
+-----------------------+----------+---------------+------------------------------+
| |align_paren|         | |values| | |default_yes| | * |align_paren__yes|         |
|                       |          |               | * |align_paren__no|          |
+-----------------------+----------+---------------+------------------------------+
| |align_when_keywords| | |values| | |default_no|  | * |align_when_keywords__yes| |
|                       |          |               | * |align_when_keywords__no|  |
+-----------------------+----------+---------------+------------------------------+
| |wrap_at_when|        | |values| | |default_yes| | * |wrap_at_when__yes|        |
|                       |          |               | * |wrap_at_when__no|         |
+-----------------------+----------+---------------+------------------------------+
| |align_else_keywords| | |values| | |default_no|  | * |align_else_keywords__yes| |
|                       |          |               | * |align_else_keywords__no|  |
+-----------------------+----------+---------------+------------------------------+

The options can be combined to format the conditional expression or conditional waveform.

This is an example of how to configure these options.

.. code-block:: yaml

   rule :
     concurrent_009:
        align_left : 'no'
        align_paren : 'no'
        align_when_keywords : 'no'
        wrap_at_when : 'no'
        align_else_keywords : 'no'

The following code snippet is used for all examples and is formatted with the configuration above

.. code-block:: vhdl

     output <= '1' when input = "0000" or (input = "1111" and
                   input2 = "0101") else
               sig_a or sig_b when input = "0001" and
                 input2 = "1001" else
               sig_c and sig_d when input = "0010" else
              '0';

.. NOTE::  Formatting in the following examples is performed by a separate rule.

Example: |align_left| set to |default_yes|
##########################################

.. code-block:: vhdl

   output <= '1' when input = "0000" or (input = "1111" and
         input2 = "0101") else
     sig_a or sig_b when input = "0001" and
       input = "1001" else
     sig_c and sig_d when input = "0010" else
     '0';

Example: |align_paren| set to |default_yes|
###########################################

.. code-block:: vhdl

   output <= '1' when input = "0000" or (input = "1111" and
                                          input2 = "0101") else
             sig_a or sig_b when input = "0001" and
               input = "1001" else
             sig_c and sig_d when input = "0010" else
             '0';

Example: |align_when_keywords| set to |default_yes|
###################################################

.. code-block:: vhdl

   output <= '1'             when input = "0000" or (input = "1111" and
                 input2 = "0101") else
             sig_a or sig_b  when input = "0001" and
               input = "1001" else
             sig_c and sig_d when input = "0010" else
             '0';

Example: |wrap_at_when| set to |default_yes|
############################################

.. code-block:: vhdl

   output <= '1' when input = "0000" or (input = "1111" and
                        input2 = "0101") else
             sig_a or sig_b when input = "0001" and
                                 input = "1001" else
             sig_c and sig_d when input = "0010" else
             '0';

Example: |align_else_keywords| set to |default_yes|
###################################################

.. code-block:: vhdl

   output <= '1' when input = "0000" or (input = "1111" and
                 input2 = "0101")                else
             sig_a or sig_b when input = "0001" and
               input = "1001"                    else
             sig_c and sig_d when input = "0010" else
             '0';

Example:  Default configuration
###############################

Using the following configuration:

.. code-block:: yaml

   rule :
     concurrent_009:
        align_left : 'no'
        align_paren : 'yes'
        align_when_keywords : 'no'
        wrap_at_when : 'yes'
        align_else_keywords : 'no'

would result in the following formatting:

.. code-block:: vhdl

  output <= '1' when input = "0000" or (input = "1111" and
                                         input2 = "0101") else
            sig_a or sig_b when input = "0001" and
                                input = "1001" else
            sig_c and sig_d when input = "0010" else
            '0';

Example:  Setting all options to |default_yes| except |align_left| set to |default_no|
######################################################################################

Using the following configuration:

.. code-block:: yaml

   rule :
     concurrent_009:
        align_left : 'no'
        align_paren : 'yes'
        align_when_keywords : 'yes'
        wrap_at_when : 'yes'
        align_else_keywords : 'yes'

would result in the following formatting:

.. code-block:: vhdl

   output <= '1'             when input = "0000" or (input = "1111" and
                                                      input2 = "0101") else
             sig_a or sig_b  when input = "0001" and
                                  input = "1001"                       else
             sig_c and sig_d when input = "0010"                       else
             '0';

Rules Enforcing Conditional Expression Alignment
################################################

* `concurrent_009 <concurrent_rules.html#concurrent-009>`_
* `sequential_401 <sequential_rules.html#sequential-401>`_
* `variable_assignment_400 <variable_assignment_400.html#variable-assignment-400>`_
