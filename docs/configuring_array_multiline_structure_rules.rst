.. _configuring-array-multiline-structure-rules:

Configuring Array Multiline Structure Rules
-------------------------------------------

There are rules which will check indent and formatting of multiline expressions and conditions.

The alignment of multiline rules is handled by a corresponding rule.
Both rules are required to ensure proper formatting of multiline expressions and conditions.
The corresponding rule will be noted in the rule documentation.

There are several options to these rules:

+-----------------------+---------+---------+---------------------------------------------------------+
| Method                |   Type  | Default | Description                                             |
+=======================+=========+=========+=========================================================+
| first_paren_new_line  | string  |   yes   | First opening parenthesis on its own line.              |
+-----------------------+---------+---------+---------------------------------------------------------+
| last_paren_new_line   | string  |   yes   | Last closing parenthesis on its own line.               |
+-----------------------+---------+---------+---------------------------------------------------------+
| open_paren_new_line   | string  |   yes   | Insert new line after open parenthesis.                 |
+-----------------------+---------+---------+---------------------------------------------------------+
| close_paren_new_line  | string  |   yes   | Insert new line before close parenthesis.               |
+-----------------------+---------+---------+---------------------------------------------------------+
| new_line_after_comma  | string  |   yes   | Insert new line after the commas.                       |
+-----------------------+---------+---------+---------------------------------------------------------+
| assign_on_single_line | string  |   yes   | Keep assignments on a single line.                      |
+-----------------------+---------+---------+---------------------------------------------------------+
| ignore_single_line    | string  |   yes   | Do not apply rules if expression/condition is contained |
|                       |         |         | on a single line.                                       |
+-----------------------+---------+---------+---------------------------------------------------------+
| move_last_comment     | string  | ignore  | If last_paren_new_line is 'yes', then move any trailing |
|                       |         |         | comments to the previous  line.                         |
+-----------------------+---------+---------+---------------------------------------------------------+

The options can be combined to format the output.

Each option except :code:`new_line_after_comma` and :code:`assign_on_single_line` allows one of three values:  yes, no and ignore.

+----------------------+---------------------------------------------------------+
| Option Value         | Action                                                  |
+======================+=========================================================+
| yes                  | Option will be enforced.                                |
+----------------------+---------------------------------------------------------+
| no                   | The inverse of the Option will be enforced.             |
+----------------------+---------------------------------------------------------+
| ignore               | The option will be ignored.                             |
+----------------------+---------------------------------------------------------+

The :code:`new_line_after_comma` option allows one of four values:  yes, no, ignore and ignore_positional.

+----------------------+--------------------------------------------------------------+
| Option Value         | Action                                                       |
+======================+==============================================================+
| yes                  | Insert new line after commas.                                |
+----------------------+--------------------------------------------------------------+
| no                   | Remove new line after commas.                                |
+----------------------+--------------------------------------------------------------+
| ignore               | Ignore commas.                                               |
+----------------------+--------------------------------------------------------------+
| ignore_positional    | Insert new line after commas unless elements are positional. |
+----------------------+--------------------------------------------------------------+

The :code:`assign_on_single_line` option allows one of two values:  yes and ignore.

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
     constant_012:
        first_paren_new_line : 'yes'
        last_paren_new_line : 'yes'
        open_paren_new_line : 'yes'
        close_paren_new_line : 'yes'
        new_line_after_comma : 'ignore'
        ignore_single_line : 'no'

.. NOTE:: All examples below are using the rule **constant_016** and the option ignore_single_line is False.

Example: first_paren_new_line
#############################

The following code would fail with this option:

.. code-Block:: vhdl

    constant c_const : t_type := (a => 0, b => 1);

The following code would pass with this option:

.. code-block:: vhdl

    constant c_const : t_type :=
    (a => 0, b => 1);

Example: last_paren_new_line
############################

The following code would fail with this option:

.. code-Block:: vhdl

    constant c_const : t_type := (a => 0, b => 1);

The following code would pass with this option:

.. code-block:: vhdl

    constant c_const : t_type := (a => 0, b => 1
    );

Example: first_paren_new_line and last_paren_new_line
#####################################################

The following code would fail with this option:

.. code-Block:: vhdl

    constant c_const : t_type := (a => 0, b => 1);

The following code would pass with this option:

.. code-block:: vhdl

    constant c_const : t_type :=
    (
      a => 0, b => 1
    );

Example: new_line_after_comma
#############################

The following code would fail with this option:

.. code-Block:: vhdl

    constant c_const : t_type := (a => 0, b => 1);

The following code would pass with this option:

.. code-block:: vhdl

    constant c_const : t_type := (a => 0,
    b => 1);

Example: new_line_after_comma and first_paren_new_line and last_paren_new_line 
##############################################################################

The following code would fail with this option:

.. code-Block:: vhdl

    constant c_const : t_type := (a => 0, b => 1);

The following code would pass with this option:

.. code-block:: vhdl

    constant c_const : t_type :=
    (a => 0,
     b => 1);

Example: open_paren_new_line
############################

The following code would fail with this option:

.. code-Block:: vhdl

    constant c_const : t_type := ((a => 0, b => 1), (c => 0, d => 1));

The following code would pass with this option:

.. code-block:: vhdl

    constant c_const : t_type := (
    (
      a => 0, b => 1), (
    c => 0, d => 1));

Example: close_paren_new_line
#############################

The following code would fail with this option:

.. code-Block:: vhdl

    constant c_const : t_type := ((a => 0, b => 1), (c => 0, d => 1));

The following code would pass with this option:

.. code-block:: vhdl

    constant c_const : t_type := ((a => 0, b => 1
                                  ), (c => 0, d => 1
                                  ));

Example: open_paren_new_line and close_paren_new_line
#####################################################

The following code would fail with this option:

.. code-Block:: vhdl

    constant c_const : t_type := ((a => 0, b => 1), (c => 0, d => 1));

The following code would pass with this option:

.. code-block:: vhdl

    constant c_const : t_type := (
    (
      a => 0, b => 1
    ), (
      c => 0, d => 1
    ));

Example: all options yes
########################

The following code would fail with this option:

.. code-Block:: vhdl

    constant c_const : t_type := ((a => 0, b => 1), (c => 0, d => 1));

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

Example: all options no
#######################

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

The following code would fail with this option:

.. code-Block:: vhdl

    constant c_const : t_type := ((a => 0, b => 1), (c => 0, d => 1));

Example: assign_on_single_line
##############################

The following code would pass with this option set to True:

.. code-block:: vhdl

    constant c_const : t_type :=
    (
      1 => func1(std_logic_vector(G_GEN), G_GEN2),
      2 => func1(std_logic_vector(G_GEN), G_GEN2)
    );

The following code would fail with this option set to True:

.. code-block:: vhdl

    constant c_const : t_type :=
    (
      1 => func1(std_logic_vector(G_GEN), G_GEN2),
      2 => func1(
                 std_logic_vector(G_GEN), G_GEN2)
    );

Example: last_paren_new_line and move_last_comment
##################################################

The following code would fail with this option:

.. code-Block:: vhdl

    constant c_const : t_type :=
    (
      a => 0,
      b => 1); -- Comment

The following code would pass with this option:

.. code-block:: vhdl

    constant c_const : t_type :=
    (
      a => 0,
      b => 1 -- Comment
    );

Rules Enforcing Array Multiline Structure Rules
###############################################

* `constant_012 <constant_rules.html#constant-012>`_
* `constant_016 <constant_rules.html#constant-016>`_
* `sequential_009 <sequential_rules.html#sequential-009>`_
* `signal_016 <signal_rules.html#signal-016>`_
* `variable_assignment_008 <variable_assignment_rules.html#variable-assignment-008>`_
