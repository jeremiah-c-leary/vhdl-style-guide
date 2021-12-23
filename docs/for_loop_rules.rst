.. include:: icons.rst

For Loop Rules
--------------

for_loop_001
############

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

for_loop_002
############

|phase_4| |error| |indent|

This rule checks the indentation of the **end loop** keywords.

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

for_loop_003
############

|phase_6| |error| |case| |case_label|

This rule checks the proper case of the label on a foor loop.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

     LABEL : for index in 4 to 23 loop
     Label : for index in 0 to 100 loop

**Fix**

.. code-block:: vhdl

     label : for index in 4 to 23 loop
     label : for index in 0 to 100 loop

for_loop_004
############

|phase_2| |error| |whitespace|

This rule checks if a label exists on a for loop that a single space exists between the label and the colon.

**Violation**

.. code-block:: vhdl

     label: for index in 4 to 23 loop
     label    : for index in 0 to 100 loop

**Fix**

.. code-block:: vhdl

     label : for index in 4 to 23 loop
     label : for index in 0 to 100 loop

for_loop_005
############

|phase_2| |error| |whitespace|

This rule checks if a label exists on a for loop that a single space exists after the colon.

**Violation**

.. code-block:: vhdl

     label :    for index in 4 to 23 loop
     label :  for index in 0 to 100 loop

**Fix**

.. code-block:: vhdl

     label : for index in 4 to 23 loop
     label : for index in 0 to 100 loop

