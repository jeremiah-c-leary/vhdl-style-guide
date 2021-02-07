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
| first_expression_new_line | boolean |  False  | First opening parenthesis on it's own line.             |
+---------------------------+---------+---------+---------------------------------------------------------+
| indent_condition_at_when  | boolean |  True   | Indent multiline condition at when keyword.             |
+---------------------------+---------+---------+---------------------------------------------------------+
| align_when_keywords       | boolean |  Ignore | each when keyword will be aligned                       |
+---------------------------+---------+---------+---------------------------------------------------------+
| align_else_keywords       | boolean |  Ignore | each else keyword will be aligned                       |
+---------------------------+---------+---------+---------------------------------------------------------+
| align_left                | boolean |  False  | Align multilines to the left                            |
+---------------------------+---------+---------+---------------------------------------------------------+
| open_paren_new_line       | boolean |  Ignore | Insert new line after open parenthesis.                 |
+---------------------------+---------+---------+---------------------------------------------------------+
| close_paren_new_line      | boolean |  Ignore | Insert new line before close parenthesis.               |
+---------------------------+---------+---------+---------------------------------------------------------+
| ignore_single_line        | boolean |  True   | Do not apply rules if expression/condition is contained |
|                           |         |         | on a single line.                                       |
+---------------------------+-----------------------------------------------------------------------------+

The options can be combined to format the conditional expression or conditional waveform.

Each option allows one of three values:  True, False and Ignore.

+----------------------+---------------------------------------------------------+
| Option Value         | Action                                                  |
+======================+=========================================================+
| True                 | Option will be enforced.                                |
+----------------------+---------------------------------------------------------+
| False                | The inverse of the Option will be enforced.             |
+----------------------+---------------------------------------------------------+
| Ignore               | The option will be ignored.                             |
+----------------------+---------------------------------------------------------+

This is an example of how to configure these options.

.. code-block:: yaml

   rule :
     constant_009:
        first_expression_new_line : False
        wrap_condition_at_when : True
        align_when_keywords : 'Ignore'
        align_else_keywords : 'Ignore'
        align_left : False
        open_paren_new_line : 'Ignore'
        close_paren_new_line : 'Ignore'
        ignore_single_line : True

.. NOTE:: All examples below are using the rule **concurrent_009** and the option ignore_single_line is False.

Example: first_expression_new_line
##################################

The following code would fail with this option:

.. code-Block:: vhdl

     output <= '1' when input = "00" else
               sig_a or sig_b when input = "01" else
               sig_c and sig_d when input = "10" else
               '0';

The following code would pass with this option:

.. code-block:: vhdl

     output <=
               '1' when input = "00" else
               sig_a or sig_b when input = "01" else
               sig_c and sig_d when input = "10" else
               '0';

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

Example: align_left True
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

Example: align_left False
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

Example: first_expression_new_line and align_when_keywords and align_else_keywords and align_left
#################################################################################################

The following code would fail with this option:

.. code-Block:: vhdl

     output <= '1' when input = "0000" else
               sig_a or sig_b when input = "0100" and input = "1100" else
               sig_c when input = "10" else
               '0';

The following code would pass with this option:

.. code-block:: vhdl

     output <=
       '1'            when input = "0000"                    else
       sig_a or sig_b when input = "0100" and input = "1100" else
       sig_c          when input = "10"                      else
       '0';

