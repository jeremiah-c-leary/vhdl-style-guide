.. _configuring-whitespace-rules:

Configuring Whitespace Rules
----------------------------

There are rules which will check for a single whitespace between keywords or keywords and identifiers.
The single whitespace can be configured to allow for multiple or no whitespaces.

<jcl - rewrite the following sentence>
There are a couple of options to these rules, which can be selected by using the :code:`style` option:

+--------------------------+----------------------------------------------------------+
| Option                   | Description                                              |
+==========================+==========================================================+
| number_of_spaces         | Determines the number of whitespace characters to allow. |
+--------------------------+----------------------------------------------------------+
| align_to_next_tab        | When true, will add spaces to align with next valid tab. |
+--------------------------+----------------------------------------------------------+

The :code:`maximum_number_of_spaces` and :code:`minimum_number_of_spaces` can accept several values:

+-----------------------+----------------------------------------------------------+
| Value                 | Description                                              |
+=======================+==========================================================+
| [0-9][0-9]*           | The number of spaces to enforce.                         |
+-----------------------+----------------------------------------------------------+
| >[0-9][0-9]*          | The minimum number of spaces to enforce.                 |
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
        maximum_number_of_spaces: >1
        minimum_number_of_spaces: 1

In this example, there must be at least a single whitespace before the colon.
All of these would not be a violation.

.. code-Block:: vhdl

   signal wr_en : std_logic;
   signal wr_en  : std_logic;
   signal wr_en                : std_logic;

Example:  allow between 3 and 5 spaces after a colon
####################################################

.. code-block:: yaml

   rule :
     signal_005:
        maximum_number_of_spaces: 5
        minimum_number_of_spaces: 3

In this example, there must be at least 3 spaces after the colon and no more than 5.
All of these would not be a violation.

.. code-block:: vhdl

   signal wr_en :   std_logic;
   signal wr_en :     std_logic;
   signal wr_en :      std_logic;

If there were less than 3 spaces...

.. code-block:: vhdl

   signal wr_en : std_logic;

Then the code would be a violation and the fix would insert enough spaces to get to 3:

.. code-block:: vhdl

   signal wr_en :   std_logic;

If there were more than 5 spaces...

.. code-block:: vhdl

   signal wr_en :                std_logic;

Then the code would be a violation and the fix would remove enough spaces to get to 5:

.. code-block:: vhdl

   signal wr_en :     std_logic;

Rules Enforcing Whitespace
##########################

* `alias_declaration_100 <alias_declaration_rules.html#alias-declaration-100>`_
* `alias_declaration_102 <alias_declaration_rules.html#alias-declaration-102>`_
* `architecture_012 <architecture_rules.html#architecture-012>`_
* `architecture_022 <architecture_rules.html#architecture-022>`_
* `architecture_030 <architecture_rules.html#architecture-030>`_
* `architecture_031 <architecture_rules.html#architecture-031>`_
* `architecture_032 <architecture_rules.html#architecture-032>`_
* `architecture_033 <architecture_rules.html#architecture-033>`_
* `attribute_declaration_100 <attribute_declaration_rules.html#attribute-declaration-100>`_
* `attribute_specification_100 <attribute_specification_rules.html#attribute-specification-100>`_
* `block_100 <block_rules.html#block-100>`_
* `block_101 <block_rules.html#block-101>`_
* `case_002 <case_rules.html#case-002>`_
* `case_003 <case_rules.html#case-003>`_
* `case_004 <case_rules.html#case-004>`_
* `case_006 <case_rules.html#case-006>`_
* `component_002 <component_rules.html#component-002>`_
* `component_007 <component_rules.html#component-007>`_
* `component_011 <component_rules.html#component-011>`_
* `component_013 <component_rules.html#component-013>`_
* `concurrent_004 <concurrent_rules.html#concurrent-004>`_
* `constant_005 <constant_rules.html#constant-005>`_
* `constant_100 <constant_rules.html#constant-100>`_
* `context_002 <context_rules.html#context-002>`_
* `context_017 <context_rules.html#context-017>`_
* `context_018 <context_rules.html#context-018>`_
* `context_019 <context_rules.html#context-019>`_
* `context_ref_002 <context_ref.html#context_ref-002>`_
* `element_association_100 <element_association_rules.html#element_association_100>`_
* `entity_002 <entity_rules.html#entity-002>`_
* `entity_007 <entity_rules.html#entity-007>`_
* `entity_specification_100 <entity_specification_rules.html#entity-specification-100>`_
* `function_100 <function_rules.html#function-100>`_
* `function_101 <function_rules.html#function-101>`_
* `generate_002 <generate_rules.html#generate-002>`_
* `generate_008 <generate_rules.html#generate-008>`_
* `generate_013 <generate_rules.html#generate-013>`_
* `generate_014 <generate_rules.html#generate-014>`_
* `generic_003 <generic_rules.html#generic-003>`_
* `generic_005 <generic_rules.html#generic-005>`_
* `if_003 <if_rules.html#if-003>`_
* `if_004 <if_rules.html#if-004>`_
* `if_005 <if_rules.html#if-005>`_
* `if_015 <if_rules.html#if-015>`_
* `instantiation_002 <instantiation_rules.html#instantiation-002>`_
* `instantiation_003 <instantiation_rules.html#instantiation-003>`_
* `instantiation_032 <instantiation_rules.html#instantiation-032>`_
* `iteration_scheme_100 <interation_scheme_rules.html#iteration-scheme-100>`_
* `iteration_scheme_101 <interation_scheme_rules.html#iteration-scheme-101>`_
* `library_002 <library_rules.html#library-002>`_
* `library_006 <library_rules.html#library-006>`_
* `loop_statement_100 <loop_statement_rules.html#loop_statement-100>`_
* `loop_statement_101 <loop_statement_rules.html#loop_statement-101>`_
* `loop_statement_102 <loop_statement_rules.html#loop_statement-102>`_
* `loop_statement_104 <loop_statement_rules.html#loop_statement-104>`_
* `package_002 <package_rules.html#package-002>`_
* `package_009 <package_rules.html#package-009>`_
* `package_body_100 <package_body_rules.html#package_body-100>`_
* `package_body_101 <package_body_rules.html#package_body-101>`_
* `procedure_100 <procedure_rules.html#procedure-100>`_
* `procedure_101 <procedure_rules.html#procedure-101>`_
* `process_002 <process_rules.html#process-002>`_
* `process_007 <process_rules.html#process-007>`_
* `process_014 <process_rules.html#process-014>`_
* `process_024 <process_rules.html#process-024>`_
* `process_025 <process_rules.html#process-025>`_
* `record_type_definition_100 <record_type_definition_rules.html#record_type_definition-100>`_
* `record_type_definition_101 <record_type_definition_rules.html#record_type_definition-101>`_
* `sequential_002 <sequential_rules.html#sequential-002>`_
* `signal_005 <signal_rules.html#signal-005>`_
* `type_definition_006 <type_rules.html#type-006>`_
* `type_definition_007 <type_rules.html#type-007>`_
* `variable_005 <variable_rules.html#variable-002>`_
* `variable_assignment_002 <variable_assignment_rules.html#variable_assignment-002>`_
