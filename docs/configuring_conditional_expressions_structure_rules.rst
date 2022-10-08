
.. _configuring-concurrent-structure-rules:

Configuring Concurrent Structure Rules
--------------------------------------

There are rules which will check the structure of conditional expressions and waveforms.

The alignment of multiline rules is handled by a corresponding rule.
Both rules are required to ensure proper formatting of multiline conditional expressions and waveforms.
The corresponding rule will be noted in the rule documentation.

There are several options to these rules:

+-----------------------+---------+---------+---------------------------------------------------------+
| Method                |   Type  | Default | Description                                             |
+=======================+=========+=========+=========================================================+
| new_line_after_assign | string  |   no    | First opening parenthesis on its own line.              |
+-----------------------+---------+---------+---------------------------------------------------------+
| ignore_single_line    | string  |   yes   | Do not apply rules if expression/condition is contained |
|                       |         |         | on a single line.                                       |
+-----------------------+---------+---------+---------------------------------------------------------+

The options can be combined to format the output.

Each option except :code:`ignore_single_line` allows one of three values:  yes, no and ignore.

+----------------------+---------------------------------------------------------+
| Option Value         | Action                                                  |
+======================+=========================================================+
| yes                  | Option will be enforced.                                |
+----------------------+---------------------------------------------------------+
| no                   | The inverse of the Option will be enforced.             |
+----------------------+---------------------------------------------------------+
| ignore               | The option will be ignored.                             |
+----------------------+---------------------------------------------------------+

The :code:`ignore_single_line` option allows one of two values:  yes and ignore.

+----------------------+--------------------------------------------------------------+
| Option Value         | Action                                                       |
+======================+==============================================================+
| yes                  | Force assignments to a single line.                          |
+----------------------+--------------------------------------------------------------+
| ignore               | Allow assignments to span multiple lines.                    |
+----------------------+--------------------------------------------------------------+

This is an example of how to configure these options.

.. code-block:: yaml

   rule :
     concurrent_011:
        ignore_single_line : 'no'

.. NOTE:: All examples below are using the rule **concurrent_011** and the option ignore_single_line is 'no'.

Example: new_line_after_assign
##############################

The following code would fail with this option:

.. code-Block:: vhdl

    write_en <= '1' when sig1 = "00" else '0';

The following code would pass with this option:

.. code-block:: vhdl

    write_en <=
      '1' when sig1 = "00" else '0';

Rules Enforcing Conditional Expression Structure
################################################

* `concurrent_011 <concurrent_rules.html#concurrent-011>`_
