
.. _configuring-selected-assignment-structure-rules:

Configuring Selected Assignment Structure Rules
-----------------------------------------------

There are rules which will check indent and formatting of selected assignments.
There are separate rules for the structure and indenting of selected assignments.
Both rules are required to ensure proper formatting of multiline constraints.

There are several options to the structure rules:

.. |values| replace::
   :code:`yes`, :code:`no`, :code:`ignore`

.. |values2| replace::
   :code:`yes`, :code:`ignore`

.. |default_yes| replace::
   :code:`yes`

.. |default_no| replace::
   :code:`no`

.. |new_line_yes_description| replace::
   :code:`yes` = Add a new line.

.. |new_line_no_description| replace::
   :code:`no` = Remove new line.

.. |new_line_ignore_description| replace::
   :code:`ignore` = Keep existing formatting.

.. |single_line_yes_description| replace::
   :code:`yes` = Keep code on a single line.

.. |single_line_ignore_description| replace::
   :code:`ignore` = Keep existing formatting.

+----------------------------------------+-----------+---------------+------------------------------------+
| Option                                 | Values    | Default Value | Description                        |
+========================================+===========+===============+====================================+
| :code:`new_line_after_with_keyword`    | |values|  | |default_no|  | * |new_line_yes_description|       |
+----------------------------------------+           +---------------+ * |new_line_no_description|        |
| :code:`new_line_before_select_keyword` |           | |default_no|  | * |new_line_ignore_description|    |
+----------------------------------------+           +---------------+                                    |
| :code:`new_line_after_select_keyword`  |           | |default_yes| |                                    |
+----------------------------------------+           +---------------+                                    |
| :code:`new_line_before_assignment`     |           | |default_no|  |                                    |
+----------------------------------------+           +---------------+                                    |
| :code:`new_line_after_assignment`      |           | |default_no|  |                                    |
+----------------------------------------+           +---------------+                                    |
| :code:`new_line_before_when_keyword`   |           | |default_no|  |                                    |
+----------------------------------------+           +---------------+                                    |
| :code:`new_line_after_when_keyword`    |           | |default_no|  |                                    |
+----------------------------------------+           +---------------+                                    |
| :code:`new_line_before_comma`          |           | |default_no|  |                                    |
+----------------------------------------+           +---------------+                                    |
| :code:`new_line_after_comma`           |           | |default_yes| |                                    |
+----------------------------------------+           +---------------+                                    |
| :code:`new_line_before_semicolon`      |           | |default_no|  |                                    |
+----------------------------------------+-----------+---------------+------------------------------------+
| :code:`single_line_with_expression`    | |values2| | |default_yes| | * |single_line_yes_description|    |
|                                        |           |               | * |single_line_ignore_description| |
+----------------------------------------+-----------+---------------+------------------------------------+

This is an example of how to configure these options.

.. code-block:: yaml

   rule :
     selected_assignment_001:
       new_line_after_with_keyword : 'no'
       new_line_before_select_keyword : 'no'
       new_line_after_select_keyword ; 'yes'
       new_line_before_assignment: 'no'
       new_line_after_assignment; 'no'
       new_line_before_when_keyword : 'no'
       new_line_after_when_keyword ; 'no'
       new_line_before_comma: 'no'
       new_line_after_comma; 'yes'
       new_line_before_semicolon: 'no'
       single_line_with_expression: 'yes'

The following code snippet will be used in the following examples:

.. code-block:: vhdl

   with
     (mux_select
       or reset)
     select
     addr
     <=
     "0000"
     when
     0
     ,
     "1111"
     when
     others
     ;

   with (mux_select or reset) select addr <= "0000" when 0, "1111" when others;

.. NOTE:: In the examples below, indenting is performed by a different rule.

Example: |new_line_after_with_keyword| set to |default_yes|
###########################################################

.. code-block:: vhdl

   with
     (mux_select
       or reset)
     select
     addr
     <=
     "0000"
     when
     0
     ,
     "1111"
     when
     others
     ;

   with
     (mux_select or reset) select addr <= "0000" when 0, "1111" when others;

Example: |new_line_after_with_keyword| set to |default_no|
##########################################################

.. code-block:: vhdl

   with (mux_select
       or reset)
     select
     addr
     <=
     "0000"
     when
     0
     ,
     "1111"
     when
     others
     ;

   with (mux_select or reset) select addr <= "0000" when 0, "1111" when others;

Example: |new_line_before_select_keyword| set to |default_yes|
##############################################################

.. code-block:: vhdl

   with
     (mux_select
       or reset)
     select
     addr
     <=
     "0000"
     when
     0
     ,
     "1111"
     when
     others
     ;

   with (mux_select or reset)
     select addr <= "0000" when 0, "1111" when others;

Example: |new_line_before_select_keyword| set to |default_no|
#############################################################

.. code-block:: vhdl

   with
     (mux_select
       or reset) select
     addr
     <=
     "0000"
     when
     0
     ,
     "1111"
     when
     others
     ;

   with (mux_select or reset) select addr <= "0000" when 0, "1111" when others;

Example: |new_line_after_select_keyword| set to |default_yes|
#############################################################

.. code-block:: vhdl

   with
     (mux_select
       or reset)
     select
     addr
     <=
     "0000"
     when
     0
     ,
     "1111"
     when
     others
     ;

   with (mux_select or reset) select
     addr <= "0000" when 0, "1111" when others;

Example: |new_line_after_select_keyword| set to |default_no|
############################################################

.. code-block:: vhdl

   with
     (mux_select
       or reset)
     select addr
     <=
     "0000"
     when
     0
     ,
     "1111"
     when
     others
     ;

   with (mux_select or reset) select addr <= "0000" when 0, "1111" when others;

Example: |new_line_before_assignment| set to |default_yes|
##########################################################

.. code-block:: vhdl

   with
     (mux_select
       or reset)
     select
     addr
     <=
     "0000"
     when
     0
     ,
     "1111"
     when
     others
     ;

   with (mux_select or reset) select addr
     <= "0000" when 0, "1111" when others;

Example: |new_line_before_assignment| set to |default_no|
#########################################################

.. code-block:: vhdl

   with
     (mux_select
       or reset)
     select
     addr <=
     "0000"
     when
     0
     ,
     "1111"
     when
     others
     ;

   with (mux_select or reset) select addr <= "0000" when 0, "1111" when others;

Example: |new_line_after_assignment| set to |default_yes|
#########################################################

.. code-block:: vhdl

   with
     (mux_select
       or reset)
     select
     addr
     <=
     "0000"
     when
     0
     ,
     "1111"
     when
     others
     ;

   with (mux_select or reset) select addr <=
     "0000" when 0, "1111" when others;

Example: |new_line_after_assignment| set to |default_no|
########################################################

.. code-block:: vhdl

   with
     (mux_select
       or reset)
     select
     addr
     <= "0000"
     when
     0
     ,
     "1111"
     when
     others
     ;

   with (mux_select or reset) select addr <= "0000" when 0, "1111" when others;

Example: |new_line_before_when_keyword| set to |default_yes|
############################################################

.. code-block:: vhdl

   with
     (mux_select
       or reset)
     select
     addr
     <=
     "0000"
     when
     0
     ,
     "1111"
     when
     others
     ;

   with (mux_select or reset) select addr <= "0000"
     when 0, "1111"
     when others;

Example: |new_line_before_when_keyword| set to |default_no|
###########################################################

.. code-block:: vhdl

   with
     (mux_select
       or reset)
     select
     addr
     <=
     "0000" when
     0
     ,
     "1111" when
     others
     ;

   with (mux_select or reset) select addr <= "0000" when 0, "1111" when others;

Example: |new_line_after_when_keyword| set to |default_yes|
###########################################################

.. code-block:: vhdl

   with
     (mux_select
       or reset)
     select
     addr
     <=
     "0000"
     when
     0
     ,
     "1111"
     when
     others
     ;

   with (mux_select or reset) select addr <= "0000" when
     0, "1111" when
     others;

Example: |new_line_after_when_keyword| set to |default_no|
##########################################################

.. code-block:: vhdl

   with
     (mux_select
       or reset)
     select
     addr
     <=
     "0000"
     when 0
     ,
     "1111"
     when others
     ;

   with (mux_select or reset) select addr <= "0000" when 0, "1111" when others;

Example: |new_line_before_comma| set to |default_yes|
#####################################################

.. code-block:: vhdl

   with
     (mux_select
       or reset)
     select
     addr
     <=
     "0000"
     when
     0
     ,
     "1111"
     when
     others
     ;

   with (mux_select or reset) select addr <= "0000" when 0
     , "1111" when others;

Example: |new_line_before_comma| set to |default_no|
####################################################

.. code-block:: vhdl

   with
     (mux_select
       or reset)
     select
     addr
     <=
     "0000"
     when
     0,
     "1111"
     when
     others
     ;

   with (mux_select or reset) select addr <= "0000" when 0, "1111" when others;

Example: |new_line_after_comma| set to |default_yes|
####################################################

.. code-block:: vhdl

   with
     (mux_select
       or reset)
     select
     addr
     <=
     "0000"
     when
     0
     ,
     "1111"
     when
     others
     ;

   with (mux_select or reset) select addr <= "0000" when 0,
     "1111" when others;

Example: |new_line_after_comma| set to |default_no|
###################################################

.. code-block:: vhdl

   with
     (mux_select
       or reset)
     select
     addr
     <=
     "0000"
     when
     0
     , "1111"
     when
     others
     ;

   with (mux_select or reset) select addr <= "0000" when 0, "1111" when others;

Example: |new_line_before_semicolon| set to |default_yes|
#########################################################

.. code-block:: vhdl

   with
     (mux_select
       or reset)
     select
     addr
     <=
     "0000"
     when
     0
     ,
     "1111"
     when
     others
     ;

   with (mux_select or reset) select addr <= "0000" when 0, "1111" when others
     ;

Example: |new_line_before_semicolon| set to |default_yes|
#########################################################

.. code-block:: vhdl

   with
     (mux_select
       or reset)
     select
     addr
     <=
     "0000"
     when
     0
     ,
     "1111"
     when
     others
     ;

   with (mux_select or reset) select addr <= "0000" when 0, "1111" when others;

Example: |single_line_with_expression| set to |default_yes|
###########################################################

.. code-block:: vhdl

   with
     (mux_select or reset)
     select
     addr
     <=
     "0000"
     when
     0
     ,
     "1111"
     when
     others
     ;

   with (mux_select or reset) select addr <= "0000" when 0, "1111" when others;

Example: Default Values
#######################

The following configuration are the default values for the rule selected_assignment_001.

.. code-block:: yaml

   rule :
     selected_assignment_001:
       new_line_after_with_keyword : 'no'
       new_line_before_select_keyword : 'no'
       new_line_after_select_keyword ; 'yes'
       new_line_before_assignment: 'no'
       new_line_after_assignment; 'no'
       new_line_before_when_keyword : 'no'
       new_line_after_when_keyword ; 'no'
       new_line_before_comma: 'no'
       new_line_after_comma; 'yes'
       new_line_before_semicolon: 'no'
       single_line_with_expression: 'yes'

The above configuration when applied to the code snippet will result in the following format:

.. code-block:: vhdl

   with (mux_select or reset) select
     addr <= "0000" when 0,
             "1111" when others;

   with (mux_select or reset) select
     addr <= "0000" when 0,
             "1111" when others;

Rules Enforcing Selected Assignment Structure Rules
###################################################

* `selected_assignment_001 <selected_assingment_rules.html#selected-assignment-001>`_
