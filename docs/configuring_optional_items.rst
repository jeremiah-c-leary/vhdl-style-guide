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

* `architecture_010 <architecture_rules.html#architecture_010>`_
* `architecture_024 <architecture_rules.html#architecture_024>`_
* `block_002 <block_rules.html#block_002>`_
* `block_007 <block_rules.html#block_007>`_
* `component_021 <component_rules.html#component_021>`_
* `context_021 <context_rules.html#context_021>`_
* `context_022 <context_rules.html#context_022>`_
* `entity_015 <entity_rules.html#entity_015>`_
* `entity_019 <entity_rules.html#entity_019>`_
* `instantiation_033 <instantiation_rules.html.html#instantiation_033>`_
* `package_007 <package_rules.html#package_007>`_
* `package_014 <package_rules.html#package_014>`_
* `package_body_002 <package_body_rules.html#package_body_002>`_
* `package_body_003 <package_body_rules.html#package_body_003>`_
* `process_012 <process_rules.html#process_012>`_
* `process_018 <process_rules.html#process_018>`_
