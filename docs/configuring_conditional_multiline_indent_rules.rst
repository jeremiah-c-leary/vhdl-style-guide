.. _configuring-conditional-multiline-indent-rules:

Configuring Conditional Multiline Indent Rules
----------------------------------------------

There are rules which will check indent and alignment of multiline conditional expressions and conditional waveforms.

Conditional expressions and conditional waveforms are defined as:

.. code-block:: bash

    conditional_expressions ::=
      expression **when** condition
      { **else** expression **when** condition }
      [ **else** expression ]

    conditional_waveforms ::=
      waveform **when** condition
      { **else** waveform **when** condition }
      [ **else** waveform ]

Below is an example of a conditional waveform:

.. code-block:: vhdl

   architecture rtl of fifo is

   begin

     output <= '1' when input = "00" else
               sig_a or sig_b when input = "01" else
               sig_c and sig_d when input = "10" else
               '0';

   end architecture rtl;

The alignment of multiline rules is handled by a corresponding rule.
Both rules are required to ensure proper formatting of multiline expressions and conditions.
The corresponding rule will be noted in the rule documentation.

There are several options to these rules:

.. |align_left| replace::
   :code:`align_left`

.. |align_paren| replace::
   :code:`align_paren`

.. |align_when_keywords| replace::
   :code:`align_when_keywords`

.. |wrap_at_when| replace::
   :code:`wrap_at_when`

.. |align_else_keywords| replace::
   :code:`align_else_keywords`

.. |values| replace::
   :code:`yes`, :code:`no`

.. |default_yes| replace::
   :code:`yes`

.. |default_no| replace::
   :code:`no`   

+-----------------------+----------+---------------+---------------------------------------------------------+
| Option                | Values   | Default       | Description                                             |
+=======================+==========+===============+=========================================================+
| |align_left|          | |values| | |default_no|  | Align multilines to the left.                           |
+-----------------------+----------+---------------+---------------------------------------------------------+
| |align_paren|         | |values| | |default_yes| | Indent lines based on parenthesis.                      |
+-----------------------+----------+---------------+---------------------------------------------------------+
| |align_when_keywords| | |values| | |default_no|  | Each when keyword will be aligned.                      |
+-----------------------+----------+---------------+---------------------------------------------------------+
| |wrap_at_when|        | |values| | |default_yes| | Indent multiline condition at 'when' keyword.           |
+-----------------------+----------+---------------+---------------------------------------------------------+
| |align_else_keywords| | |values| | |default_no|  | Each else keyword will be aligned.                      |
+-----------------------+----------+---------------+---------------------------------------------------------+

The options can be combined to format the conditional expression or conditional waveform.

This is an example of how to configure these options.

.. code-block:: yaml

   rule :
     concurrent_009:
        wrap_at_when : 'yes'
        align_when_keywords : 'yes'
        align_else_keywords : 'yes'
        align_left : 'no'

.. NOTE:: All examples below are using the rule **concurrent_009**.

Example: |wrap_at_when| set to |default_yes|
############################################

The following code would fail with this option:

.. code-Block:: vhdl

     output <= '1' when input = "0000" or 
         input = "1111" else
       sig_a or sig_b when input = "0001" and 
         input = "1001" else
       sig_c and sig_d when input = "0010" or
         input = "1010" else
       '0';

The following code would pass with this option:

.. code-block:: vhdl

     output <= '1' when input = "0000" or 
                        input = "1111" else
       sig_a or sig_b when input = "0001" and 
                           input = "1001" else
       sig_c and sig_d when input = "0010" or
                            input = "1010" else
       '0';

Example: |align_when_keywords| set to |default_yes|
###################################################

The following code would fail with this option:

.. code-Block:: vhdl

     output <= '1' when input = "00" else
               sig_a or sig_b when input = "01" else
               sig_c and sig_d when input = "10" else
               '0';

The following code would pass with this option:

.. code-block:: vhdl

     output <= '1'             when input = "00" else
               sig_a or sig_b  when input = "01" else
               sig_c and sig_d when input = "10" else
               '0';

Example: |align_when_keywords| and |align_else_keywords| set to |default_yes|
#############################################################################

The following code would fail with this option:

.. code-Block:: vhdl

     output <= '1' when input = "0000" else
               sig_a or sig_b when input = "0100" and input = "1100" else
               sig_c when input = "10" else
               '0';

The following code would pass with this option:

.. code-block:: vhdl

     output <= '1'            when input = "0000"                    else
               sig_a or sig_b when input = "0100" and input = "1100" else
               sig_c          when input = "10"                      else
               '0';

Example: |align_left| set to |default_yes|
##########################################

The following code would fail with this option:

.. code-Block:: vhdl

     output <= '1' when input = "0000" else
               sig_a or sig_b when input = "0100" and input = "1100" else
               sig_c when input = "10" else
               '0';

The following code would pass with this option:

.. code-block:: vhdl

     output <= '1' when input = "0000" else
       sig_a or sig_b when input = "0100" and input = "1100" else
       sig_c when input = "10" else
       '0';

Example: |align_left| set to |default_no|
#########################################

The following code would fail with this option:

.. code-Block:: vhdl

     output <= '1' when input = "0000" else
       sig_a or sig_b when input = "0100" and input = "1100" else
       sig_c when input = "10" else
       '0';

The following code would pass with this option:

.. code-block:: vhdl

     output <= '1' when input = "0000" else
               sig_a or sig_b when input = "0100" and input = "1100" else
               sig_c when input = "10" else
               '0';

Example: |align_paren| set to |default_yes| and |align_left| set to |default_no|
################################################################################

The following code would fail with this option:

.. code-block:: vhdl

   output <= '1' when func1(func2(G_VALUE1,
                        G_VALUE2), func3(
                        G_VALUE3)
                        ) else
             '0';

The following code would pass with this option:

.. code-block:: vhdl

   output <= '1' when func1(func2(G_VALUE1,
                                   G_VALUE2), func3(
                                                     G_VALUE3)
                           ) else
             '0';

Rules Enforcing Conditional Expression Alignment
################################################

* `concurrent_009 <concurrent_rules.html#concurrent-009>`_
* `sequential_401 <sequential_rules.html#sequential-401>`_
* `variable_assignment_400 <variable_assignment_400.html#variable-assignment-400>`_

