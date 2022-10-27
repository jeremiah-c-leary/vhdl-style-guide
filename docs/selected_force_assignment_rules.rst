.. include:: includes.rst

Selected Force Assignment Rules
-------------------------------

selected_force_assignment_300
#############################

|phase_4| |error| |indent|

This rule checks the indent of the **with** keyword.

**Violation**

.. code-block:: vhdl

   wr_en <= '1';

       with mux_sel select
     addr <= force "0000" when 0,
                   "0001" when 1,
                   "1111" when others;

**Fix**

.. code-block:: vhdl

   wr_en <= '1';

   with mux_sel select
     addr <= force "0000" when 0,
                   "0001" when 1,
                   "1111" when others;

selected_force_assignment_500
#############################

|phase_6| |error| |case| |case_keyword|

This rule checks the **with** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   WITH mux_sel select
     addr <= force "0000" when 0,
                   "0001" when 1,
                   "1111" when others;

**Fix**

.. code-block:: vhdl

   with mux_sel select
     addr <= force "0000" when 0,
                   "0001" when 1,
                   "1111" when others;

selected_force_assignment_501
#############################

|phase_6| |error| |case| |case_keyword|

This rule checks the **with** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   with mux_sel SELECT
     addr <= force "0000" when 0,
                   "0001" when 1,
                   "1111" when others;

**Fix**

.. code-block:: vhdl

   with mux_sel select
     addr <= force "0000" when 0,
                   "0001" when 1,
                   "1111" when others;

selected_force_assignment_502
#############################

|phase_6| |error| |case| |case_keyword|

This rule checks the **force** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   with mux_sel select
     addr <= FORCE "0000" when 0,
                   "0001" when 1,
                   "1111" when others;

**Fix**

.. code-block:: vhdl

   with mux_sel select
     addr <= force "0000" when 0,
                   "0001" when 1,
                   "1111" when others;

