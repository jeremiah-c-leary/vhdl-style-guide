.. include:: includes.rst

Wait Rules
----------

wait_001
########

|phase_4| |error| |indent|

This rule checks for indentation of the **wait** keyword.
Proper indentation enhances comprehension.

**Violation**

.. code-block:: vhdl

   begin

       wait for 10ns;
    wait on a,b;
          wait until a = '0';

**Fix**

.. code-block:: vhdl

   begin

     wait for 10ns;
     wait on a,b;
     wait until a = '0';

wait_300
########

|phase_4| |error| |indent|

This rule checks for indentation of the label.
Proper indentation enhances comprehension.

**Violation**

.. code-block:: vhdl

   begin

    wait on a,b;
          wait_label : wait until a = '0';

**Fix**

.. code-block:: vhdl

   begin

     wait on a,b;
     wait_label : wait until a = '0';

wait_500
########

|phase_6| |error| |case| |case_keyword|

This rule checks the **wait** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   WAIT for 100 ns;

**Fix**

.. code-block:: vhdl

   wait for 100 ns;

wait_501
########

|phase_6| |error| |case| |case_keyword|

This rule checks the **on** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   wait ON condition;

**Fix**

.. code-block:: vhdl

   wait on condition;

wait_502
########

|phase_6| |error| |case| |case_keyword|

This rule checks the **until** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   wait UNTIL rising_edge(clk);

**Fix**

.. code-block:: vhdl

   wait until rising_edge(clk);

wait_503
########

|phase_6| |error| |case| |case_keyword|

This rule checks the **for** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   wait FOR 100 ns;

**Fix**

.. code-block:: vhdl

   wait for 100 ns;
