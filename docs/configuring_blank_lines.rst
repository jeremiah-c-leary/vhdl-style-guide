.. _configuring-blank-lines:

Configuring Blank Lines
-----------------------

There are rules which will check for blank lines either above or below a line.
These rules are designed to improve readability by separating code using blank lines.


There are several options to these rules:

.. |style| replace::
   :code:`style`

.. |no_blank_line| replace::
   :code:`no_blank_line`

.. |require_blank_line| replace::
   :code:`require_blank_line`

.. |require_blank_line_unless_pragma| replace::
   :code:`require_blank_line_unless_pragma`

.. |style__no_blank_line| replace::
   :code:`no_blank_line` = Removes blank lines on the line above or below

.. |style__require_blank_line| replace::
   :code:`require_blank_line` = Requires a blank line on the line above or below

.. |style__require_blank_line_unless_pragma| replace::
   :code:`require_blank_line_unless_pragma` = Requires a blank line on the line above or below unless the line has a pragma

.. |style_values| replace::
   :code:`no_blank_line`, :code:`require_blank_line`, :code:`require_blank_line_unless_pragma`

.. |style_default| replace::
   Rule dependent

+-------------------------+------------------------------------+-----------------+----------------------------------------------+
| Option                  |   Values                           | Default         | Description                                  |
+=========================+====================================+=================+==============================================+
| |style|                 | |no_blank_line|                    | |style_default| | * |style__no_blank_line|                     |
|                         | |require_blank_line|               |                 | * |style__require_blank_line|                |
|                         | |require_blank_line_unless_pragma| |                 | * |style__require_blank_line_unless_pragma|  |
+-------------------------+------------------------------------+-----------------+----------------------------------------------+

This is an example of how to configure the options.

.. code-block:: yaml

   rule :
     architecture_015:
        style : require_blank_line

.. WARNING:: It is important to be aware these rules may conflict with rules that enforce rules on previous lines.
  This can occur when a below rule is applied and then on the next line a previous rule applies.
  Resolve any conflicts by changing the configuration of either rule.

Example: |style| set to |require_blank_line|
############################################

The following code would fail with this option:

.. code-Block:: vhdl

   architecture rtl of fifo is
     -- Comment

   architecture rtl of fifo is
     signal s_sig1 : std_logic;

The following code would pass with this option:

.. code-block:: vhdl

   architecture rtl of fifo is

     -- Comment

   architecture rtl of fifo is

     signal s_sig1 : std_logic;

Example: |style| set to |no_blank_line|
#######################################

The following code would fail with this option:

.. code-Block:: vhdl

   architecture rtl of fifo is

     -- Comment

   architecture rtl of fifo is

     signal s_sig1 : std_logic;

The following code would pass with this option:

.. code-block:: vhdl

   architecture rtl of fifo is
     -- Comment

   architecture rtl of fifo is
     signal s_sig1 : std_logic;

Example: |style| set to |require_blank_line_unless_pragma|
##########################################################

The following code would fail with this option:

.. code-Block:: vhdl

   architecture rtl of fifo is
     -- synthesis translate_off

   architecture rtl of fifo is
     signal s_sig1 : std_logic;

The following code would pass with this option:

.. code-block:: vhdl

   architecture rtl of fifo is
     -- synthesis translate_off

   architecture rtl of fifo is

     signal s_sig1 : std_logic;

Rules Enforcing Blank Lines
###########################

* `architecture_015 <architecture_rules.html#architecture-015>`_
* `architecture_016 <architecture_rules.html#architecture-016>`_
* `architecture_017 <architecture_rules.html#architecture-017>`_
* `architecture_018 <architecture_rules.html#architecture-018>`_
* `architecture_200 <architecture_rules.html#architecture-200>`_
* `block_201 <block_rules.html#block-201>`_
* `block_202 <block_rules.html#block-202>`_
* `block_203 <block_rules.html#block-203>`_
* `block_204 <block_rules.html#block-204>`_
* `block_205 <block_rules.html#block-205>`_
* `case_009 <case_rules.html#case-009>`_
* `case_010 <case_rules.html#case-010>`_
* `case_200 <case_rules.html#case-200>`_
* `case_generate_alternative_200 <case_generate_alternative_rules.html#case-generate-alternative-200>`_
* `case_generate_statement_200 <case_generate_statement_rules.html#case-generate-statement-200>`_
* `component_016 <component_rules.html#component-016>`_
* `component_018 <component_rules.html#component-018>`_
* `constant_200 <constant_rules.html#constant-200>`_
* `context_023 <context_rules.html#context-023>`_
* `context_024 <context_rules.html#context-024>`_
* `context_025 <context_rules.html#context-025>`_
* `entity_016 <entity_rules.html#entity-016>`_
* `entity_200 <entity_rules.html#entity-200>`_
* `entity_202 <entity_rules.html#entity-202>`_
* `entity_203 <entity_rules.html#entity-203>`_
* `generate_003 <generate_rules.html#generate-003>`_
* `generic_map_201 <generic_map_rules.html#generic-map-201>`_
* `if_030 <if_rules.html#if-030>`_
* `instantiation_019 <instantiation_rules.html#instantiation-019>`_
* `loop_statement_201 <loop_statement_rules.html#loop-statement-201>`_
* `loop_statement_203 <loop_statement_rules.html#loop-statement-203>`_
* `package_011 <package_rules.html#package-011>`_
* `package_012 <package_rules.html#package-012>`_
* `package_body_201 <package_body_rules.html#package-body-201>`_
* `package_body_202 <package_body_rules.html#package-body-202>`_
* `package_body_203 <package_body_rules.html#package-body-203>`_
* `package_instantiation_201 <package_instantiation_rules.html#package-instantiation-201>`_
* `port_001 <port_rules.html#port-001>`_
* `port_map_200 <port_map_rules.html#port-map-200>`_
* `port_map_201 <port_map_rules.html#port-map-201>`_
* `pragma_401 <pragma_rules.html#pragma-401>`_
* `pragma_403 <pragma_rules.html#pragma-403>`_
* `process_011 <process_rules.html#process-011>`_
* `process_021 <process_rules.html#process-021>`_
* `process_022 <process_rules.html#process-022>`_
* `process_023 <process_rules.html#process-023>`_
* `process_026 <process_rules.html#process-026>`_
* `process_027 <process_rules.html#process-027>`_
* `record_type_definition_200 <record_type_definition_rules.html#record-type-definition-200>`_
* `signal_200 <signal_rules.html#signal-200>`_
* `subprogram_body_201 <subprogram_body_rules.html#subprogram-body-201>`_
* `subprogram_body_202 <subprogram_body_rules.html#subprogram-body-202>`_
* `subprogram_body_203 <subprogram_body_rules.html#subprogram-body-203>`_
* `subprogram_body_204 <subprogram_body_rules.html#subprogram-body-204>`_
* `subprogram_body_205 <subprogram_body_rules.html#subprogram-body-205>`_
* `subtype_200 <subtype_rules.html#subtype-200>`_
* `subtype_202 <subtype_rules.html#subtype-202>`_
* `type_011 <type_rules.html#type-011>`_
* `type_200 <type_rules.html#type-200>`_
