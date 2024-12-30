.. include:: includes.rst

Iteration Scheme Rules
----------------------

iteration_scheme_100
####################

|phase_2| |error| |whitespace|

This rule checks that a single space exists after the **while** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   while(condition)

   while      (condition)

**Fix**

.. code-block:: vhdl

   while (condition)

   while (condition)

iteration_scheme_101
####################

|phase_2| |error| |whitespace|

This rule checks that a single space exists after the **for** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   for      x in (31 downto 0) loop

**Fix**

.. code-block:: vhdl

   for x in (31 downto 0) loop

iteration_scheme_300
####################

|phase_4| |error| |indent|

This rule checks for indentation of the **while** keyword.
Proper indentation enhances comprehension.

**Violation**

.. code-block:: vhdl

   begin

   while (temp /= 0) loop
       temp := temp/2;
     end loop;

**Fix**

.. code-block:: vhdl

   begin

     while (temp /= 0) loop
       temp := temp/2;
     end loop;

iteration_scheme_301
####################

|phase_4| |error| |indent|

This rule checks the indentation of the **for** keyword.

**Violation**

.. code-block:: vhdl

   fifo_proc : process () is
   begin

   for index in 4 to 23 loop

     end loop;

   end process;

**Fix**

.. code-block:: vhdl

   fifo_proc : process () is
   begin

     for index in 4 to 23 loop

     end loop;

   end process;

iteration_scheme_500
####################

|phase_6| |error| |case| |case_keyword|

This rule checks the **while** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   WHILE (condition) loop

**Fix**

.. code-block:: vhdl

   while (condition) loop

iteration_scheme_501
####################

|phase_6| |error| |case| |case_keyword|

This rule checks the **for** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   FOR x in (31 downto 0) loop

**Fix**

.. code-block:: vhdl

   for x in (31 downto 0) loop

iteration_scheme_502
####################

|phase_6| |error| |case| |case_keyword|

This rule checks the **in** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   for lv_thing IN t_thing loop

**Fix**

.. code-block:: vhdl

   for lv_thing in t_thing loop
