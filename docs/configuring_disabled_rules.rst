
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
* `architecture_025 <architecture_rules.html#architecture-025>`_
* `block_600 <block_rules.html#block-600>`_
* `block_601 <block_rules.html#block-601>`_
* `block_comment_001 <block_comment_rules.html#block-comment-001>`_
* `block_comment_002 <block_comment_rules.html#block-comment-002>`_
* `block_comment_003 <block_comment_rules.html#block-comment-003>`_
* `case_generate_statement_300 <case_generate_statement.html#case-statement-generate-400>`_
* `comment_011 <comment_rules.html#comment-011>`_
* `constant_015 <constant_rules.html#constant-015>`_
* `generate_017 <generate_rules.html#generate-017>`_
* `generic_020 <generic_rules.html#generic-020>`_
* `instantiation_600 <instantiation_rules.html#instantiation-600>`_
* `instantiation_601 <instantiation_rules.html#instantiation-601>`_
* `package_016 <package_rules.html#package-016>`_
* `package_017 <package_rules.html#package-017>`_
* `package_body_600 <package_body_rules.html#package-body-600>`_
* `package_body_601 <package_body_rules.html#package-body-601>`_
* `port_011 <port_rules.html#port-011>`_
* `port_025 <port_rules.html#port-025>`_
* `process_029 <process_rules.html#process-029>`_
* `process_036 <process_rules.html#process-036>`_
* `signal_008 <signal_rules.html#signal-008>`_
* `subtype_004 <subtype_rules.html#subtype-004>`_
* `type_015 <type_rules.html#type-015>`_
* `variable_012 <variable_rules.html#variable-012>`_

