
.. _configuring-multiline-indent-rules:

Configuring Multiline Indent Rules
----------------------------------

There are rules which will check indent of multiline expressions and conditions.

There are several options to these rules:

.. |align_left| replace::
   :code:`align_left`

.. |align_paren| replace::
   :code:`align_paren`

.. |values| replace::
   :code:`yes`, :code:`no`

.. |default_yes| replace::
   :code:`yes`

.. |default_no| replace::
   :code:`no`   

+---------------+----------+---------------+-----------------------------------------------------------+
| Option        | Values   | Default       | Description                                               |
+===============+==========+===============+===========================================================+
| |align_left|  | |values| | |default_yes| | |default_yes| = New lines will be aligned left.           |
|               |          |               | |default_no| = Align to right of assignment operator.     |
+---------------+----------+---------------+-----------------------------------------------------------+
| |align_paren| | |values| | |default_no|  | |default_yes| = Use open parenthesis for alignment.       |
|               |          |               | |default_no| = Do not use open parenthesis for alignment. |
+---------------+----------+---------------+-----------------------------------------------------------+

This is an example of how to configure the option.

.. code-block:: yaml

   rule :
     constant_012:
        align_left : "no"
        align_paren : "yes"

.. NOTE:: All examples below are using the rule **constant_012**.

All examples use the following code snippet:

.. code-block:: vhdl

   constant c_const : t_type :=
   (
     1 => func1(G_GENERIC1, 
                G_GENERIC2, G_GENERIC2),
     2 => func2(G_GENERIC2, G_GENERIC3,
                G_GENERIC4)
   );

   constant c_const : t_type := (
     1 => func1(G_GENERIC1, 
                G_GENERIC2, G_GENERIC2),
     2 => func2(G_GENERIC2, G_GENERIC3,
                G_GENERIC4)
   );

Example: |align_left| set to |default_yes| and |align_paren| set to |default_no|
################################################################################

.. code-block:: vhdl

   constant c_const : t_type :=
   (
     1 => func1(G_GENERIC1, 
       G_GENERIC2, G_GENERIC2),
     2 => func2(G_GENERIC2, G_GENERIC3,
       G_GENERIC4)
   );

   constant c_const : t_type := (
     1 => func1(G_GENERIC1, 
       G_GENERIC2, G_GENERIC2),
     2 => func2(G_GENERIC2, G_GENERIC3,
       G_GENERIC4)
   );

Example: |align_left| set to |default_no| and |align_paren| set to |default_no|
###############################################################################

.. code-block:: vhdl

   constant c_const : t_type :=
                                (
                                  1 => func1(G_GENERIC1, 
                                    G_GENERIC2, G_GENERIC2),
                                  2 => func2(G_GENERIC2, G_GENERIC3,
                                    G_GENERIC4)
                                );

   constant c_const : t_type := (
                                  1 => func1(G_GENERIC1, 
                                    G_GENERIC2, G_GENERIC2),
                                  2 => func2(G_GENERIC2, G_GENERIC3,
                                    G_GENERIC4)
                                );

Example: |align_left| set to |default_yes| and |align_paren| set to |default_yes|
#################################################################################

.. code-block:: vhdl

   constant c_const : t_type :=
   (
     1 => func1(G_GENERIC1, 
                 G_GENERIC2, G_GENERIC2),
     2 => func2(G_GENERIC2, G_GENERIC3,
                 G_GENERIC4)
   );

   constant c_const : t_type := (
     1 => func1(G_GENERIC1, 
                 G_GENERIC2, G_GENERIC2),
     2 => func2(G_GENERIC2, G_GENERIC3,
                 G_GENERIC4)
   );

Example: |align_left| set to |default_no| and |align_paren| set to |default_yes|
################################################################################

.. code-block:: vhdl

   constant c_const : t_type :=
   (
     1 => func1(G_GENERIC1, 
                 G_GENERIC2, G_GENERIC2),
     2 => func2(G_GENERIC2, G_GENERIC3,
                 G_GENERIC4)
   );

   constant c_const : t_type := (
                                  1 => func1(G_GENERIC1, 
                                              G_GENERIC2, G_GENERIC2),
                                  2 => func2(G_GENERIC2, G_GENERIC3,
                                              G_GENERIC4)
                                );

Rules Enforcing Multiline Indent Rules
######################################

.. * `concurrent_003 <concurrent_rules.html#concurrent-003>`_
* `concurrent_401 <concurrent_rules.html#concurrent-401>`_
* `constant_012 <constant_rules.html#constant-012>`_
.. * `constant_014 <constant_rules.html#constant-014>`_
.. * `process_020 <process_rules.html#process-020>`_
.. * `sequential_004 <sequential_rules.html#sequential-004>`_
* `sequential_402 <sequential_rules.html#sequential-402>`_
.. * `signal_400 <signal_rules.html#signal-400>`_
.. * `variable_assignment_004 <variable_assignment_rules.html#variable-assignment-004>`_
* `variable_assignment_401 <variable_assignment_rules.html#variable-assignment-401>`_
