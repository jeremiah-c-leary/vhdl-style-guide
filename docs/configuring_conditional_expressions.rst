Configuring Conditional Expressions and Conditional Waveforms
-------------------------------------------------------------

There are rules which will check indent and formatting of multiline conditional expressions and conditional waveforms.

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

+---------------------------+---------+---------+---------------------------------------------------------+
| Option                    |   Type  | Default | Description                                             |
+===========================+=========+=========+=========================================================+
| align_left                | string  |  'no'   | Align multilines to the left                            |
+---------------------------+---------+---------+---------------------------------------------------------+
| align_paren               | string  |  'yes'  | Indent lines based on parenthesis                       |
+---------------------------+---------+---------+---------------------------------------------------------+
| align_when_keywords       | string  |  'no'   | each when keyword will be aligned                       |
+---------------------------+---------+---------+---------------------------------------------------------+
| wrap_at_when              | string  |  'yes'  | Indent multiline condition at when keyword.             |
+---------------------------+---------+---------+---------------------------------------------------------+
| align_else_keywords       | string  |  'no'   | each else keyword will be aligned                       |
+---------------------------+---------+---------+---------------------------------------------------------+

The options can be combined to format the conditional expression or conditional waveform.

Each option allows one two values:  'yes' and 'no'.

+----------------------+---------------------------------------------------------+
| Option Value         | Action                                                  |
+======================+=========================================================+
| 'yes'                | Option will be enforced.                                |
+----------------------+---------------------------------------------------------+
| 'no'                 | The inverse of the Option will be enforced.             |
+----------------------+---------------------------------------------------------+

This is an example of how to configure these options.

.. code-block:: yaml

   rule :
     constant_009:
        wrap_condition_at_when : 'yes'
        align_when_keywords : 'yes'
        align_else_keywords : 'yes'
        align_left : 'no'
        ignore_single_line : 'yes'

.. NOTE:: All examples below are using the rule **concurrent_009**.

Example: indent_condition_at_when
#################################

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

Example: align_when_keywords
############################

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

Example: align_when_keywords and align_else_keywords
####################################################

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

Example: align_left 'yes'
#########################

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

Example: align_left 'no'
########################

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
