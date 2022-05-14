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

* `architecture_012 <architecture_rules.html#architecture-012>`_
* `architecture_022 <architecture_rules.html#architecture-022>`_
* `architecture_030 <architecture_rules.html#architecture-030>`_
* `architecture_031 <architecture_rules.html#architecture-031>`_
* `architecture_032 <architecture_rules.html#architecture-032>`_
* `architecture_033 <architecture_rules.html#architecture-033>`_
* `case_002 <case_rules.html#case-002>`_
* `case_003 <case_rules.html#case-003>`_
* `case_004 <case_rules.html#case-004>`_
* `case_006 <case_rules.html#case-006>`_
* `component_002 <component_rules.html#component-002>`_
* `component_007 <component_rules.html#component-007>`_
* `component_011 <component_rules.html#component-011>`_
* `component_013 <component_rules.html#component-013>`_
* `context_002 <context_rules.html#context-002>`_
* `context_017 <context_rules.html#context-017>`_
* `context_018 <context_rules.html#context-018>`_
* `context_019 <context_rules.html#context-019>`_
* `element_association_100 <element_association_rules.html#element_association_100>`_
* `entity_002 <entity_rules.html#entity-002>`_
* `entity_007 <entity_rules.html#entity-007>`_
* `loop_statement_100 <loop_statement_rules.html#loop_statement-100>`_
* `loop_statement_101 <loop_statement_rules.html#loop_statement-101>`_
* `loop_statement_102 <loop_statement_rules.html#loop_statement-102>`_
* `record_type_definition_100 <record_type_definition_rules.html#record_type_definition-100>`_
* `record_type_definition_101 <record_type_definition_rules.html#record_type_definition-101>`_
