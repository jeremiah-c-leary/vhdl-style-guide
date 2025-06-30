
.. _configuring-optional-items:

Configuring Optional Items
--------------------------

There are optional language items in VHDL.
In the Language Reference Manual (LRM) they are denoted with square brackets [].
Using many of these optional items improves the readability of VHDL code.

However, it may not fit the current style of existing code bases.
The rules checking the optional items can be configured to add or remove them.

.. |action| replace::
   :code:`action`

.. |action__add| replace::
   :code:`add` = Add the optional item.

.. |action__remove| replace::
   :code:`remove` = Remove the optional item.

.. |values| replace::
   :code:`add`, :code:`remove`

.. |default_value| replace::
   :code:`add`

+----------------------+----------+-----------------+----------------------------+
| Option               | Values   | Default Value   | Description                |
+======================+==========+=================+============================+
| |action|             | |values| | |default_value| | * |action__add|            |
|                      |          |                 | * |action__remove|         |
+----------------------+----------+-----------------+----------------------------+

This is an example of how to configure these options.

.. code-block:: yaml

   rule :
     architecture_010:
        action: 'add'

.. NOTE:: The following examples are using rule architecture_010.

Example: |action| set to :code:`add`
####################################

    **Violation**

    .. code-block:: yaml

       architecture rtl of fifo is
       begin
       end fifo;

    **Violation**

    .. code-block:: yaml

       architecture rtl of fifo is
       begin
       end architecture fifo;

Example: |action| set to :code:`remove`
#######################################

    **Violation**

    .. code-block:: yaml

       architecture rtl of fifo is
       begin
       end architecture fifo;

    **Violation**

    .. code-block:: yaml

       architecture rtl of fifo is
       begin
       end fifo;

Rules Enforcing Optional Items
##############################

* `architecture_010 <architecture_rules.html#architecture-010>`_
* `architecture_024 <architecture_rules.html#architecture-024>`_
* `block_002 <block_rules.html#block-002>`_
* `block_007 <block_rules.html#block-007>`_
* `component_021 <component_rules.html#component-021>`_
* `component_022 <component_rules.html#component-022>`_
* `context_021 <context_rules.html#context-021>`_
* `context_022 <context_rules.html#context-022>`_
* `entity_015 <entity_rules.html#entity-015>`_
* `entity_019 <entity_rules.html#entity-019>`_
* `function_018 <function_rules.html#function-018>`_
* `function_020 <function_rules.html#function-020>`_
* `generate_011 <generate_rules.html#generate-011>`_
* `instantiation_033 <instantiation_rules.html#instantiation-033>`_
* `instantiation_036 <instantiation_rules.html#instantiation-036>`_
* `loop_statement_007 <loop_statement_rules.html#loop-statement-007>`_
* `package_007 <package_rules.html#package-007>`_
* `package_014 <package_rules.html#package-014>`_
* `package_body_002 <package_body_rules.html#package-body-002>`_
* `package_body_003 <package_body_rules.html#package-body-003>`_
* `procedure_012 <procedure_rules.html#procedure-012>`_
* `procedure_014 <procedure_rules.html#procedure-014>`_
* `process_012 <process_rules.html#process-012>`_
* `process_018 <process_rules.html#process-018>`_
* `record_type_definition_005 <record_type_definition_rules.html#record-type-definition-005>`_
