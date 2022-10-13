.. _configuring-simple-multiline-structure-rules:

.. |new_line_after_assign| replace::
   :code:`new_line_after_assign`

.. |ignore_single_line| replace::
   :code:`ignore_single_line`

Configuring Simple Multiline Structure Rules
--------------------------------------------

There are rules which will check the structure of simple multiline expressions and conditions.

There are several options to these rules:

+-------------------------+---------+---------+---------------------------------------------------------+
| Method                  |   Type  | Default | Description                                             |
+=========================+=========+=========+=========================================================+
| |new_line_after_assign| | string  |   yes   | Insert new line after the assignment token.             |
+-------------------------+---------+---------+---------------------------------------------------------+
| |ignore_single_line|    | string  |   yes   | Do not apply rules if expression/condition is contained |
|                         |         |         | on a single line.                                       |
+-------------------------+---------+---------+---------------------------------------------------------+

The options can be combined to format the output.

The option |new_line_after_assign| allows one of three values:  yes, no and ignore.

+----------------------+---------------------------------------------------------+
| Option Value         | Action                                                  |
+======================+=========================================================+
| yes                  | Option will be enforced.                                |
+----------------------+---------------------------------------------------------+
| no                   | The inverse of the Option will be enforced.             |
+----------------------+---------------------------------------------------------+
| ignore               | The option will be ignored.                             |
+----------------------+---------------------------------------------------------+

The option |ignore_single_line| allows one of two values:  yes and no.

+----------------------+---------------------------------------------------------+
| Option Value         | Action                                                  |
+======================+=========================================================+
| yes                  | Ignore single line expressions.                         |
+----------------------+---------------------------------------------------------+
| no                   | Apply rules to single line expressions.                 |
+----------------------+---------------------------------------------------------+


This is an example of how to configure these options.

.. code-block:: yaml

   rule :
     concurrent_011:
        new_line_after_assign : 'yes'
        ignore_single_line : 'no'

.. NOTE:: All examples below are using the rule **constant_011** and the option ignore_single_line is False.

Example: |new_line_after_assign|
################################

The following code would fail with this option set to 'yes':

.. code-Block:: vhdl

   wr_en <= '1' when fifo_full = '0' else
            '0';
    

The following code would pass with this option:

.. code-block:: vhdl

   wr_en <=
            '1' when fifo_full = '0' else
            '0';
    
Rules Enforcing Multiline Structure Rules
#########################################

* `concurrent_011 <concurrent_rules.html#concurrent-011>`_
* `signal_016 <signal_rules.html#signal-016>`_
