
.. _configuring-uppercase-and-lowercase-rules:

Configuring Uppercase and Lowercase Rules
-----------------------------------------

There are several rules that enforce upper_or_lower, uppercase or lowercase.

There are several options to these rules:

.. |case_option| replace::
   :code:`case`

.. |upper_value| replace::
   :code:`upper`

.. |lower_value| replace::
   :code:`lower`

.. |upper_or_lower_value| replace::
   :code:`upper_or_lower`

.. |camelCase_value| replace::
   :code:`camelCase`

.. |relaxedCamelCase_value| replace::
   :code:`relaxedCamelCase`

.. |PascalCase_value| replace::
   :code:`PascalCase`

.. |RelaxedPascalCase_value| replace::
   :code:`RelaxedPascalCase`

.. |PascalSnakeCase_value| replace::
   :code:`Pascal_Snake_Case`

.. |regex_value| replace::
   :code:`regex`

.. |case_option__upper| replace::
   |upper_value| = Enforce upper case

.. |case_option__lower| replace::
   |lower_value| = Enforce lower case

.. |case_option__upper_or_lower| replace::
   |upper_or_lower_value| = Allow upper or lower case

.. |case_option__camelCase| replace::
   |camelCase_value| = Enforce camelCase with two allowed uppercase characters in a row

.. |case_option__relaxedCamelCase| replace::
   |relaxedCamelCase_value| = Enforce camelCase with any number of uppercase characters in a row

.. |case_option__PascalCase| replace::
   |PascalCase_value| = Enforce PascalCase with two allowed uppercase characters in a row

.. |case_option__RelaxedPascalCase| replace::
   |RelaxedPascalCase_value| = Enforce PascalCase with any number of uppercase characters in a row

.. |case_option__PascalSnakeCase| replace::
   |PascalSnakeCase_value| = Enforce Pascal_Snake_Case

.. |case_option__regex| replace::
   |regex_value| = Enforce user defined regex

.. |case_values| replace::
   |upper_value|, |lower_value|, |upper_or_lower_value|, |camelCase_value|, |relaxedCamelCase_value|, |PascalCase_value|, |RelaxedPascalCase_value|, |regex_value|

.. |case_default_value| replace::
   |lower_value|

.. |prefix_exceptions_option| replace::
   :code:`prefix_exceptions`

.. |pe_values| replace::
   List of strings

.. |pe_default_value| replace::
   Empty list

.. |pe_description| replace::
   Enforce exception case on prefix if encountered.

.. |suffix_exceptions_option| replace::
   :code:`suffix_exceptions`

.. |se_values| replace::
   List of strings

.. |se_default_value| replace::
   Empty list

.. |se_description| replace::
   Enforce exception case on suffix if encountered.

.. |case_exceptions_option| replace::
   :code:`case_exceptions`

.. |ce_values| replace::
   List of strings

.. |regex_values| replace::
   String

.. |ce_default_value| replace::
   Empty list

.. |regex_default_value| replace::
   Empty String

.. |ce_description| replace::
   Enforce case for items in the list.

.. |regex_option| replace::
   :code:`regex`

.. |regex_description| replace::
   Enforce case based on regex string

+----------------------------+---------------------------+-----------------------+------------------------------------+
| Option                     | Values                    | Default Value         | Description                        |
+============================+===========================+=======================+====================================+
| |case_option|              | |upper_value|             | |case_default_value|  | * |case_option__upper|             |
|                            | |lower_value|             |                       | * |case_option__lower|             |
|                            | |upper_or_lower_value|    |                       | * |case_option__upper_or_lower|    |
|                            | |camelCase_value|         |                       | * |case_option__camelCase|         |
|                            | |relaxedCamelCase_value|  |                       | * |case_option__relaxedCamelCase|  |
|                            | |PascalCase_value|        |                       | * |case_option__PascalCase|        |
|                            | |RelaxedPascalCase_value| |                       | * |case_option__RelaxedPascalCase| |
|                            | |PascalSnakeCase_value|   |                       | * |case_option__PascalSnakeCase|   |
|                            | |regex_value|             |                       | * |case_option__regex|             |
+----------------------------+---------------------------+-----------------------+------------------------------------+
| |prefix_exceptions_option| | |pe_values|               | |pe_default_value|    | |pe_description|                   |
+----------------------------+---------------------------+-----------------------+------------------------------------+
| |suffix_exceptions_option| | |se_values|               | |se_default_value|    | |se_description|                   |
+----------------------------+---------------------------+-----------------------+------------------------------------+
| |case_exceptions_option|   | |ce_values|               | |ce_default_value|    | |ce_description|                   |
+----------------------------+---------------------------+-----------------------+------------------------------------+
| |regex_option|             | |regex_values|            | |regex_default_value| | |regex_description|                |
+----------------------------+---------------------------+-----------------------+------------------------------------+

This is an example of how to configure these options.

.. code-block:: yaml

   rule :
     architecture_004:
        case: 'lower'
        prefix_exceptions:
          - 'G_'
        suffix_exceptions:
          - '_G'
        case_exceptions:
          - 'IEEE'
        regex: ''

The following code snippet is used in the following examples:

.. code-block:: vhdl

   constant c_DATA_width : positive := 32;
   constant addr_WIDTH_c : positive := 8;

.. NOTE:: The following examples use rule `constant_004`.

Example: |case_option| set to |lower_value|
###########################################

.. code-block:: vhdl

   constant c_data_width : positive := 32;
   constant addr_width_c : positive := 8;

Example: |case_option| set to |upper_value|
###########################################

.. code-block:: vhdl

   constant C_DATA_WIDTH : positive := 32;
   constant ADDR_WIDTH_C : positive := 8;

Example: |case_option| set to |upper_or_lower_value|
####################################################

This option will not perform any updates to the code as the case could be either upper or lower.

.. code-block:: vhdl

   constant c_DATA_width : positive := 32;
   constant addr_WIDTH_c : positive := 8;

Example: |case_option| set to |upper_value| and |prefix_exceptions_option| set to :code:`c_`
############################################################################################

.. code-block:: vhdl

   constant c_DATA_WIDTH : positive := 32;
   constant ADDR_WIDTH_C : positive := 8;

Example: |case_option| set to |upper_value| and |suffix_exceptions_option| set to :code:`_c`
############################################################################################

.. code-block:: vhdl

   constant C_DATA_WIDTH : positive := 32;
   constant ADDR_WIDTH_c : positive := 8;

Example: |case_option| set to |upper_value| and |case_exceptions_option| set to :code:`addr_WIDTH_c`
####################################################################################################

.. code-block:: vhdl

   constant C_DATA_WIDTH : positive := 32;
   constant addr_WIDTH_c : positive := 8;

Example: |case_option| set to |regex_value| and |regex_option| set to :code:`[A-Z][A-Za-z\d]*`
##############################################################################################

The following constant identifiers would pass with the defined regular expression.

.. code-block:: vhdl

   constant SPIAccess : std_logic;
   constant ADCRegisters : std_logic;

Example: Changing Multiple Case Rules
#####################################

If there are a lot of case rules you want to change, you can use the global option to reduce the size of the configuration.
For example, if you want to uppercase everything except the entity name, you could write the following configuration:

.. code-block:: yaml

   rule :
     global :
       case : 'upper'
     entity_008 :
       case : 'lower'

Rules Enforcing Case
####################

* `after_500 <after_rules.html#after-500>`_

* `alias_declaration_500 <alias_declaration_rules.html#alias-declaration-500>`_
* `alias_declaration_501 <alias_declaration_rules.html#alias-declaration-501>`_
* `alias_declaration_502 <alias_declaration_rules.html#alias-declaration-502>`_

* `architecture_004 <architecture_rules.html#architecture-004>`_
* `architecture_009 <architecture_rules.html#architecture-009>`_
* `architecture_011 <architecture_rules.html#architecture-011>`_
* `architecture_013 <architecture_rules.html#architecture-013>`_
* `architecture_014 <architecture_rules.html#architecture-014>`_
* `architecture_019 <architecture_rules.html#architecture-019>`_
* `architecture_020 <architecture_rules.html#architecture-020>`_
* `architecture_021 <architecture_rules.html#architecture-021>`_
* `architecture_028 <architecture_rules.html#architecture-028>`_

* `array_constraint_500 <../array_constraint_rules.html#array-constraint-500>`_

* `assert_500 <assert_rules.html#assert-500>`_
* `assert_501 <assert_rules.html#assert-501>`_
* `assert_502 <assert_rules.html#assert-502>`_

* `attribute_500 <attribute_rules.html#attribute-500>`_

* `attribute_declaration_500 <attribute_declaration_rules.html#attribute-declaration-500>`_
* `attribute_declaration_501 <attribute_declaration_rules.html#attribute-declaration-501>`_
* `attribute_declaration_502 <attribute_declaration_rules.html#attribute-declaration-502>`_

* `attribute_specification_500 <attribute_specification_rules.html#attribute-specification-500>`_
* `attribute_specification_501 <attribute_specification_rules.html#attribute-specification-501>`_
* `attribute_specification_502 <attribute_specification_rules.html#attribute-specification-502>`_
* `attribute_specification_503 <attribute_specification_rules.html#attribute-specification-503>`_

* `bit_string_literal_500 <bit_string_literal_rules.html#bit-string-literal-500>`_
* `bit_string_literal_501 <bit_string_literal_rules.html#bit-string-literal-501>`_

* `block_500 <block_rules.html#block-500>`_
* `block_501 <block_rules.html#block-501>`_
* `block_502 <block_rules.html#block-502>`_
* `block_503 <block_rules.html#block-503>`_
* `block_504 <block_rules.html#block-504>`_
* `block_505 <block_rules.html#block-505>`_
* `block_506 <block_rules.html#block-506>`_

* `case_014 <case_rules.html#case-014>`_
* `case_015 <case_rules.html#case-015>`_
* `case_016 <case_rules.html#case-016>`_
* `case_017 <case_rules.html#case-017>`_
* `case_018 <case_rules.html#case-018>`_

* `case_generate_alternative_500 <case_generate_alternative_rules.html#case-generate-alternative-500>`_

* `case_generate_statement_500 <case_generate_statement_rules.html#case-generate-statement-500>`_
* `case_generate_statement_501 <case_generate_statement_rules.html#case-generate-statement-501>`_

* `choice_500 <choice_rules.html#choice-500>`_

* `component_004 <component_rules.html#component-004>`_
* `component_006 <component_rules.html#component-006>`_
* `component_008 <component_rules.html#component-008>`_
* `component_010 <component_rules.html#component-010>`_
* `component_012 <component_rules.html#component-012>`_
* `component_014 <component_rules.html#component-014>`_

* `conditional_expressions_500 <conditional_expressions_rules.html#conditional-expressions-500>`_
* `conditional_expressions_501 <conditional_expressions_rules.html#conditional-expressions-501>`_

* `conditional_waveforms_500 <conditional_waveforms_rules.html#conditional-waveforms-500>`_
* `conditional_waveforms_501 <conditional_waveforms_rules.html#conditional-waveforms-501>`_

* `constant_002 <constant_rules.html#constant-002>`_
* `constant_004 <constant_rules.html#constant-004>`_

* `constrained_array_definition_500 <constrained_array_definition_rules.html#constrained-array-definition-500>`_
* `constrained_array_definition_501 <constrained_array_definition_rules.html#constrained-array-definition-501>`_

* `context_004 <context_rules.html#context-004>`_
* `context_012 <context_rules.html#context-012>`_
* `context_013 <context_rules.html#context-013>`_
* `context_014 <context_rules.html#context-014>`_
* `context_015 <context_rules.html#context-015>`_
* `context_016 <context_rules.html#context-016>`_

* `context_ref_003 <context_ref_rules.html#context-ref-003>`_
* `context_ref_500 <context_ref_rules.html#context-ref-500>`_
* `context_ref_501 <context_ref_rules.html#context-ref-501>`_

* `delay_mechanism_500 <delay_mechanism_rules.html#delay-mechanism-500>`_
* `delay_mechanism_501 <delay_mechanism_rules.html#delay-mechanism-501>`_
* `delay_mechanism_502 <delay_mechanism_rules.html#delay-mechanism-502>`_

* `entity_004 <entity_rules.html#entity-004>`_
* `entity_006 <entity_rules.html#entity-006>`_
* `entity_008 <entity_rules.html#entity-008>`_
* `entity_010 <entity_rules.html#entity-010>`_
* `entity_012 <entity_rules.html#entity-012>`_
* `entity_014 <entity_rules.html#entity-014>`_
* `entity_500 <entity_rules.html#entity-500>`_

* `entity_specification_500 <entity_specification_rules.html#entity-specification-500>`_
* `entity_specification_501 <entity_specification_rules.html#entity-specification-501>`_
* `entity_specification_503 <entity_specification_rules.html#entity-specification-503>`_

* `exit_statement_500 <exit_statement_rules.html#exit-statement-500>`_
* `exit_statement_501 <exit_statement_rules.html#exit-statement-501>`_

* `exponent_500 <exponent_rules.html#exponent-500>`_

* `external_constant_name_500 <external_constant_name_rules.html#external-constant-name-500>`_

* `external_signal_name_500 <external_signal_name_rules.html#external-signal-name-500>`_

* `external_variable_name_500 <external_variable_name_rules.html#external-variable-name-500>`_

* `file_open_information_500 <file_open_information_rules.html#file-open-information-500>`_
* `file_open_information_501 <file_open_information_rules.html#file-open-information-501>`_
* `file_open_information_502 <file_open_information_rules.html#file-open-information-502>`_

* `file_002 <file_rules.html#file-002>`_
* `file_500 <file_rules.html#file-500>`_

* `file_type_definition_500 <file_type_definition_rules.html#file-type-definition-500>`_
* `file_type_definition_501 <file_type_definition_rules.html#file-type-definition-501>`_

* `for_generate_statement_500 <for_generate_statement_rules.html#for-generate-statement-500>`_
* `for_generate_statement_501 <for_generate_statement_rules.html#for-generate-statement-501>`_

* `function_004 <function_rules.html#function-004>`_
* `function_005 <function_rules.html#function-005>`_
* `function_013 <function_rules.html#function-013>`_
* `function_017 <function_rules.html#function-017>`_
* `function_501 <function_rules.html#function-501>`_
* `function_502 <function_rules.html#function-502>`_
* `function_506 <function_rules.html#function-506>`_
* `function_507 <function_rules.html#function-507>`_
* `function_509 <function_rules.html#function-509>`_
* `function_510 <function_rules.html#function-510>`_
* `function_511 <function_rules.html#function-511>`_
* `function_512 <function_rules.html#function-512>`_

* `generate_005 <generate_rules.html#generate-005>`_
* `generate_009 <generate_rules.html#generate-009>`_
* `generate_010 <generate_rules.html#generate-010>`_
* `generate_012 <generate_rules.html#generate-012>`_
* `generate_500 <generate_rules.html#generate-500>`_
* `generate_501 <generate_rules.html#generate-501>`_

* `generic_007 <generic_rules.html#generic-007>`_
* `generic_009 <generic_rules.html#generic-009>`_

* `generic_map_001 <generic_map_rules.html#generic-map-001>`_
* `generic_map_002 <generic_map_rules.html#generic-map-002>`_

* `if_generate_statement_500 <if_generate_statement_rules.html#if-generate-statement-500>`_
* `if_generate_statement_501 <if_generate_statement_rules.html#if-generate-statement-501>`_
* `if_generate_statement_502 <if_generate_statement_rules.html#if-generate-statement-502>`_
* `if_generate_statement_503 <if_generate_statement_rules.html#if-generate-statement-503>`_

* `if_025 <if_rules.html#if-025>`_
* `if_026 <if_rules.html#if-026>`_
* `if_027 <if_rules.html#if-027>`_
* `if_028 <if_rules.html#if-028>`_
* `if_029 <if_rules.html#if-029>`_
* `if_034 <if_rules.html#if-034>`_

* `index_subtype_definition_500 <index_subtype_definition_rules.html#index-subtype-definition-500>`_

* `instantiation_008 <instantiation_rules.html#instantiation-008>`_
* `instantiation_009 <instantiation_rules.html#instantiation-009>`_
* `instantiation_027 <instantiation_rules.html#instantiation-027>`_
* `instantiation_028 <instantiation_rules.html#instantiation-028>`_
* `instantiation_031 <instantiation_rules.html#instantiation-031>`_
* `instantiation_500 <instantiation_rules.html#instantiation-500>`_

* `interface_incomplete_type_declaration_500 <../interface_incomplete_type_declaration_rules.html#interface-incomplete-type-declaration-500>`_
* `interface_incomplete_type_declaration_501 <../interface_incomplete_type_declaration_rules.html#interface-incomplete-type-declaration-501>`_

* `iteration_scheme_500 <iteration_scheme_rules.html#iteration-scheme-500>`_
* `iteration_scheme_501 <iteration_scheme_rules.html#iteration-scheme-501>`_

* `library_004 <library_rules.html#library-004>`_
* `library_005 <library_rules.html#library-005>`_
* `library_500 <library_rules.html#library-500>`_

* `logical_operator_500 <logical_operator_rules.html#logical-operator-500>`_

* `loop_statement_500 <loop_statement_rules.html#loop-statement-500>`_
* `loop_statement_501 <loop_statement_rules.html#loop-statement-501>`_
* `loop_statement_502 <loop_statement_rules.html#loop-statement-502>`_
* `loop_statement_503 <loop_statement_rules.html#loop-statement-503>`_
* `loop_statement_504 <loop_statement_rules.html#loop-statement-504>`_

* `next_statement_500 <next_statement_rules.html#next-statement-500>`_
* `next_statement_501 <next_statement_rules.html#next-statement-501>`_

* `null_statement_500 <null_statement_rules.html#null-statement-500>`_

* `package_004 <package_rules.html#package-004>`_
* `package_006 <package_rules.html#package-006>`_
* `package_008 <package_rules.html#package-008>`_
* `package_010 <package_rules.html#package-010>`_
* `package_013 <package_rules.html#package-013>`_
* `package_018 <package_rules.html#package-018>`_

* `package_body_500 <package_body_rules.html#package-body-500>`_
* `package_body_501 <package_body_rules.html#package-body-501>`_
* `package_body_502 <package_body_rules.html#package-body-502>`_
* `package_body_503 <package_body_rules.html#package-body-503>`_
* `package_body_504 <package_body_rules.html#package-body-504>`_
* `package_body_505 <package_body_rules.html#package-body-505>`_
* `package_body_506 <package_body_rules.html#package-body-506>`_
* `package_body_507 <package_body_rules.html#package-body-507>`_

* `package_instantiation_500 <package_instantiation_rules.html#package-instantiation-500>`_
* `package_instantiation_501 <package_instantiation_rules.html#package-instantiation-501>`_
* `package_instantiation_502 <package_instantiation_rules.html#package-instantiation-502>`_
* `package_instantiation_503 <package_instantiation_rules.html#package-instantiation-503>`_
* `package_instantiation_504 <package_instantiation_rules.html#package-instantiation-504>`_

* `parameter_specification_500 <parameter_specification_rules.html#parameter-specification-500>`_
* `parameter_specification_501 <parameter_specification_rules.html#parameter-specification-501>`_

* `port_010 <port_rules.html#port-010>`_
* `port_017 <port_rules.html#port-017>`_
* `port_019 <port_rules.html#port-019>`_

* `port_map_001 <port_map_rules.html#port-map-001>`_
* `port_map_002 <port_map_rules.html#port-map-002>`_

* `procedure_008 <procedure_rules.html#procedure-008>`_
* `procedure_500 <procedure_rules.html#procedure-500>`_
* `procedure_501 <procedure_rules.html#procedure-501>`_
* `procedure_502 <procedure_rules.html#procedure-502>`_
* `procedure_503 <procedure_rules.html#procedure-503>`_
* `procedure_504 <procedure_rules.html#procedure-504>`_
* `procedure_506 <procedure_rules.html#procedure-506>`_
* `procedure_508 <procedure_rules.html#procedure-508>`_
* `procedure_510 <procedure_rules.html#procedure-510>`_
* `procedure_511 <procedure_rules.html#procedure-511>`_

* `procedure_call_500 <procedure_call_rules.html#procedure-call-500>`_
* `procedure_call_501 <procedure_call_rules.html#procedure-call-501>`_
* `procedure_call_502 <procedure_call_rules.html#procedure-call-502>`_

* `process_004 <process_rules.html#process-004>`_
* `process_005 <process_rules.html#process-005>`_
* `process_008 <process_rules.html#process-008>`_
* `process_009 <process_rules.html#process-009>`_
* `process_013 <process_rules.html#process-013>`_
* `process_017 <process_rules.html#process-017>`_
* `process_019 <process_rules.html#process-019>`_

* `protected_type_500 <protected_type_rules.html#protected-type-500>`_
* `protected_type_501 <protected_type_rules.html#protected-type-501>`_
* `protected_type_502 <protected_type_rules.html#protected-type-502>`_
* `protected_type_body_500 <protected_type_rules.html#protected-type-body-500>`_

* `protected_type_body_501 <protected_type_rules.html#protected-type-body-501>`_
* `protected_type_body_502 <protected_type_rules.html#protected-type-body-502>`_
* `protected_type_body_503 <protected_type_rules.html#protected-type-body-503>`_
* `protected_type_body_504 <protected_type_rules.html#protected-type-body-504>`_

* `range_constraint_500 <../range_constraint_rules.html#range-constraint-500>`_

* `range_001 <range_rules.html#range-001>`_
* `range_002 <range_rules.html#range-002>`_

* `record_type_definition_500 <record_type_definition_rules.html#record-type-definition-500>`_
* `record_type_definition_501 <record_type_definition_rules.html#record-type-definition-501>`_
* `record_type_definition_502 <record_type_definition_rules.html#record-type-definition-502>`_

* `report_statement_500 <report_statement_rules.html#report-statement-500>`_
* `report_statement_501 <report_statement_rules.html#report-statement-501>`_

* `return_statement_500 <return_statement_rules.html#return-statement-500>`_

* `selected_assignment_500 <selected_assignment_rules.html#selected-assignment-500>`_
* `selected_assignment_501 <selected_assignment_rules.html#selected-assignment-501>`_
* `selected_assignment_502 <selected_assignment_rules.html#selected-assignment-502>`_
* `selected_assignment_503 <selected_assignment_rules.html#selected-assignment-503>`_

* `shift_operator_500 <shift_operator_rules.html#shift-operator-500>`_

* `signal_002 <signal_rules.html#signal-002>`_
* `signal_004 <signal_rules.html#signal-004>`_

* `subprogram_instantiation_500 <subprogram_instantiation_rules.html#subprogram-instantiation-500>`_
* `subprogram_instantiation_501 <subprogram_instantiation_rules.html#subprogram-instantiation-501>`_
* `subprogram_instantiation_502 <subprogram_instantiation_rules.html#subprogram-instantiation-502>`_
* `subprogram_instantiation_503 <subprogram_instantiation_rules.html#subprogram-instantiation-503>`_

* `subprogram_kind_500 <subprogram_kind_rules.html#subprogram-kind-500>`_
* `subprogram_kind_501 <subprogram_kind_rules.html#subprogram-kind-501>`_

* `subtype_500 <subtype_rules.html#subtype-500>`_
* `subtype_501 <subtype_rules.html#subtype-501>`_
* `subtype_502 <subtype_rules.html#subtype-502>`_

* `type_002 <type_rules.html#type-002>`_
* `type_004 <type_rules.html#type-004>`_
* `type_013 <type_rules.html#type-013>`_
* `type_500 <type_rules.html#type-500>`_

* `type_mark_500 <type_mark_rules.html#type-mark-500>`_

* `unbounded_array_definition_500 <unbounded_array_definition_rules.html#unbounded-array-definition-500>`_
* `unbounded_array_definition_501 <unbounded_array_definition_rules.html#unbounded-array-definition-501>`_

* `use_clause_500 <use_clause_rules.html#use-clause-500>`_
* `use_clause_501 <use_clause_rules.html#use-clause-501>`_
* `use_clause_502 <use_clause_rules.html#use-clause-502>`_
* `use_clause_503 <use_clause_rules.html#use-clause-503>`_

* `variable_002 <variable_rules.html#variable-002>`_
* `variable_004 <variable_rules.html#variable-004>`_

* `wait_500 <wait_rules.html#wait-500>`_
* `wait_501 <wait_rules.html#wait-501>`_
* `wait_502 <wait_rules.html#wait-502>`_
* `wait_503 <wait_rules.html#wait-503>`_
