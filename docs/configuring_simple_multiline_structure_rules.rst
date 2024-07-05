.. _configuring-simple-multiline-structure-rules:

Configuring Simple Multiline Structure Rules
--------------------------------------------

.. |new_line_after_assign| replace::
   :code:`new_line_after_assign`

.. |new_line_after_assign__yes| replace::
   :code:`yes` =  Adds a carriage return (alias "new line") after the assignment operator.

.. |new_line_after_assign__no| replace::
   :code:`no` = Removes a carriage return (alias "new line") after the assignment operator.

.. |new_line_after_assign__ignore| replace::
   :code:`ignore` = Ignores any formatting after the assignment operator.

.. |values1| replace::
   :code:`yes`, :code:`no`, :code:`ignore`

.. |values2| replace::
   :code:`yes`, :code:`no`

.. |ignore_single_line| replace::
   :code:`ignore_single_line`

.. |ignore_single_line__yes| replace::
   :code:`yes` = Ignore single line expressions.

.. |ignore_single_line__no| replace::
   :code:`no` =  Apply rules to single line expressions.

.. |default_yes| replace::
   :code:`yes`

.. |default_no| replace::
   :code:`no`

There are rules which will check the structure of simple multiline expressions and conditions.

There are several options to these rules:

+-------------------------+-------------+---------------+-----------------------------------+
| Method                  | Values      | Default       | Description                       |
+=========================+=============+===============+===================================+
| |new_line_after_assign| | |values1|   | |default_yes| | * |new_line_after_assign__yes|    |
|                         |             |               | * |new_line_after_assign__no|     |
|                         |             |               | * |new_line_after_assign__ignore| |
+-------------------------+-------------+---------------+-----------------------------------+
| |ignore_single_line|    | |values2|   | |default_yes| | * |ignore_single_line__yes|       |
|                         |             |               | * |ignore_single_line__no|        |
+-------------------------+-------------+---------------+-----------------------------------+

This is an example of how to configure these options.

.. code-block:: yaml

   rule :
     concurrent_011:
        new_line_after_assign : 'yes'
        ignore_single_line : 'no'

The following code snippet will be used in the following examples:

.. code-block:: vhdl

   wr_en <= '1' when fifo_full = '0' else
            '0';

   rd_en <=
            '1' when fifo_empty = '0' else
            '0';

.. NOTE:: In the examples below, indenting is performed by a different rule.

Example: |new_line_after_assign| set to |default_yes|
#####################################################

Code after the assignment operator :code:`<=` will be moved to the next line.

.. code-Block:: vhdl

   wr_en <=
            '1' when fifo_full = '0' else
            '0';

   rd_en <=
            '1' when fifo_empty = '0' else
            '0';

Example: |new_line_after_assign| set to |default_no|
####################################################

Code after the assignment operator :code:`<=` will be enforced.

.. code-Block:: vhdl

   wr_en <= '1' when fifo_full = '0' else
            '0';

   rd_en <= '1' when fifo_empty = '0' else
            '0';

Rules Enforcing Multiline Structure Rules
#########################################

* `concurrent_011 <concurrent_rules.html#concurrent-011>`_
* `sequential_008 <sequential_rules.html#sequential-008>`_
* `variable_assignment_007 <variable_assignment_rules.html#variable-assignment-007>`_
