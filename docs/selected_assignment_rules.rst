.. include:: includes.rst

Selected Assignment Rules
-------------------------

selected_assignment_001
#######################

|phase_1| |error| |structure|

This rule checks the **with** keyword is on the same line as the expression.

**Violation**

.. code-block:: vhdl

   with
     mux_sel select addr <=
     "0000" when 0,
     "0001" when 1,
     "1111" when others;

**Fix**

.. code-block:: vhdl

   with mux_sel select addr <=
     "0000" when 0,
     "0001" when 1,
     "1111" when others;

selected_assignment_002
#######################

|phase_1| |error| |structure|

This rule checks the **select** keyword is on the same line as the expression.

**Violation**

.. code-block:: vhdl

   with mux_sel
     select addr <=
     "0000" when 0,
     "0001" when 1,
     "1111" when others;

**Fix**

.. code-block:: vhdl

   with mux_sel select addr <=
     "0000" when 0,
     "0001" when 1,
     "1111" when others;

selected_assignment_003
#######################

|phase_1| |error| |structure|

This rule checks the **select** keyword is on the same line as the target.

**Violation**

.. code-block:: vhdl

   with mux_sel select
     addr <=
     "0000" when 0,
     "0001" when 1,
     "1111" when others;

**Fix**

.. code-block:: vhdl

   with mux_sel select addr <=
     "0000" when 0,
     "0001" when 1,
     "1111" when others;

selected_assignment_004
#######################

|phase_1| |error| |structure|

This rule checks the assignment is on the same line as the target.

**Violation**

.. code-block:: vhdl

   with mux_sel select addr
     <=
     "0000" when 0,
     "0001" when 1,
     "1111" when others;

**Fix**

.. code-block:: vhdl

   with mux_sel select addr <=
     "0000" when 0,
     "0001" when 1,
     "1111" when others;

selected_assignment_005
#######################

|phase_1| |error| |structure|

This rule checks for code after the assignment.

**Violation**

.. code-block:: vhdl

   with mux_sel select addr <= "0000" when 0,
     "0001" when 1,
     "1111" when others;

**Fix**

.. code-block:: vhdl

   with mux_sel select addr <=
     "0000" when 0,
     "0001" when 1,
     "1111" when others;

selected_assignment_006
#######################

|phase_1| |error| |structure|

This rule checks for code after the **force** keyword.

**Violation**

.. code-block:: vhdl

   with mux_sel select addr <= force "0000" when 0,
     "0001" when 1,
     "1111" when others;

**Fix**

.. code-block:: vhdl

   with mux_sel select addr <= force
     "0000" when 0,
     "0001" when 1,
     "1111" when others;

selected_assignment_007
#######################

|phase_1| |error| |structure|

This rule checks for code after the force mode keywords **in** and **out**.

**Violation**

.. code-block:: vhdl

   with mux_sel select addr <= force in "0000" when 0,
     "0001" when 1,
     "1111" when others;

**Fix**

.. code-block:: vhdl

   with mux_sel select addr <= force in
     "0000" when 0,
     "0001" when 1,
     "1111" when others;

selected_assignment_008
#######################

|phase_1| |error| |structure|

This rule checks for code after the **guarded** keyword.

**Violation**

.. code-block:: vhdl

   with mux_sel select addr <= guarded "0000" when 0,
     "0001" when 1,
     "1111" when others;

**Fix**

.. code-block:: vhdl

   with mux_sel select addr <= guarded
     "0000" when 0,
     "0001" when 1,
     "1111" when others;

selected_assignment_009
#######################

|phase_1| |error| |structure|

This rule checks for code after the delay mechanism keywords **transport** and **inertial**.

**Violation**

.. code-block:: vhdl

   with mux_sel select addr <= transport "0000" when 0,
     "0001" when 1,
     "1111" when others;

**Fix**

.. code-block:: vhdl

   with mux_sel select addr <= transport
     "0000" when 0,
     "0001" when 1,
     "1111" when others;

selected_assignment_010
#######################

|phase_1| |error| |structure|

This rule checks the **when** keyword is on the same line as the expression or waveform.

**Violation**

.. code-block:: vhdl

   with mux_sel select addr <=
     "0000"
     when 0,
     "0001" when 1,
     "1111" when others;

**Fix**

.. code-block:: vhdl

   with mux_sel select addr <=
     "0000" when 0,
     "0001" when 1,
     "1111" when others;

selected_assignment_011
#######################

|phase_1| |error| |structure|

This rule checks the **when** keyword is on the same line as the choices.

**Violation**

.. code-block:: vhdl

   with
     mux_sel select addr <=
     "0000" when
     0,
     "0001" when 1,
     "1111" when others;

**Fix**

.. code-block:: vhdl

   with mux_sel select addr <=
     "0000" when 0,
     "0001" when 1,
     "1111" when others;

selected_assignment_012
#######################

|phase_1| |error| |structure|

This rule checks for code after the comma in choices.

**Violation**

.. code-block:: vhdl

   with mux_sel select addr <=
     "0000" when 0, "0001" when 1, "1111" when others;

**Fix**

.. code-block:: vhdl

   with mux_sel select addr <= force
     "0000" when 0,
     "0001" when 1,
     "1111" when others;

selected_assignment_100
#######################

|phase_2| |error| |whitespace|

This rule checks for a single space after the **with** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   with    mux_sel select addr <=
     "0000" when 0,
     "0001" when 1,
     "1111" when others;

**Fix**

.. code-block:: vhdl

   with mux_sel select addr <=
     "0000" when 0,
     "0001" when 1,
     "1111" when others;

selected_assignment_101
#######################

|phase_2| |error| |whitespace|

This rule checks for a single space before the **select** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   with mux_sel     select addr <=
     "0000" when 0,
     "0001" when 1,
     "1111" when others;

**Fix**

.. code-block:: vhdl

   with mux_sel select addr <=
     "0000" when 0,
     "0001" when 1,
     "1111" when others;

selected_assignment_102
#######################

|phase_2| |error| |whitespace|

This rule checks for a single space after the **select** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   with mux_sel select    addr <=
     "0000" when 0,
     "0001" when 1,
     "1111" when others;

**Fix**

.. code-block:: vhdl

   with mux_sel select addr <=
     "0000" when 0,
     "0001" when 1,
     "1111" when others;

selected_assignment_103
#######################

|phase_2| |error| |whitespace|

This rule checks for a single space before the assignment.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   with mux_sel select addr<=
     "0000" when 0,
     "0001" when 1,
     "1111" when others;

**Fix**

.. code-block:: vhdl

   with mux_sel select addr <=
     "0000" when 0,
     "0001" when 1,
     "1111" when others;

selected_assignment_104
#######################

|phase_2| |error| |whitespace|

This rule checks for a single space after the assignment.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   with mux_sel select addr <=    "0000" when 0,
     "0001" when 1,
     "1111" when others;

**Fix**

.. code-block:: vhdl

   with mux_sel select addr <= "0000" when 0,
     "0001" when 1,
     "1111" when others;

selected_assignment_105
#######################

|phase_2| |error| |whitespace|

This rule checks for a single space after the **force** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   with mux_sel select addr <= force   "0000" when 0,
     "0001" when 1,
     "1111" when others;

**Fix**

.. code-block:: vhdl

   with mux_sel select addr <= force "0000" when 0,
     "0001" when 1,
     "1111" when others;

selected_assignment_106
#######################

|phase_2| |error| |whitespace|

This rule checks for a single space before the **when** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   with mux_sel select addr <=
     "0000"    when 0,
     "0001"when 1,
     "1111" when others;

**Fix**

.. code-block:: vhdl

   with mux_sel select addr <=
     "0000" when 0,
     "0001" when 1,
     "1111" when others;

selected_assignment_107
#######################

|phase_2| |error| |whitespace|

This rule checks for a single space after the **when** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   with mux_sel select addr <=
     "0000" when     0,
     "0001" when  1,
     "1111" when others;

**Fix**

.. code-block:: vhdl

   with mux_sel select addr <=
     "0000" when 0,
     "0001" when 1,
     "1111" when others;

selected_assignment_300
#######################

|phase_4| |error| |indent|

This rule checks the indent of the **with** keyword.

**Violation**

.. code-block:: vhdl

   wr_en <= '1';

       with mux_sel select addr <=
     "0000" when 0,
     "0001" when 1,
     "1111" when others;

**Fix**

.. code-block:: vhdl

   wr_en <= '1';

   with mux_sel select addr <=
     "0000" when 0,
     "0001" when 1,
     "1111" when others;

selected_assignment_400
#######################

|phase_5| |error| |alignment|

This rule checks the alignment of multiline selected assignment statements.

|configuring_multiline_indent_rules_link|

**Violation**

.. code-block:: vhdl

   with (mux_select or reset) select addr <=
   "0000" when 0,
           "0001" when 1,
        "1111" when others;

**Fix**

.. code-block:: vhdl

   with (mux_select or reset) select addr <=
     "0000" when 0,
     "0001" when 1,
     "1111" when others;

selected_assignment_500
#######################

|phase_6| |error| |case| |case_keyword|

This rule checks the **with** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   WITH mux_sel select addr <=
     "0000" when 0,
     "0001" when 1,
     "1111" when others;

**Fix**

.. code-block:: vhdl

   with mux_sel select addr <=
     "0000" when 0,
     "0001" when 1,
     "1111" when others;

selected_assignment_501
#######################

|phase_6| |error| |case| |case_keyword|

This rule checks the **select** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   with mux_sel SELECT addr <=
     "0000" when 0,
     "0001" when 1,
     "1111" when others;

**Fix**

.. code-block:: vhdl

   with mux_sel select addr <=
     "0000" when 0,
     "0001" when 1,
     "1111" when others;

selected_assignment_502
#######################

|phase_6| |error| |case| |case_keyword|

This rule checks the **force** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   with mux_sel select addr <= FORCE
     "0000" when 0,
     "0001" when 1,
     "1111" when others;

**Fix**

.. code-block:: vhdl

   with mux_sel select addr <= force
     "0000" when 0,
     "0001" when 1,
     "1111" when others;

selected_assignment_503
#######################

|phase_6| |error| |case| |case_keyword|

This rule checks the **when** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   with mux_sel select addr <=
     "0000" WHEN 0,
     "0001" WHEN 1,
     "1111" WHEN others;

**Fix**

.. code-block:: vhdl

   with mux_sel select addr <=
     "0000" when 0,
     "0001" when 1,
     "1111" when others;

