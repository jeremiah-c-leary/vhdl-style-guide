.. _configuring-whitespace-rules:

Configuring Whitespace Rules
----------------------------

There are rules which will check for a whitespace between keywords or keywords and identifiers.
The number of spaces can be configured to allow for multiple or no whitespaces.

There are a couple of options to these rules:

+--------------------------+----------------------------------------------------------+
| Option                   | Description                                              |
+==========================+==========================================================+
| number_of_spaces         | Determines the number of whitespace characters to allow. |
+--------------------------+----------------------------------------------------------+

The :code:`number_of_spaces` option can accept several values:

+-----------------------+----------------------------------------------------------+
| Value                 | Description                                              |
+=======================+==========================================================+
| [0-9][0-9]*           | The number of spaces to enforce.                         |
+-----------------------+----------------------------------------------------------+
| >[0-9][0-9]*          | The minimum number of spaces to enforce.                 |
+-----------------------+----------------------------------------------------------+
| >=[0-9][0-9]*         | The minimum number of spaces to enforce.                 |
+-----------------------+----------------------------------------------------------+
| [0-9][0-9]*+          | The minimum number of spaces to enforce.                 |
+-----------------------+----------------------------------------------------------+
| <[0-9][0-9]*          | The maximum number of spaces to enforce.                 |
+-----------------------+----------------------------------------------------------+
| <=[0-9][0-9]*         | The maximum number of spaces to enforce.                 |
+-----------------------+----------------------------------------------------------+

These options combined with the values allow complete control over the number of whitespaces allowed.

Example:  enforce one whitespace between end and architecture
##############################################################

.. code-block:: yaml

   rule :
     architecture_012:
        number_of_spaces: 1

In this example, the number of whitespaces between the keywords must be 1.

.. code-Block:: vhdl

   end architecture;

Example:  enforce two whitespaces between end and architecture
##############################################################

.. code-block:: yaml

   rule :
     architecture_012:
        number_of_spaces: 2

In this example, the number of whitespaces between the keywords must be 2.

.. code-Block:: vhdl

   end  architecture;


Example:  allow at least 1 space before a colon
###############################################

.. code-block:: yaml

   rule :
     signal_006:
        number_of_spaces: '>=1'

In this example, there must be at least a single whitespace before the colon.
All of these would not be a violation.

.. code-Block:: vhdl

   signal wr_en : std_logic;
   signal wr_en  : std_logic;
   signal wr_en                : std_logic;

The same result could be achieved using this yaml:

.. code-block:: yaml

   rule :
     signal_006:
        number_of_spaces: '1+'

Example:  allow at most 4 spaces before colon
#############################################
.. code-block:: yaml

   rule :
     signal_006:
        number_of_spaces: '<=4'

In this example, there must be at most four whitespaces before the colon.
The third signal declaration would be a violation.

.. code-Block:: vhdl

   signal wr_en : std_logic;
   signal wr_en  : std_logic;
   signal wr_en                : std_logic;


Rules Enforcing Whitespace
##########################

* `alias_declaration_100 <alias_declaration_rules.html#alias-declaration-100>`_
* `alias_declaration_101 <alias_declaration_rules.html#alias-declaration-101>`_
* `alias_declaration_102 <alias_declaration_rules.html#alias-declaration-102>`_
* `alias_declaration_103 <alias_declaration_rules.html#alias-declaration-103>`_
* `architecture_012 <architecture_rules.html#architecture-012>`_
* `architecture_022 <architecture_rules.html#architecture-022>`_
* `architecture_030 <architecture_rules.html#architecture-030>`_
* `architecture_031 <architecture_rules.html#architecture-031>`_
* `architecture_032 <architecture_rules.html#architecture-032>`_
* `architecture_033 <architecture_rules.html#architecture-033>`_
* `assert_100 <assert_rules.html#assert-100>`_
* `assert_101 <assert_rules.html#assert-101>`_
* `assert_102 <assert_rules.html#assert-102>`_
* `attribute_declaration_100 <attribute_declaration_rules.html#attribute-declaration-100>`_
* `attribute_declaration_101 <attribute_declaration_rules.html#attribute-declaration-101>`_
* `attribute_specification_100 <attribute_specification_rules.html#attribute-specification-100>`_
* `attribute_specification_101 <attribute_specification_rules.html#attribute-specification-101>`_
* `block_100 <block_rules.html#block-100>`_
* `block_101 <block_rules.html#block-101>`_
* `case_002 <case_rules.html#case-002>`_
* `case_003 <case_rules.html#case-003>`_
* `case_004 <case_rules.html#case-004>`_
* `case_005 <case_rules.html#case-005>`_
* `case_006 <case_rules.html#case-006>`_
* `case_generate_alternative_100 <case_generate_alternative_rules.html#case-generate-alternative-100>`_
* `case_generate_alternative_101 <case_generate_alternative_rules.html#case-generate-alternative-101>`_
* `case_generate_statement_100 <case_generate_statement_rules.html#case-generate-statement-100>`_
* `case_generate_statement_101 <case_generate_statement_rules.html#case-generate-statement-101>`_
* `comment_004 <comment_rules.html#comment-004>`_
* `component_002 <component_rules.html#component-002>`_
* `component_007 <component_rules.html#component-007>`_
* `component_011 <component_rules.html#component-011>`_
* `component_013 <component_rules.html#component-013>`_
* `concurrent_002 <concurrent_rules.html#concurrent-002>`_
* `concurrent_004 <concurrent_rules.html#concurrent-004>`_
* `conditional_expressions_100 <conditional_expressions_rules.html#conditional-expressions-100>`_
* `conditional_expressions_101 <conditional_expressions_rules.html#conditional-expressions-101>`_
* `conditional_expressions_102 <conditional_expressions_rules.html#conditional-expressions-102>`_
* `conditional_expressions_103 <conditional_expressions_rules.html#conditional-expressions-103>`_
* `conditional_waveforms_100 <conditional_waveforms_rules.html#conditional-waveforms-100>`_
* `conditional_waveforms_101 <conditional_waveforms_rules.html#conditional-waveforms-101>`_
* `conditional_waveforms_102 <conditional_waveforms_rules.html#conditional-waveforms-102>`_
* `conditional_waveforms_103 <conditional_waveforms_rules.html#conditional-waveforms-103>`_
* `constant_005 <constant_rules.html#constant-005>`_
* `constant_006 <constant_rules.html#constant-006>`_
* `constant_010 <constant_rules.html#constant-010>`_
* `constant_100 <constant_rules.html#constant-100>`_
* `constant_101 <constant_rules.html#constant-101>`_
* `context_002 <context_rules.html#context-002>`_
* `context_017 <context_rules.html#context-017>`_
* `context_018 <context_rules.html#context-018>`_
* `context_019 <context_rules.html#context-019>`_
* `context_ref_002 <context_ref.html#context-ref-002>`_
* `element_association_100 <element_association_rules.html#element-association-100>`_
* `element_association_101 <element_association_rules.html#element-association-101>`_
* `entity_002 <entity_rules.html#entity-002>`_
* `entity_007 <entity_rules.html#entity-007>`_
* `entity_011 <entity_rules.html#entity-011>`_
* `entity_013 <entity_rules.html#entity-013>`_
* `entity_specification_100 <entity_specification_rules.html#entity-specification-100>`_
* `entity_specification_101 <entity_specification_rules.html#entity-specification-101>`_
* `external_constant_name_100 <external_constant_name_rules.html#external-constant-name-100>`_
* `external_constant_name_101 <external_constant_name_rules.html#external-constant-name-101>`_
* `external_constant_name_102 <external_constant_name_rules.html#external-constant-name-102>`_
* `external_constant_name_103 <external_constant_name_rules.html#external-constant-name-103>`_
* `external_constant_name_104 <external_constant_name_rules.html#external-constant-name-104>`_
* `external_signal_name_100 <external_signal_name_rules.html#external-signal-name-100>`_
* `external_signal_name_101 <external_signal_name_rules.html#external-signal-name-101>`_
* `external_signal_name_102 <external_signal_name_rules.html#external-signal-name-102>`_
* `external_signal_name_103 <external_signal_name_rules.html#external-signal-name-103>`_
* `external_signal_name_104 <external_signal_name_rules.html#external-signal-name-104>`_
* `external_variable_name_100 <external_variable_name_rules.html#external-variable-name-100>`_
* `external_variable_name_101 <external_variable_name_rules.html#external-variable-name-101>`_
* `external_variable_name_102 <external_variable_name_rules.html#external-variable-name-102>`_
* `external_variable_name_103 <external_variable_name_rules.html#external-variable-name-103>`_
* `external_variable_name_104 <external_variable_name_rules.html#external-variable-name-104>`_
* `file_100 <file_rules.html#file-100>`_
* `function_100 <function_rules.html#function-100>`_
* `function_101 <function_rules.html#function-101>`_
* `generate_002 <generate_rules.html#generate-002>`_
* `generate_008 <generate_rules.html#generate-008>`_
* `generate_013 <generate_rules.html#generate-013>`_
* `generate_014 <generate_rules.html#generate-014>`_
* `generic_003 <generic_rules.html#generic-003>`_
* `generic_005 <generic_rules.html#generic-005>`_
* `generic_006 <generic_rules.html#generic-006>`_
* `generic_014 <generic_rules.html#generic-014>`_
* `generic_map_006 <generic_map_rules.html#generic-map-006>`_
* `generic_map_007 <generic_map_rules.html#generic-map-007>`_
* `generic_map_100 <generic_map_rules.html#generic-map-100>`_
* `generic_map_101 <generic_map_rules.html#generic-map-101>`_
* `if_003 <if_rules.html#if-003>`_
* `if_004 <if_rules.html#if-004>`_
* `if_005 <if_rules.html#if-005>`_
* `if_015 <if_rules.html#if-015>`_
* `instantiation_002 <instantiation_rules.html#instantiation-002>`_
* `instantiation_003 <instantiation_rules.html#instantiation-003>`_
* `instantiation_032 <instantiation_rules.html#instantiation-032>`_
* `iteration_scheme_100 <iteration_scheme_rules.html#iteration-scheme-100>`_
* `iteration_scheme_101 <iteration_scheme_rules.html#iteration-scheme-101>`_
* `library_002 <library_rules.html#library-002>`_
* `library_006 <library_rules.html#library-006>`_
* `loop_statement_100 <loop_statement_rules.html#loop-statement-100>`_
* `loop_statement_101 <loop_statement_rules.html#loop-statement-101>`_
* `loop_statement_102 <loop_statement_rules.html#loop-statement-102>`_
* `loop_statement_103 <loop_statement_rules.html#loop-statement-103>`_
* `loop_statement_104 <loop_statement_rules.html#loop-statement-104>`_
* `package_002 <package_rules.html#package-002>`_
* `package_009 <package_rules.html#package-009>`_
* `package_body_100 <package_body_rules.html#package-body-100>`_
* `package_body_101 <package_body_rules.html#package-body-101>`_
* `package_instantiation_100 <package_instantiation_rules.html#package-instantiation-100>`_
* `package_instantiation_101 <package_instantiation_rules.html#package-instantiation-101>`_
* `package_instantiation_102 <package_instantiation_rules.html#package-instantiation-102>`_
* `package_instantiation_103 <package_instantiation_rules.html#package-instantiation-103>`_
* `port_003 <port_rules.html#port-003>`_
* `port_020 <port_rules.html#port-020>`_
* `port_100 <port_rules.html#port-100>`_
* `port_101 <port_rules.html#port-101>`_
* `port_map_006 <port_map_rules.html#port-map-006>`_
* `port_map_007 <port_map_rules.html#port-map-007>`_
* `port_map_100 <port_map_rules.html#port-map-100>`_
* `port_map_101 <port_map_rules.html#port-map-101>`_
* `procedure_100 <procedure_rules.html#procedure-100>`_
* `procedure_101 <procedure_rules.html#procedure-101>`_
* `procedure_call_100 <procedure_call_rules.html#procedure-call-100>`_
* `procedure_call_101 <procedure_call_rules.html#procedure-call-101>`_
* `process_002 <process_rules.html#process-002>`_
* `process_007 <process_rules.html#process-007>`_
* `process_014 <process_rules.html#process-014>`_
* `process_024 <process_rules.html#process-024>`_
* `process_025 <process_rules.html#process-025>`_
* `record_type_definition_100 <record_type_definition_rules.html#record-type-definition-100>`_
* `record_type_definition_101 <record_type_definition_rules.html#record-type-definition-101>`_
* `report_statement_100 <report_statement_rules.html#report-statement-100>`_
* `report_statement_101 <report_statement_rules.html#report-statement-101>`_
* `selected_assignment_100 <selected_assignment_rules.html#selected-assignment-100>`_
* `selected_assignment_101 <selected_assignment_rules.html#selected-assignment-101>`_
* `selected_assignment_102 <selected_assignment_rules.html#selected-assignment-102>`_
* `selected_assignment_103 <selected_assignment_rules.html#selected-assignment-103>`_
* `selected_assignment_104 <selected_assignment_rules.html#selected-assignment-104>`_
* `selected_assignment_105 <selected_assignment_rules.html#selected-assignment-105>`_
* `selected_assignment_106 <selected_assignment_rules.html#selected-assignment-106>`_
* `selected_assignment_107 <selected_assignment_rules.html#selected-assignment-107>`_
* `sequential_002 <sequential_rules.html#sequential-002>`_
* `sequential_003 <sequential_rules.html#sequential-003>`_
* `signal_005 <signal_rules.html#signal-005>`_
* `signal_006 <signal_rules.html#signal-006>`_
* `signal_100 <signal_rules.html#signal-100>`_
* `signal_101 <signal_rules.html#signal-101>`_
* `signal_102 <signal_rules.html#signal-102>`_
* `subprogram_instantiation_100 <subprogram_instantiation_rules.html#subprogram-instantiation-100>`_
* `subprogram_instantiation_101 <subprogram_instantiation_rules.html#subprogram-instantiation-101>`_
* `subprogram_instantiation_102 <subprogram_instantiation_rules.html#subprogram-instantiation-102>`_
* `subprogram_instantiation_103 <subprogram_instantiation_rules.html#subprogram-instantiation-103>`_
* `subprogram_instantiation_104 <subprogram_instantiation_rules.html#subprogram-instantiation-104>`_
* `subtype_100 <subtype_rules.html#subtype-100>`_
* `subtype_101 <subtype_rules.html#subtype-101>`_
* `subtype_102 <subtype_rules.html#subtype-102>`_
* `type_006 <type_rules.html#type-006>`_
* `type_007 <type_rules.html#type-007>`_
* `type_100 <type_rules.html#type-100>`_
* `variable_005 <variable_rules.html#variable-005>`_
* `variable_006 <variable_rules.html#variable-006>`_
* `variable_100 <variable_rules.html#variable-100>`_
* `variable_101 <variable_rules.html#variable-101>`_
* `variable_102 <variable_rules.html#variable-102>`_
* `variable_103 <variable_rules.html#variable-103>`_
* `variable_assignment_002 <variable_assignment_rules.html#variable-assignment-002>`_
* `variable_assignment_003 <variable_assignment_rules.html#variable-assignment-003>`_
* `whitespace_007 <whitespace_rules.html#whitespace-007>`_
