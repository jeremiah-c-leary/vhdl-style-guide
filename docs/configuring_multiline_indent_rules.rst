Configuring Multiline Indent Rules
----------------------------------

There are rules which will check indent of multiline expressions and conditions.

There are several options to these rules:

+----------------------+---------+---------+---------------------------------------------------------+
| Method               |   Type  | Default | Description                                             |
+======================+=========+=========+=========================================================+
| align_left           | boolean |  True   | True = New lines will be aligned left.                  |
|                      |         |         | False = Align to left of assignment operator.           |
+----------------------+-----------------------------------------------------------------------------+
| indent_step          | integer |    1    | Sets how many columns to the right to check for         |
|                      |         |         | alignment.                                              |
+----------------------+-----------------------------------------------------------------------------+
| align_paren          | boolean |  True   | True = Use open parenthesis for alignment.              |
|                      |         |         | False = Do not use open parenthesis for alignment.      |
+----------------------+-----------------------------------------------------------------------------+

This is an example of how to configure the option.

.. code-block:: yaml

   rule :
     constant_012:
        align_left : False
        indent_step : 2

.. NOTE:: All examples below are using the rule **constant_012**.

Example: align_left True and indent_step 1
##########################################

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

Example: align_left True and indent_step 2
##########################################

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

Example: align_left False and indent_step 2
###########################################

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

Example: align_left True and indent_step 2 and align_paren True
###############################################################

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

Example: align_left True and indent_step 2 and align_paren False
################################################################

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

