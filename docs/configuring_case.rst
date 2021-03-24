Configuring Uppercase and Lowercase Rules
-----------------------------------------

There are several rules that enforce either uppercase or lowercase.
The default for all such rules is :code:`lowercase`.
The decision was motivated by the fact, that the VHDL language is case insensitive.
Having the same default for all case rules also results in less documentation and code to maintain.
The default value for each of these case rules can be overridden using a configuration.

Overriding Default Lowercase Enforcement
########################################

The default lowercase setting can be changed using a configuration.

For example the rule constant_002 can be changed to enforce uppercase using the following configuration:

.. code-block:: yaml

   ---

   rule :
     constant_002 :
        case : 'upper'

Changing Multiple Case Rules
############################

If there are a lot of case rules you want to change, you can use the global option to reduce the size of the configuration.
For example, if you want to uppercase everything except the entity name, you could write the following configuration:

.. code-block:: yaml

   ---

   rule :
     global :
       case : 'upper'
     entity_008 :
       case : 'lower'

Rules Enforcing Case
####################

* `architecture_004 <architecture_rules.html#architecture-004>`_
* `architecture_009 <architecture_rules.html#architecture-009>`_
* `architecture_011 <architecture_rules.html#architecture-011>`_
* `architecture_013 <architecture_rules.html#architecture-013>`_
* `architecture_014 <architecture_rules.html#architecture-014>`_
* `architecture_019 <architecture_rules.html#architecture-019>`_
* `architecture_020 <architecture_rules.html#architecture-020>`_
* `architecture_021 <architecture_rules.html#architecture-021>`_
* `architecture_028 <architecture_rules.html#architecture-028>`_

* `attribute_declaration_500 <attribute_declaration_rules.html#attribute-declaration-500>`_
* `attribute_declaration_501 <attribute_declaration_rules.html#attribute-declaration-501>`_
* `attribute_declaration_502 <attribute_declaration_rules.html#attribute-declaration-502>`_

* `attribute_specification_500 <attribute_specification_rules.html#attribute-specification-500>`_
* `attribute_specification_501 <attribute_specification_rules.html#attribute-specification-501>`_
* `attribute_specification_502 <attribute_specification_rules.html#attribute-specification-502>`_
* `attribute_specification_503 <attribute_specification_rules.html#attribute-specification-503>`_

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

* `component_004 <component_rules.html#component-004>`_
* `component_006 <component_rules.html#component-006>`_
* `component_008 <component_rules.html#component-008>`_
* `component_010 <component_rules.html#component-010>`_
* `component_012 <component_rules.html#component-012>`_
* `component_014 <component_rules.html#component-014>`_

* `constant_002 <constant_rules.html#constant-002>`_
* `constant_004 <constant_rules.html#constant-004>`_
* `constant_011 <constant_rules.html#constant-011>`_
* `constant_013 <constant_rules.html#constant-013>`_

* `context_004 <context_rules.html#context-004>`_
* `context_012 <context_rules.html#context-012>`_
* `context_013 <context_rules.html#context-013>`_
* `context_014 <context_rules.html#context-014>`_
* `context_015 <context_rules.html#context-015>`_
* `context_016 <context_rules.html#context-016>`_

* `context_ref_003 <context_ref_rules.html#context-ref-003>`_
* `context_ref_004 <context_ref_rules.html#context-ref-004>`_

* `entity_004 <entity_rules.html#entity-004>`_
* `entity_006 <entity_rules.html#entity-006>`_
* `entity_008 <entity_rules.html#entity-008>`_
* `entity_010 <entity_rules.html#entity-010>`_
* `entity_012 <entity_rules.html#entity-012>`_
* `entity_014 <entity_rules.html#entity-014>`_

* `entity_specification_500 <entity_specification_rules.html#entity-specification-500>`_
* `entity_specification_501 <entity_specification_rules.html#entity-specification-501>`_
* `entity_specification_502 <entity_specification_rules.html#entity-specification-502>`_
* `entity_specification_503 <entity_specification_rules.html#entity-specification-503>`_

* `file_statement_002 <file_statement_rules.html#file-statement-002>`_

* `for_loop_003 <for_loop_rules.html#for-loop-003>`_

* `function_004 <function_rules.html#function-004>`_
* `function_005 <function_rules.html#function-005>`_
* `function_010 <function_rules.html#function-010>`_
* `function_013 <function_rules.html#function-013>`_
* `function_014 <function_rules.html#function-014>`_
* `function_017 <function_rules.html#function-017>`_

* `generate_005 <generate_rules.html#generate-005>`_
* `generate_009 <generate_rules.html#generate-009>`_
* `generate_010 <generate_rules.html#generate-010>`_
* `generate_012 <generate_rules.html#generate-012>`_

* `generic_007 <generic_rules.html#generic-007>`_
* `generic_009 <generic_rules.html#generic-009>`_
* `generic_017 <generic_rules.html#generic-017>`_

* `generic_map_001 <generic_map_rules.html#generic-map-001>`_
* `generic_map_002 <generic_map_rules.html#generic-map-002>`_

* `if_statement_025 <if_statement_rules.html#if-statement-025>`_
* `if_statement_026 <if_statement_rules.html#if-statement-026>`_
* `if_statement_027 <if_statement_rules.html#if-statement-027>`_
* `if_statement_028 <if_statement_rules.html#if-statement-028>`_
* `if_statement_029 <if_statement_rules.html#if-statement-029>`_
* `if_statement_034 <if_statement_rules.html#if-statement-034>`_

* `instantiation_008 <instantiation_rules.html#instantiation-008>`_
* `instantiation_009 <instantiation_rules.html#instantiation-009>`_
* `instantiation_027 <instantiation_rules.html#instantiation-027>`_
* `instantiation_031 <instantiation_rules.html#instantiation-031>`_

* `library_004 <library_rules.html#library-004>`_
* `library_005 <library_rules.html#library-005>`_

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

* `port_010 <port_rules.html#port-010>`_
* `port_017 <port_rules.html#port-017>`_
* `port_018 <port_rules.html#port-018>`_
* `port_019 <port_rules.html#port-019>`_

* `port_map_001 <port_map_rules.html#port-map-001>`_
* `port_map_002 <port_map_rules.html#port-map-002>`_

* `procedure_007 <procedure_rules.html#procedure-007>`_
* `procedure_008 <procedure_rules.html#procedure-008>`_
* `procedure_009 <procedure_rules.html#procedure-009>`_

* `process_004 <process_rules.html#process-004>`_
* `process_005 <process_rules.html#process-005>`_
* `process_008 <process_rules.html#process-008>`_
* `process_009 <process_rules.html#process-009>`_
* `process_013 <process_rules.html#process-013>`_
* `process_017 <process_rules.html#process-017>`_
* `process_019 <process_rules.html#process-019>`_

* `range_001 <range_rules.html#range-001>`_
* `range_002 <range_rules.html#range-002>`_

* `signal_002 <signal_rules.html#signal-002>`_
* `signal_004 <signal_rules.html#signal-004>`_
* `signal_010 <signal_rules.html#signal-010>`_
* `signal_011 <signal_rules.html#signal-011>`_
* `signal_014 <signal_rules.html#signal-014>`_

* `subtype_002 <subtype_rules.html#subtype-002>`_

* `type_definition_002 <type_definition.html#type-definition-002>`_
* `type_definition_004 <type_definition.html#type-definition-004>`_
* `type_definition_013 <type_definition.html#type-definition-013>`_
* `type_definition_014 <type_definition.html#type-definition-014>`_

* `variable_002 <variable_rules.html#variable-002>`_
* `variable_004 <variable_rules.html#variable-004>`_
* `variable_010 <variable_rules.html#variable-010>`_
* `variable_011 <variable_rules.html#variable-011>`_
