.. _configuring-array-multiline-structure-rules:

Configuring Array Multiline Structure Rules
-------------------------------------------

There are rules which will check indent and formatting of multiline expressions and conditions.

The alignment of multiline rules is handled by a corresponding rule.
Both rules are required to ensure proper formatting of multiline expressions and conditions.
The corresponding rule will be noted in the rule documentation.

There are several options to these rules:

.. |first_paren_new_line| replace::
   :code:`first_paren_new_line`

.. |first_paren_new_line__yes| replace::
   :code:`yes` = Add new line before first parenthesis.

.. |first_paren_new_line__no| replace::
   :code:`no` = Remove new line before first parenthesis.

.. |ignore_formatting| replace::
   :code:`ignore` = Ignore formatting.

.. |last_paren_new_line| replace::
   :code:`last_paren_new_line`

.. |last_paren_new_line__yes| replace::
   :code:`yes` = Add new line before last parenthesis.

.. |last_paren_new_line__no| replace::
   :code:`no` = Remove new line before last parenthesis.

.. |open_paren_new_line| replace::
   :code:`open_paren_new_line`

.. |open_paren_new_line__yes| replace::
   :code:`yes` = Add new line after open parenthesis.

.. |open_paren_new_line__no| replace::
   :code:`no` = Remove new line after open parenthesis.

.. |close_paren_new_line| replace::
   :code:`close_paren_new_line`

.. |close_paren_new_line__yes| replace::
   :code:`yes` = Add new line before close parenthesis.

.. |close_paren_new_line__no| replace::
   :code:`no` = Remove new line before close parenthesis.

.. |new_line_after_comma| replace::
   :code:`new_line_after_comma`

.. |new_line_after_comma__yes| replace::
   :code:`yes` = Add new line after comma.

.. |new_line_after_comma__no| replace::
   :code:`no` = Remove new line after comma.

.. |new_line_after_comma__ignore_positional| replace::
   :code:`ignore_positional` = Add new line after comma unless elements are positional.

.. |assign_on_single_line| replace::
   :code:`assign_on_single_line`

.. |assign_on_single_line__yes| replace::
   :code:`yes` = Force assignments to single line.

.. |assign_on_single_line__ignore| replace::
   :code:`ignore` = Allow assignments to span multiple lines.

.. |ignore_single_line| replace::
   :code:`ignore_single_line`

.. |ignore_single_line__yes| replace::
   :code:`yes` = Ignore single line expressions.

.. |ignore_single_line__no| replace::
   :code:`no` =  Apply rules to single line expressions.

.. |move_last_comment| replace::
   :code:`move_last_comment`

.. |move_last_comment__yes| replace::
   :code:`yes` = If :code:`last_paren_new_line` is :code:`yes`, then move any trailing comment to the previous line.

.. |yes| replace::
   :code:`yes`

.. |no| replace::
   :code:`no`

.. |ignore| replace::
   :code:`ignore`

.. |values_1| replace::
   :code:`yes`, :code:`no`, :code:`ignore`

.. |values_2| replace::
   :code:`yes`, :code:`no`, :code:`ignore`, :code:`ignore_positional`

.. |values_3| replace::
   :code:`yes`, :code:`ignore`

.. |values_4| replace::
   :code:`yes`, :code:`no`

+-------------------------+------------+----------+----------------------------------------------+
| Option                  |   Values   | Default  | Description                                  |
+=========================+============+==========+==============================================+
| |first_paren_new_line|  | |values_1| | |yes|    | * |first_paren_new_line__yes|                |
|                         |            |          | * |first_paren_new_line__no|                 |
|                         |            |          | * |ignore_formatting|                        |
+-------------------------+------------+----------+----------------------------------------------+
| |last_paren_new_line|   | |values_1| | |yes|    | * |last_paren_new_line__yes|                 |
|                         |            |          | * |last_paren_new_line__no|                  |
|                         |            |          | * |ignore_formatting|                        |
+-------------------------+------------+----------+----------------------------------------------+
| |open_paren_new_line|   | |values_1| | |yes|    | * |open_paren_new_line__yes|                 |
|                         |            |          | * |open_paren_new_line__no|                  |
|                         |            |          | * |ignore_formatting|                        |
+-------------------------+------------+----------+----------------------------------------------+
| |close_paren_new_line|  | |values_1| | |yes|    | * |close_paren_new_line__yes|                |
|                         |            |          | * |close_paren_new_line__no|                 |
|                         |            |          | * |ignore_formatting|                        |
+-------------------------+------------+----------+----------------------------------------------+
| |new_line_after_comma|  | |values_2| | |yes|    | * |new_line_after_comma__yes|                |
|                         |            |          | * |new_line_after_comma__no|                 |
|                         |            |          | * |new_line_after_comma__ignore_positional|  |
|                         |            |          | * |ignore_formatting|                        |
+-------------------------+------------+----------+----------------------------------------------+
| |assign_on_single_line| | |values_3| | |yes|    | * |assign_on_single_line__yes|               |
|                         |            |          | * |assign_on_single_line__ignore|            |
+-------------------------+------------+----------+----------------------------------------------+
| |ignore_single_line|    | |values_4| | |yes|    | * |ignore_single_line__yes|                  |
|                         |            |          | * |ignore_single_line__no|                   |
+-------------------------+------------+----------+----------------------------------------------+

The options can be combined to format arrays.

This is an example of how to configure these options.

.. code-block:: yaml

   rule :
     constant_016:
        first_paren_new_line : 'yes'
        last_paren_new_line : 'yes'
        open_paren_new_line : 'yes'
        close_paren_new_line : 'yes'
        new_line_after_comma : 'ignore'
        assign_on_single_line : 'yes'
        ignore_single_line : 'no'

The following code snippet is used in the following examples:

.. code-block:: vhdl

   constant c_stimulus : t_stimulus_array := ((name => "Hold in reset", clk_in => "01", rst_in => "11", cnt_en_in => "00", cnt_out => "00"), (name => "Not enabled", clk_in => "01", rst_in => "00", cnt_en_in => "00", cnt_out => "00")); -- Define test vectors

   constant c_stimulus : t_stimulus_array :=
   (
     (
       name =>
               "Hold in reset",
       clk_in => "01",
       rst_in => "11",
       cnt_en_in => "00",
       cnt_out => "00"
     ),
     (
       name =>
               "Not enabled",
       clk_in => "01",
       rst_in => "00",
       cnt_en_in => "00",
       cnt_out => "00"
     )
   ); -- Define test vectors

.. NOTE::  The indenting in the following examples are performed by a different rule.

Example: |first_paren_new_line| set to |yes|
############################################

.. code-block:: vhdl

   constant c_stimulus : t_stimulus_array :=
   ((name => "Hold in reset", clk_in => "01", rst_in => "11", cnt_en_in => "00", cnt_out => "00"), (name => "Not enabled", clk_in => "01", rst_in => "00", cnt_en_in => "00", cnt_out => "00")); -- Define test vectors

   constant c_stimulus : t_stimulus_array :=
   (
     (
       name =>
               "Hold in reset",
       clk_in => "01",
       rst_in => "11",
       cnt_en_in => "00",
       cnt_out => "00"
     ),
     (
       name =>
               "Not enabled",
       clk_in => "01",
       rst_in => "00",
       cnt_en_in => "00",
       cnt_out => "00"
     )
   ); -- Define test vectors

Example: |first_paren_new_line| set to |no|
###########################################

.. code-block:: vhdl

   constant c_stimulus : t_stimulus_array := ((name => "Hold in reset", clk_in => "01", rst_in => "11", cnt_en_in => "00", cnt_out => "00"), (name => "Not enabled", clk_in => "01", rst_in => "00", cnt_en_in => "00", cnt_out => "00")); -- Define test vectors

   constant c_stimulus : t_stimulus_array := (
     (
       name =>
               "Hold in reset",
       clk_in => "01",
       rst_in => "11",
       cnt_en_in => "00",
       cnt_out => "00"
     ),
     (
       name =>
               "Not enabled",
       clk_in => "01",
       rst_in => "00",
       cnt_en_in => "00",
       cnt_out => "00"
     )
   ); -- Define test vectors


Example: |last_paren_new_line| set to |yes|
###########################################

.. code-block:: vhdl

   constant c_stimulus : t_stimulus_array := ((name => "Hold in reset", clk_in => "01", rst_in => "11", cnt_en_in => "00", cnt_out => "00"), (name => "Not enabled", clk_in => "01", rst_in => "00", cnt_en_in => "00", cnt_out => "00")
   ); -- Define test vectors

   constant c_stimulus : t_stimulus_array :=
   (
     (
       name =>
               "Hold in reset",
       clk_in => "01",
       rst_in => "11",
       cnt_en_in => "00",
       cnt_out => "00"
     ),
     (
       name =>
               "Not enabled",
       clk_in => "01",
       rst_in => "00",
       cnt_en_in => "00",
       cnt_out => "00"
     )
   ); -- Define test vectors

Example: |last_paren_new_line| set to |no|
##########################################

.. code-block:: vhdl

   constant c_stimulus : t_stimulus_array := ((name => "Hold in reset", clk_in => "01", rst_in => "11", cnt_en_in => "00", cnt_out => "00"), (name => "Not enabled", clk_in => "01", rst_in => "00", cnt_en_in => "00", cnt_out => "00")); -- Define test vectors

   constant c_stimulus : t_stimulus_array := (
     (
       name =>
               "Hold in reset",
       clk_in => "01",
       rst_in => "11",
       cnt_en_in => "00",
       cnt_out => "00"
     ),
     (
       name =>
               "Not enabled",
       clk_in => "01",
       rst_in => "00",
       cnt_en_in => "00",
       cnt_out => "00"
     )); -- Define test vectors

Example: |open_paren_new_line| set to |yes|
###########################################

.. code-block:: vhdl

   constant c_stimulus : t_stimulus_array := (
     (
      name => "Hold in reset", clk_in => "01", rst_in => "11", cnt_en_in => "00", cnt_out => "00"), (
      name => "Not enabled", clk_in => "01", rst_in => "00", cnt_en_in => "00", cnt_out => "00")); -- Define test vectors

   constant c_stimulus : t_stimulus_array :=
   (
     (
       name =>
               "Hold in reset",
       clk_in => "01",
       rst_in => "11",
       cnt_en_in => "00",
       cnt_out => "00"
     ),
     (
       name =>
               "Not enabled",
       clk_in => "01",
       rst_in => "00",
       cnt_en_in => "00",
       cnt_out => "00"
     )
   ); -- Define test vectors

Example: |open_paren_new_line| set to |no|
##########################################

.. code-block:: vhdl

   constant c_stimulus : t_stimulus_array := ((name => "Hold in reset", clk_in => "01", rst_in => "11", cnt_en_in => "00", cnt_out => "00"), (name => "Not enabled", clk_in => "01", rst_in => "00", cnt_en_in => "00", cnt_out => "00")); -- Define test vectors

   constant c_stimulus : t_stimulus_array := ((name =>
       "Hold in reset",
       clk_in => "01",
       rst_in => "11",
       cnt_en_in => "00",
       cnt_out => "00"
     ),
     (name =>
              "Not enabled",
       clk_in => "01",
       rst_in => "00",
       cnt_en_in => "00",
       cnt_out => "00"
     )); -- Define test vectors

Example: |close_paren_new_line| set to |yes|
############################################

.. code-block:: vhdl

   constant c_stimulus : t_stimulus_array := ((name => "Hold in reset", clk_in => "01", rst_in => "11", cnt_en_in => "00", cnt_out => "00"
     ), (name => "Not enabled", clk_in => "01", rst_in => "00", cnt_en_in => "00", cnt_out => "00"
     )
   ); -- Define test vectors

   constant c_stimulus : t_stimulus_array :=
   (
     (
       name =>
               "Hold in reset",
       clk_in => "01",
       rst_in => "11",
       cnt_en_in => "00",
       cnt_out => "00"
     ),
     (
       name =>
               "Not enabled",
       clk_in => "01",
       rst_in => "00",
       cnt_en_in => "00",
       cnt_out => "00"
     )
   ); -- Define test vectors

Example: |close_paren_new_line| set to |no|
###########################################

.. code-block:: vhdl

   constant c_stimulus : t_stimulus_array := ((name => "Hold in reset", clk_in => "01", rst_in => "11", cnt_en_in => "00", cnt_out => "00"), (name => "Not enabled", clk_in => "01", rst_in => "00", cnt_en_in => "00", cnt_out => "00")); -- Define test vectors

   constant c_stimulus : t_stimulus_array := ((name =>
              "Hold in reset",
       clk_in => "01",
       rst_in => "11",
       cnt_en_in => "00",
       cnt_out => "00"),
     (name =>
              "Not enabled",
       clk_in => "01",
       rst_in => "00",
       cnt_en_in => "00",
       cnt_out => "00")); -- Define test vectors

Example: |new_line_after_comma| set to |yes|
############################################

.. code-block:: vhdl

   constant c_stimulus : t_stimulus_array := ((name => "Hold in reset",
       clk_in => "01",
       rst_in => "11",
       cnt_en_in => "00",
       cnt_out => "00"),
     (name => "Not enabled",
       clk_in => "01",
       rst_in => "00",
       cnt_en_in => "00",
       cnt_out => "00")); -- Define test vectors

   constant c_stimulus : t_stimulus_array :=
   (
     (
       name =>
               "Hold in reset",
       clk_in => "01",
       rst_in => "11",
       cnt_en_in => "00",
       cnt_out => "00"
     ),
     (
       name =>
               "Not enabled",
       clk_in => "01",
       rst_in => "00",
       cnt_en_in => "00",
       cnt_out => "00"
     )
   ); -- Define test vectors

Example: |new_line_after_comma| set to |no|
###########################################

.. code-block:: vhdl

   constant c_stimulus : t_stimulus_array := ((name => "Hold in reset", clk_in => "01", rst_in => "11", cnt_en_in => "00", cnt_out => "00"), (name => "Not enabled", clk_in => "01", rst_in => "00", cnt_en_in => "00", cnt_out => "00")); -- Define test vectors

   constant c_stimulus : t_stimulus_array := ((name =>
              "Hold in reset", clk_in => "01", rst_in => "11", cnt_en_in => "00", cnt_out => "00"), (name =>
              "Not enabled", clk_in => "01", rst_in => "00", cnt_en_in => "00", cnt_out => "00")); -- Define test vectors

Example: |assign_on_single_line| set to |yes|
#############################################

.. code-block:: vhdl

   constant c_stimulus : t_stimulus_array :=
   ((name => "Hold in reset", clk_in => "01", rst_in => "11", cnt_en_in => "00", cnt_out => "00"), (name => "Not enabled", clk_in => "01", rst_in => "00", cnt_en_in => "00", cnt_out => "00")); -- Define test vectors

   constant c_stimulus : t_stimulus_array :=
   (
     (
       name => "Hold in reset",
       clk_in => "01",
       rst_in => "11",
       cnt_en_in => "00",
       cnt_out => "00"
     ),
     (
       name => "Not enabled",
       clk_in => "01",
       rst_in => "00",
       cnt_en_in => "00",
       cnt_out => "00"
     )
   ); -- Define test vectors

Example: Keep all assignments on single line
############################################

Using the following configuration:

.. code-block:: yaml

   rule :
     constant_016:
        first_paren_new_line : 'no'
        last_paren_new_line : 'yes'
        open_paren_new_line : 'yes'
        close_paren_new_line : 'yes'
        new_line_after_comma : 'no'
        assign_on_single_line : 'yes'
        ignore_single_line : 'no'

would result in the following formatting:

.. code-block:: vhdl

   constant c_stimulus : t_stimulus_array := (
     (
       name => "Hold in reset", clk_in => "01", rst_in => "11", cnt_en_in => "00", cnt_out => "00"
     ), (
       name => "Not enabled", clk_in => "01", rst_in => "00", cnt_en_in => "00", cnt_out => "00"
     )
   ); -- Define test vectors

   constant c_stimulus : t_stimulus_array := (
     (
       name => "Hold in reset", clk_in => "01", rst_in => "11", cnt_en_in => "00", cnt_out => "00"
     ), (
       name => "Not enabled", clk_in => "01", rst_in => "00", cnt_en_in => "00", cnt_out => "00"
     )
   ); -- Define test vectors

Example: Fully expand expression
################################

Using the following configuration:

.. code-block:: yaml

   rule :
     constant_016:
        first_paren_new_line : 'yes'
        last_paren_new_line : 'yes'
        open_paren_new_line : 'yes'
        close_paren_new_line : 'yes'
        new_line_after_comma : 'yes'
        assign_on_single_line : 'yes'
        ignore_single_line : 'no'

would result in the following formatting:

.. code-block:: vhdl

   constant c_stimulus : t_stimulus_array :=
   (
     (
       name => "Hold in reset",
       clk_in => "01",
       rst_in => "11",
       cnt_en_in => "00",
       cnt_out => "00"
     ),
     (
       name => "Not enabled",
       clk_in => "01",
       rst_in => "00",
       cnt_en_in => "00",
       cnt_out => "00"
     )
   ); -- Define test vectors

   constant c_stimulus : t_stimulus_array :=
   (
     (
       name => "Hold in reset",
       clk_in => "01",
       rst_in => "11",
       cnt_en_in => "00",
       cnt_out => "00"
     ),
     (
       name => "Not enabled",
       clk_in => "01",
       rst_in => "00",
       cnt_en_in => "00",
       cnt_out => "00"
     )
   ); -- Define test vectors


Rules Enforcing Array Multiline Structure Rules
###############################################

* `concurrent_012 <concurrent_rules.html#concurrent-012>`_
* `constant_016 <constant_rules.html#constant-016>`_
* `sequential_009 <sequential_rules.html#sequential-009>`_
* `signal_403 <signal_rules.html#signal-403>`_
* `variable_403 <variable_rules.html#variable-403>`_
* `variable_assignment_008 <variable_assignment_rules.html#variable-assignment-008>`_
