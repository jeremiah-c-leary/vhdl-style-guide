
.. include:: includes.rst

.. _configuring-disabled-rules:

Configuring Disabled Rules
--------------------------

Each rule is either enabled (actively checked) or disabled (not checked).
Each rule can be enabled or disabled by user configuration.

Most rules are enabled by default while some are disabled by default.
Rules disabled by default are marked by |disabled| and are typically naming convention rules.
They can be enabled by setting the `disable` option to `False` in a configuration.

.. code-block:: yaml

   rule :
     <rule_id>:
         disable: False

Rules Disabled by Default
#########################

* `after_001 <after_rules.html#after-001>`_
* `after_002 <after_rules.html#after-002>`_
* `after_003 <after_rules.html#after-003>`_
* `alias_declaration_103 <alias_declaration_rules.html#alias-declaration-103>`_
* `alias_declaration_600 <alias_declaration_rules.html#alias-declaration-600>`_
* `alias_declaration_601 <alias_declaration_rules.html#alias-declaration-601>`_
* `architecture_025 <architecture_rules.html#architecture-025>`_
* `block_600 <block_rules.html#block-600>`_
* `block_601 <block_rules.html#block-601>`_
* `block_comment_001 <block_comment_rules.html#block-comment-001>`_
* `block_comment_002 <block_comment_rules.html#block-comment-002>`_
* `block_comment_003 <block_comment_rules.html#block-comment-003>`_
* `case_generate_statement_400 <case_generate_statement_rules.html#case-generate-statement-400>`_
* `comment_011 <comment_rules.html#comment-011>`_
* `comment_012 <comment_rules.html#comment-012>`_
* `constant_015 <constant_rules.html#constant-015>`_
* `constant_101 <constant_rules.html#constant-101>`_
* `constant_200 <constant_rules.html#constant-200>`_
* `constant_600 <constant_rules.html#constant-600>`_
* `context_028 <context_rules.html#context-028>`_
* `context_ref_006 <context_ref_rules.html#context-ref-006>`_
* `context_ref_007 <context_ref_rules.html#context-ref-007>`_
* `context_ref_008 <context_ref_rules.html#context-ref-008>`_
* `context_ref_009 <context_ref_rules.html#context-ref-009>`_
* `file_100 <file_rules.html#file-100>`_
* `function_600 <function_rules.html#function-600>`_
* `function_601 <function_rules.html#function-601>`_
* `generate_017 <generate_rules.html#generate-017>`_
* `generate_600 <generate_rules.html#generate-600>`_
* `generate_601 <generate_rules.html#generate-601>`_
* `generate_602 <generate_rules.html#generate-602>`_
* `generic_020 <generic_rules.html#generic-020>`_
* `generic_600 <generic_rules.html#generic-600>`_
* `generic_map_600 <generic_map_rules.html#generic-map-600>`_
* `generic_map_601 <generic_map_rules.html#generic-map-601>`_
* `instantiation_600 <instantiation_rules.html#instantiation-600>`_
* `instantiation_601 <instantiation_rules.html#instantiation-601>`_

* `interface_incomplete_type_declaration_600 <../interface_incomplete_type_declaration_rules.html#interface-incomplete-type-declaration-600>`_
* `interface_incomplete_type_declaration_601 <../interface_incomplete_type_declaration_rules.html#interface-incomplete-type-declaration-601>`_

* `loop_statement_006 <loop_statement_rules.html#loop-statement-006>`_
* `loop_statement_007 <loop_statement_rules.html#loop-statement-007>`_
* `loop_statement_600 <loop_statement_rules.html#loop-statement-600>`_
* `loop_statement_601 <loop_statement_rules.html#loop-statement-601>`_
* `loop_statement_602 <loop_statement_rules.html#loop-statement-602>`_
* `loop_statement_603 <loop_statement_rules.html#loop-statement-603>`_
* `package_016 <package_rules.html#package-016>`_
* `package_017 <package_rules.html#package-017>`_
* `package_body_600 <package_body_rules.html#package-body-600>`_
* `package_body_601 <package_body_rules.html#package-body-601>`_
* `package_instantiation_600 <package_instantiation_rules.html#package-instantiation-600>`_
* `package_instantiation_601 <package_instantiation_rules.html#package-instantiation-601>`_
* `port_011 <port_rules.html#port-011>`_
* `port_025 <port_rules.html#port-025>`_
* `port_600 <port_rules.html#port-600>`_
* `port_601 <port_rules.html#port-601>`_
* `port_602 <port_rules.html#port-602>`_
* `port_603 <port_rules.html#port-603>`_
* `port_604 <port_rules.html#port-604>`_
* `port_605 <port_rules.html#port-605>`_
* `port_606 <port_rules.html#port-606>`_
* `port_607 <port_rules.html#port-607>`_
* `port_608 <port_rules.html#port-608>`_
* `port_609 <port_rules.html#port-609>`_
* `process_029 <process_rules.html#process-029>`_
* `process_036 <process_rules.html#process-036>`_
* `process_600 <process_rules.html#process-600>`_
* `signal_008 <signal_rules.html#signal-008>`_
* `signal_100 <signal_rules.html#signal-100>`_
* `signal_200 <signal_rules.html#signal-200>`_
* `signal_600 <signal_rules.html#signal-600>`_
* `subtype_004 <subtype_rules.html#subtype-004>`_
* `subtype_100 <subtype_rules.html#subtype-100>`_
* `subtype_200 <subtype_rules.html#subtype-200>`_
* `subtype_600 <subtype_rules.html#subtype-600>`_
* `type_015 <type_rules.html#type-015>`_
* `type_100 <type_rules.html#type-100>`_
* `type_200 <type_rules.html#type-200>`_
* `type_600 <type_rules.html#type-600>`_
* `variable_012 <variable_rules.html#variable-012>`_
* `variable_100 <variable_rules.html#variable-100>`_
* `variable_600 <variable_rules.html#variable-600>`_
