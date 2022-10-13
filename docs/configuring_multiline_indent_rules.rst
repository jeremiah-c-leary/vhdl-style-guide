
.. _configuring-multiline-indent-rules:

Configuring Multiline Indent Rules
----------------------------------

There are rules which will check indent of multiline expressions and conditions.

There are several options to these rules:

+----------------------+---------+---------+---------------------------------------------------------+
| Method               |   Type  | Default | Description                                             |
+======================+=========+=========+=========================================================+
| align_left           | string  |  "yes"  | "yes" = New lines will be aligned left.                 |
|                      |         |         | "no" = Align to right of assignment operator.           |
+----------------------+---------+---------+---------------------------------------------------------+
| align_paren          | string  |  "no"   | "yes" = Use open parenthesis for alignment.             |
|                      |         |         | "no" = Do not use open parenthesis for alignment.       |
+----------------------+---------+---------+---------------------------------------------------------+

This is an example of how to configure the option.

.. code-block:: yaml

   rule :
     constant_012:
        align_left : "no"
        align_paren : "yes"

.. NOTE:: All examples below are using the rule **constant_012**.

Example: align_left "yes", align_paren "no"
###########################################

The following code would fail with this option:

.. code-Block:: vhdl

    constant c_const : t_type :=
                                 (
                                   (
                                     a => 0,
                                     b => 1
                                   ),
                                   (
                                     c => 0,
                                     d => 1
                                   )
                                 );

    constant c_const : t_type :=
    (
     (
      a => 0,
      b => 1
     ),
     (
      c => 0,
      d => 1
     )
    );

The following code would pass with this option:

.. code-block:: vhdl

    constant c_const : t_type :=
    (
      (
        a => 0,
        b => 1
      ),
      (
        c => 0,
        d => 1
      )
    );

    constant c_const : t_type :=
    (
      (
        a => 0,
        b => 1
      ),
      (
        c => 0,
        d => 1
      )
    );

Example: align_left "no", align_paren "no"
##########################################

The following code would fail with this option:

.. code-block:: vhdl

    constant c_const : t_type :=
    (
      (
        a => 0,
        b => 1
      ),
      (
        c => 0,
        d => 1
      )
    );

The following code would pass with this option:

.. code-Block:: vhdl

    constant c_const : t_type :=
                                 (
                                   (
                                     a => 0,
                                     b => 1
                                   ),
                                   (
                                     c => 0,
                                     d => 1
                                   )
                                 );

Example: align_left "yes", align_paren "yes"
############################################

The following code would fail with this option:

.. code-block:: vhdl

   constant c_const : t_type := (
     1 => func1(
       G_GENERIC1, G_GENERIC2)
   );

The following code would pass with this option:

.. code-block:: vhdl

   constant c_const : t_type := (
     1 => func1(
                  G_GENERIC1, G_GENERIC2)
   );

Rules Enforcing Multiline Indent Rules
######################################

* `concurrent_003 <concurrent_rules.html#concurrent-003>`_
* `concurrent_401 <concurrent_rules.html#concurrent-401>`_
* `constant_012 <constant_rules.html#constant-012>`_
* `constant_014 <constant_rules.html#constant-014>`_
* `if_004 <if_rules.html#if-004>`_
* `process_020 <process_rules.html#process-020>`_
* `sequential_004 <sequential_rules.html#sequential-004>`_
* `sequential_402 <sequential_rules.html#sequential-402>`_
* `signal_400 <signal_rules.html#signal-400>`_
* `variable_assignment_004 <variable_assignment_rules.html#variable-assignment-004>`_
* `variable_assignment_401 <variable_assignment_rules.html#variable-assignment-401>`_
