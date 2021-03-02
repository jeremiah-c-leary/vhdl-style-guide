Configuring Multiline Indent Rules
----------------------------------

There are rules which will check indent of multiline expressions and conditions.

There are several options to these rules:

+----------------------+---------+---------+---------------------------------------------------------+
| Method               |   Type  | Default | Description                                             |
+======================+=========+=========+=========================================================+
| align_left           | boolean |  True   | True = New lines will be aligned left.                  |
|                      |         |         | False = Align to left of assignment operator.           |
+----------------------+---------+---------+---------------------------------------------------------+
| align_paren          | boolean |  True   | True = Use open parenthesis for alignment.              |
|                      |         |         | False = Do not use open parenthesis for alignment.      |
+----------------------+---------+---------+---------------------------------------------------------+

This is an example of how to configure the option.

.. code-block:: yaml

   rule :
     constant_012:
        align_left : False
        align_paren : True

.. NOTE:: All examples below are using the rule **constant_012**.

Example: align_left True, align_paren False
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

Example: align_left False, align_paren False
############################################

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

Example: align_left True, align_paren True
##########################################

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

