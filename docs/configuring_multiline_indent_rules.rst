
.. _configuring-multiline-indent-rules:

Configuring Multiline Indent Rules
----------------------------------

There are rules which will check indent of multiline expressions and conditions.

There are several options to these rules:

.. |align_left| replace::
   :code:`align_left`

.. |align_left__yes| replace::
   :code:`yes` = Lines will be aligned left

.. |align_left__no| replace::
   :code:`no` = Lines will be aligned to assignment operator

.. |align_paren| replace::
   :code:`align_paren`

.. |align_paren__yes| replace::
   :code:`yes` = Align to unbalanced open parenthesis

.. |align_paren__no| replace::
   :code:`no` = Each unbalanced open parenthesis will add an indent.

.. |values| replace::
   :code:`yes`, :code:`no`

.. |default_yes| replace::
   :code:`yes`

.. |default_no| replace::
   :code:`no`

+---------------+----------+---------------+----------------------+
| Option        | Values   | Default       | Description          |
+===============+==========+===============+======================+
| |align_left|  | |values| | |default_no|  | * |align_left__yes|  |
|               |          |               | * |align_left__no|   |
+---------------+----------+---------------+----------------------+
| |align_paren| | |values| | |default_yes| | * |align_paren__yes| |
|               |          |               | * |align_paren__no|  |
+---------------+----------+---------------+----------------------+

This is an example of how to configure the option.

.. code-block:: yaml

   rule :
     concurrent_003:
        align_left : "no"
        align_paren : "yes"

All examples use the following code snippet:

.. code-block:: vhdl

  wr_en <= resize(unsigned(I_FOO) +
              unsigned(I_BAR), q_foo'length);

  wr_en <=
      resize(unsigned(I_FOO) +
                      unsigned(I_BAR), q_foo'length);

Example: |align_left| set to |default_yes| and |align_paren| set to |default_no|
################################################################################

.. code-block:: vhdl

  wr_en <= resize(unsigned(I_FOO) +
      unsigned(I_BAR), q_foo'length);

  wr_en <=
    resize(unsigned(I_FOO) +
      unsigned(I_BAR), q_foo'length);

Example: |align_left| set to |default_no| and |align_paren| set to |default_no|
###############################################################################

.. code-block:: vhdl

  wr_en <= resize(unsigned(I_FOO) +
             unsigned(I_BAR), q_foo'length);

  wr_en <=
           resize(unsigned(I_FOO) +
             unsigned(I_BAR), q_foo'length);

Example: |align_left| set to |default_yes| and |align_paren| set to |default_yes|
#################################################################################

.. code-block:: vhdl

  wr_en <= resize(unsigned(I_FOO) +
                  unsigned(I_BAR), q_foo'length);

  wr_en <=
    resize(unsigned(I_FOO) +
           unsigned(I_BAR), q_foo'length);

Example: |align_left| set to |default_no| and |align_paren| set to |default_yes|
################################################################################

.. code-block:: vhdl

  wr_en <= resize(unsigned(I_FOO) +
                  unsigned(I_BAR), q_foo'length);

  wr_en <=
           resize(unsigned(I_FOO) +
                  unsigned(I_BAR), q_foo'length);

Rules Enforcing Multiline Indent Rules
######################################

* `concurrent_003 <concurrent_rules.html#concurrent-003>`_
* `concurrent_401 <concurrent_rules.html#concurrent-401>`_
* `constant_012 <constant_rules.html#constant-012>`_
* `constant_014 <constant_rules.html#constant-014>`_
* `if_009 <if_rules.html#if-009>`_
* `procedure_call_400 <procedure_call_rules.html#procedure-call-400>`_
* `process_020 <process_rules.html#process-020>`_
* `selected_assignment_400 <selected_assignment_rules.html#selected-assignment-400>`_
* `sequential_004 <sequential_rules.html#sequential-004>`_
* `sequential_402 <sequential_rules.html#sequential-402>`_
* `signal_400 <signal_rules.html#signal-400>`_
* `variable_400 <signal_rules.html#variable-400>`_
* `variable_402 <signal_rules.html#variable-402>`_
* `variable_assignment_004 <variable_assignment_rules.html#variable-assignment-004>`_
* `variable_assignment_401 <variable_assignment_rules.html#variable-assignment-401>`_
