Configuring Multiline Structure Rules
--------------------------------------

There are rules which will check indent and formatting of multiline expressions and conditions.

The alignment of multiline rules is handled by a corresponding rule.
Both rules are required to ensure proper formatting of multiline expressions and conditions.
The corresponding rule will be noted in the rule documentation.

There are several options to these rules:

+-----------------------+---------+---------+---------------------------------------------------------+
| Method                |   Type  | Default | Description                                             |
+=======================+=========+=========+=========================================================+
| first_paren_new_line  | string  |  false  | First opening parenthesis on it's own line.             |
+-----------------------+---------+---------+---------------------------------------------------------+
| last_paren_new_line   | string  |  false  | Last closing parenthesis on it's own line.              |
+-----------------------+---------+---------+---------------------------------------------------------+
| open_paren_new_line   | string  |  false  | Insert new line after open parenthesis.                 |
+-----------------------+---------+---------+---------------------------------------------------------+
| close_paren_new_line  | string  |  false  | Insert new line before close parenthesis.               |
+-----------------------+---------+---------+---------------------------------------------------------+
| new_line_after_comma  | string  |  false  | Insert new line after the commas.                       |
+-----------------------+---------+---------+---------------------------------------------------------+
| assign_on_single_line | string  |  true   | Keep assignments on a single line.                      |
+-----------------------+---------+---------+---------------------------------------------------------+
| ignore_single_line    | string  |  true   | Do not apply rules if expression/condition is contained |
|                       |         |         | on a single line.                                       |
+-----------------------+-----------------------------------------------------------------------------+

The options can be combined to format the output.

Each option except :code:`new_line_after_comma` and :code:`assign_on_single_line` allows one of three values:  true, false and ignore.

+----------------------+---------------------------------------------------------+
| Option Value         | Action                                                  |
+======================+=========================================================+
| true                 | Option will be enforced.                                |
+----------------------+---------------------------------------------------------+
| false                | The inverse of the Option will be enforced.             |
+----------------------+---------------------------------------------------------+
| ignore               | The option will be ignored.                             |
+----------------------+---------------------------------------------------------+

The :code:`new_line_after_comma` option allows one of four values:  true, false, ignore and ignore_positional.

+----------------------+--------------------------------------------------------------+
| Option Value         | Action                                                       |
+======================+==============================================================+
| true                 | Insert new line after commas.                                |
+----------------------+--------------------------------------------------------------+
| false                | Remove new line after commas.                                |
+----------------------+--------------------------------------------------------------+
| ignore               | Ignore commas.                                               |
+----------------------+--------------------------------------------------------------+
| ignore_positional    | Insert new line after commas unless elements are positional. |
+----------------------+--------------------------------------------------------------+

The :code:`assign_on_single_line` option allows one of two values:  true and ignore.

+----------------------+--------------------------------------------------------------+
| Option Value         | Action                                                       |
+======================+==============================================================+
| true                 | Force assignments to a single line.                          |
+----------------------+--------------------------------------------------------------+
| ignore               | Allow assignments to span multiple lines.                    |
+----------------------+--------------------------------------------------------------+

This is an example of how to configure these options.

.. code-block:: yaml

   rule :
     constant_012:
        first_paren_new_line : 'true'
        last_paren_new_line : 'true'
        open_paren_new_line : 'true'
        close_paren_new_line : 'true'
        new_line_after_comma : 'ignore'
        ignore_single_line : 'false'

.. NOTE:: All examples below are using the rule **constant_012** and the option ignore_single_line is False.

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
#############################################################################################

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

Example: all options True
#########################

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

Example: all options False
##########################

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

