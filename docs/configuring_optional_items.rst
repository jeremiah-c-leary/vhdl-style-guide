
.. _configuring-optional-items:

Configuring Optional Items
--------------------------

There are optional language items in VHDL.
In the Language Reference Manual (LRM) they are denoted with square brackets [].
Using many of these optional items improves the readability of VHDL code.

However, it may not fit the current style of existing code bases.
The rules checking the optional items can be configured to add or remove them.

Adding Optional Items
#####################

This is the default behavior for these rules.

The configuration format to **add** the optional items is shown below:

.. code-block:: yaml

   rule :
     <rule_id>:
        action: 'add'


Removing Optional Items
#######################

The configuration format to **remove** the optional items is shown below:

.. code-block:: yaml

   rule :
     <rule_id>:
        action: 'remove'

Rules Enforcing Optional Items
##############################

* `architecture_010 <architecture_rules.html#architecture-010>`_
* `architecture_024 <architecture_rules.html#architecture-024>`_
* `block_002 <block_rules.html#block-002>`_
* `block_007 <block_rules.html#block-007>`_
* `component_021 <component_rules.html#component-021>`_
* `context_021 <context_rules.html#context-021>`_
* `context_022 <context_rules.html#context-022>`_
* `entity_015 <entity_rules.html#entity-015>`_
* `entity_019 <entity_rules.html#entity-019>`_
* `function_018 <function_rules.html#function-018>`_
* `generate_011 <generate_rules.html#generate-011>`_
* `instantiation_033 <instantiation_rules.html#instantiation-033>`_
* `loop_statement_007 <loop_statement_rules.html#loop-statement-007>`_
* `package_007 <package_rules.html#package-007>`_
* `package_014 <package_rules.html#package-014>`_
* `package_body_002 <package_body_rules.html#package-body-002>`_
* `package_body_003 <package_body_rules.html#package-body-003>`_
* `procedure_012 <procedure_rules.html#procedure-012>`_
* `process_012 <process_rules.html#process-012>`_
* `process_018 <process_rules.html#process-018>`_
* `record_type_definition_005 <record_type_definition_rules.html#record-type-definition-005>`_
