Configuring Multiline Rules
---------------------------

There are rules which will check indent and formatting of multiline expressions and conditions.

There are several options to these rules:

+----------------------+---------+---------+---------------------------------------------------------+
| Method               |   Type  | Default | Description                                             |
+======================+=========+=========+=========================================================+
| first_paren_new_line | boolean |  False  | First opening parenthesis on it's own line.             |
+----------------------+---------+---------+---------------------------------------------------------+
| last_paren_new_line  | boolean |  False  | Last closing parenthesis on it's own line.              |
+----------------------+---------+---------+---------------------------------------------------------+
| open_paren_new_line  | boolean |  False  | Insert new line after open parenthesis.                 |
+----------------------+---------+---------+---------------------------------------------------------+
| close_paren_new_line | boolean |  False  | Insert new line before close parenthesis.               |
+----------------------+---------+---------+---------------------------------------------------------+
| new_line_after_comma | boolean |  False  | Insert new line after the commas.                       |
+----------------------+---------+---------+---------------------------------------------------------+
| align_left           | boolean |  True   | True = New lines will be aligned left.                  |
|                      |         |         | False = Align to current column                         |
+----------------------+---------+---------+---------------------------------------------------------+
| ignore_single_line   | boolean |  True   | Do not apply rules if expression/condition is contained |
|                      |         |         | on a single line.                                       |
+----------------------+-----------------------------------------------------------------------------+

The options can be combined to format the output.

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
     constant_012:
        first_paren_new_line : True
        last_paren_new_line : True
        open_paren_new_line : True
        close_paren_new_line : True
        new_line_after_comma : Ignore
        ignore_single_line : False

.. NOTE:: All examples below are using the rule **constant_012**.

Example: first_paren_new_line and align_left and not ignore_single_line
#######################################################################

The following code would fail with this option:

.. code-Block:: vhdl

    constant c_const : t_type := (a => 0, b => 1);

The following code would pass with this option:

.. code-block:: vhdl

    constant c_const : t_type :=
    (a => 0, b => 1);

Example: first_paren_new_line and not align_left and not ignore_single_line
###########################################################################

The following code would fail with this option:

.. code-Block:: vhdl

    constant c_const : t_type := (a => 0, b => 1);

The following code would pass with this option:

.. code-block:: vhdl

    constant c_const : t_type :=
                                 (a => 0, b => 1);

Example: last_paren_new_line and align_left and not ignore_single_line
######################################################################

The following code would fail with this option:

.. code-Block:: vhdl

    constant c_const : t_type := (a => 0, b => 1);

The following code would pass with this option:

.. code-block:: vhdl

    constant c_const : t_type := (a => 0, b => 1
    );

Example: last_paren_new_line and not align_left and not ignore_single_line
##########################################################################

The following code would fail with this option:

.. code-Block:: vhdl

    constant c_const : t_type := (a => 0, b => 1);

The following code would pass with this option:

.. code-block:: vhdl

    constant c_const : t_type := (a => 0, b => 1
                                 );

Example: first_paren_new_line and last_paren_new_line and align_left and not ignore_single_line
###############################################################################################

The following code would fail with this option:

.. code-Block:: vhdl

    constant c_const : t_type := (a => 0, b => 1);

The following code would pass with this option:

.. code-block:: vhdl

    constant c_const : t_type :=
    (
      a => 0, b => 1
    );

Example: first_paren_new_line and last_paren_new_line and not align_left and not ignore_single_line
###################################################################################################

The following code would fail with this option:

.. code-Block:: vhdl

    constant c_const : t_type := (a => 0, b => 1);

The following code would pass with this option:

.. code-block:: vhdl

    constant c_const : t_type :=
                                 (
                                   a => 0, b => 1
                                 );

Example: new_line_after_comma and align_left and not ignore_single_line
#######################################################################

The following code would fail with this option:

.. code-Block:: vhdl

    constant c_const : t_type := (a => 0, b => 1);

The following code would pass with this option:

.. code-block:: vhdl

    constant c_const : t_type := (a => 0,
    b => 1);

Example: new_line_after_comma and not align_left and not ignore_single_line
###########################################################################

The following code would fail with this option:

.. code-Block:: vhdl

    constant c_const : t_type := (a => 0, b => 1);

The following code would pass with this option:

.. code-block:: vhdl

    constant c_const : t_type := (a => 0,
                                  b => 1);

Example: new_line_after_comma and align_left and first_paren_new_line and last_paren_new_line and not ignore_single_line
########################################################################################################################

The following code would fail with this option:

.. code-Block:: vhdl

    constant c_const : t_type := (a => 0, b => 1);

The following code would pass with this option:

.. code-block:: vhdl

    constant c_const : t_type :=
    (a => 0,
     b => 1);

Example: new_line_after_comma and not align_left and first_paren_new_line and last_paren_new_line and not ignore_single_line
############################################################################################################################

The following code would fail with this option:

.. code-Block:: vhdl

    constant c_const : t_type := (a => 0, b => 1);

The following code would pass with this option:

.. code-block:: vhdl

    constant c_const : t_type :=
                                 (a => 0,
                                  b => 1);

Example: open_paren_new_line and align_left and not ignore_single_line
######################################################################

The following code would fail with this option:

.. code-Block:: vhdl

    constant c_const : t_type := ((a => 0, b => 1), (c => 0, d => 1));

The following code would pass with this option:

.. code-block:: vhdl

    constant c_const : t_type := (
    (
      a => 0, b => 1), (
    c => 0, d => 1));

Example: open_paren_new_line and not align_left and not ignore_single_line
##########################################################################

The following code would fail with this option:

.. code-Block:: vhdl

    constant c_const : t_type := ((a => 0, b => 1), (c => 0, d => 1));

The following code would pass with this option:

.. code-block:: vhdl

    constant c_const : t_type := (
                                  (
                                   a => 0, b => 1), (
                                  c => 0, d => 1));

Example: close_paren_new_line and align_left and not ignore_single_line
#######################################################################

The following code would fail with this option:

.. code-Block:: vhdl

    constant c_const : t_type := ((a => 0, b => 1), (c => 0, d => 1));

The following code would pass with this option:

.. code-block:: vhdl

    constant c_const : t_type := ((a => 0, b => 1
                                  ), (c => 0, d => 1
                                  ));

Example: close_paren_new_line and not align_left and not ignore_single_line
###########################################################################

The following code would fail with this option:

.. code-Block:: vhdl

    constant c_const : t_type := ((a => 0, b => 1), (c => 0, d => 1));

The following code would pass with this option:

.. code-block:: vhdl

    constant c_const : t_type := (
                                  (
                                   a => 0, b => 1), (
                                  c => 0, d => 1));

Example: open_paren_new_line and close_paren_new_line and align_left and not ignore_single_line
###############################################################################################

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

Example: open_paren_new_line and close_paren_new_line and not align_left
########################################################################

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

Example: all options enabled except ignore_single_line
######################################################

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

Example: all options enabled except align_left and ignore_single_line
#####################################################################

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
