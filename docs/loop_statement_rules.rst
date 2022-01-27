.. include:: icons.rst

Loop Statement Rules
--------------------

loop_statement_001
##################

|phase_1| |error| |structure|

This rule checks for code after the **loop** keyword.

**Violation**

.. code-block:: vhdl

   loop a <= b;

**Fix**

.. code-block:: vhdl

   loop
     a <= b;

loop_statement_002
##################

|phase_1| |error| |structure|

This rule checks the **end** keyword is on it's own line.

**Violation**

.. code-block:: vhdl

   loop
     a <= b; end loop;

**Fix**

.. code-block:: vhdl

   loop
     a <= b;
   end loop;

loop_statement_100
##################

|phase_2| |error| |whitespace|

This rule checks that a single exists between the **end** and **loop** keywords

**Violation**

.. code-block:: vhdl

     end loop;
     end    loop;

**Fix**

.. code-block:: vhdl

     end loop;
     end loop;

loop_statement_101
##################

|phase_2| |error| |whitespace|

This rule checks for a single space before the ending loop label if it exists.

**Violation**

.. code-block:: vhdl

   end loop           END_LOOP_LABEL;

**Fix**

.. code-block:: vhdl

   end loop END_LOOP_LABEL;

loop_statement_102
##################

|phase_2| |error| |whitespace|

This rule checks for a single space before the **loop** keyword.

**Violation**

.. code-block:: vhdl

  for x in (0 to 30)loop
  for x in (0 to 30)         loop

**Fix**

.. code-block:: vhdl

  for x in (0 to 30) loop
  for x in (0 to 30) loop

loop_statement_300
##################

|phase_4| |error| |indent|

This rule checks the indentation of the **loop** keyword.

**Violation**

.. code-block:: vhdl

   fifo_proc : process () is
   begin

       loop

     end loop;

   end process;

**Fix**

.. code-block:: vhdl

   fifo_proc : process () is
   begin

     loop

     end loop;

   end process;

loop_statement_301
##################

|phase_4| |error| |indent|

This rule checks the indentation of the loop label if it exists.

**Violation**

.. code-block:: vhdl

   fifo_proc : process () is
   begin

       LOOP_LABEL : loop

     end loop;

   end process;

**Fix**

.. code-block:: vhdl

   fifo_proc : process () is
   begin

     LOOP_LABEL : loop

     end loop;

   end process;

loop_statement_500
##################

|phase_6| |error| |case| |case_keyword|

This rule checks the **loop** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   while (condition) LOOP

**Fix**

.. code-block:: vhdl

   while (condition) loop

loop_statement_501
##################

|phase_6| |error| |case| |case_keyword|

This rule checks the **end** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   while (condition) loop

   END loop;

**Fix**

.. code-block:: vhdl

   while (condition) loop

   end loop;

loop_statement_502
##################

|phase_6| |error| |case| |case_keyword|

This rule checks the **loop** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   while (condition) loop

   end LOOP;

**Fix**

.. code-block:: vhdl

   while (condition) loop

   end loop;

