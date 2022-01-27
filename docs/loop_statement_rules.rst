.. include:: icons.rst

Loop Statement Rules
--------------------

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

   end LOOP;

**Fix**

.. code-block:: vhdl

   while (condition) loop

   end loop;

