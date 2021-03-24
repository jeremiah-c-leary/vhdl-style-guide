Configuring Blank Lines
-----------------------

There are rules which will check for blank lines either above or below a line.
These rules are designed to improve readability by separating code using blank lines.

There are a couple of options to these rules, which can be selected by using the :code:`style` option:

+---------------------+----------------------------------------------------------+
| Style               | Description                                              |
+=====================+==========================================================+
| no_blank_line       | Removes blank lines on the line above or below.          |
+---------------------+----------------------------------------------------------+
| require_blank_line  | Requires a blank line on the line above or below.        |
+---------------------+----------------------------------------------------------+

.. code-block:: yaml

   rule :
     architecture_015:
        style : require_blank_line

.. WARNING:: It is important to be aware these rules may conflict with rules that enforce rules on previous lines.
  This can occur when a below rule is applied and then on the next line a previous rule applies.
  Resolve any conflicts by changing the configuration of either rule.

Example: require_blank_line
###########################

The following code would fail with this option:

.. code-Block:: vhdl

   architecture rtl of fifo is
     -- Comment

   architecture rtl of fifo is
     signal s_sig1 : std_logic;

The following code would pass with this option:

.. code-block:: vhdl

   architecture rtl of fifo is

     -- Comment

   architecture rtl of fifo is

     signal s_sig1 : std_logic;

Example: no_blank_line
######################

The following code would fail with this option:

.. code-Block:: vhdl

   architecture rtl of fifo is

     -- Comment

   architecture rtl of fifo is

     signal s_sig1 : std_logic;

The following code would pass with this option:

.. code-block:: vhdl

   architecture rtl of fifo is
     -- Comment

   architecture rtl of fifo is
     signal s_sig1 : std_logic;

Rules Enforcing Blank Lines
###########################

* `architecture_015 <architecture_rules.html#architecture-015>`_
* `architecture_016 <architecture_rules.html#architecture-016>`_
* `architecture_017 <architecture_rules.html#architecture-017>`_
* `architecture_018 <architecture_rules.html#architecture-018>`_
* `architecture_200 <architecture_rules.html#architecture-200>`_
* `block_201 <block_rules.html#block-201>`_
* `block_202 <block_rules.html#block-202>`_
* `block_203 <block_rules.html#block-203>`_
* `block_204 <block_rules.html#block-204>`_
* `block_205 <block_rules.html#block-205>`_
* `case_008 <case_rules.html#case-008>`_
* `case_009 <case_rules.html#case-009>`_
* `case_010 <case_rules.html#case-010>`_
* `component_018 <component_rules.html#component-018>`_
* `context_023 <context_rules.html#context-023>`_
* `context_024 <context_rules.html#context-024>`_
* `context_025 <context_rules.html#context-025>`_
* `function_007 <function_rules.html#function-007>`_
* `generate_003 <generate_rules.html#generate-003>`_
* `if_030 <if_statement_rules.html#if_statement-030>`_
* `instantiation_019 <instantiation_rules.html#instantiation-019>`_
* `package_011 <package_rules.html#package-011>`_
* `package_012 <package_rules.html#package-012>`_
* `package_body_201 <package_body_rules.html#package-body-201>`_
* `package_body_202 <package_body_rules.html#package-body-202>`_
* `package_body_203 <package_body_rules.html#package-body-203>`_
* `process_011 <process_rules.html#process-011>`_
* `process_021 <process_rules.html#process-021>`_
* `process_022 <process_rules.html#process-022>`_
* `process_023 <process_rules.html#process-023>`_
* `process_026 <process_rules.html#process-026>`_
* `process_027 <process_rules.html#process-027>`_
* `type_011 <type_rules.html#type-011>`_
