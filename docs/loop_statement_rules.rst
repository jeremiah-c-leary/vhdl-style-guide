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

loop_statement_003
##################

|phase_1| |error| |structure|

This rule checks the **end** keyword is on the same line as the **end loop** keyword.

**Violation**

.. code-block:: vhdl

   end
   loop;

**Fix**

.. code-block:: vhdl

   end loop;

loop_statement_004
##################

|phase_1| |error| |structure|

This rule checks the semicolon is on the same line as the **end loop** keyword.

**Violation**

.. code-block:: vhdl

   end loop
   ;

   end loop LOOP_LABEL
   ;

**Fix**

.. code-block:: vhdl

   end loop;

   end loop LOOP_LABEL;

loop_statement_005
##################

|phase_1| |error| |structure|

This rule checks the loop label and the **while**, **for** or **loop** keywords are on the same line.

**Violation**

.. code-block:: vhdl

   LOOP_LABEL:
     loop

   LOOP_LABEL:
     while condition loop

   LOOP_LABEL:
     for x in range(15 downto 0) loop

**Fix**

.. code-block:: vhdl

   LOOP_LABEL: loop

   LOOP_LABEL: while condition loop

   LOOP_LABEL: for x in range(15 downto 0) loop

loop_statement_100
##################

|phase_2| |error| |whitespace|

This rule checks that a single space exists between the **end** and **loop** keywords

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

loop_statement_103
##################

|phase_2| |error| |whitespace|

This rule checks if a label exists that a single space exists between the label and the colon.

**Violation**

.. code-block:: vhdl

     label: for index in 4 to 23 loop
     label    : for index in 0 to 100 loop

**Fix**

.. code-block:: vhdl

     label : for index in 4 to 23 loop
     label : for index in 0 to 100 loop

loop_statement_104
##################

|phase_2| |error| |whitespace|

This rule checks if a label exists that a single space exists after the colon.

**Violation**

.. code-block:: vhdl

     label :    for index in 4 to 23 loop
     label :  for index in 0 to 100 loop

**Fix**

.. code-block:: vhdl

     label : for index in 4 to 23 loop
     label : for index in 0 to 100 loop

loop_statement_201
##################

|phase_3| |error| |blank_line|

This rule checks for blank lines below the **loop** keyword.

Refer to `Configuring Blank Lines <configuring.html#configuring-blank-lines>`_ for options.

**Violation**

.. code-block:: vhdl

   loop
     a <= b;

**Fix**

.. code-block:: vhdl

   loop
     a <= b;

loop_statement_202
##################

|phase_3| |error| |blank_line|

This rule checks for blank lines or comments above the **end** keyword.

Refer to `Configuring Previous Line Rules <configuring.html#configuring-previous-line-rules>`_ for options.

**Violation**

.. code-block:: vhdl

   loop
     a <= b;
   end loop;

**Fix**

.. code-block:: vhdl

   loop
     a <= b;

   end loop;

loop_statement_203
##################

|phase_3| |error| |blank_line|

This rule checks for blank lines below the **end loop** keywords.

Refer to `Configuring Blank Lines <configuring.html#configuring-blank-lines>`_ for options.

**Violation**

.. code-block:: vhdl

   end loop;
   a <= b;

**Fix**

.. code-block:: vhdl

   end loop;

   a <= b;

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

loop_statement_302
##################

|phase_4| |error| |indent|

This rule checks the indentation of the **end** keyword.

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

loop_statement_503
##################

|phase_6| |error| |case| |case_label|

This rule checks the proper case of the label on a loop statement.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

     LABEL : for index in 4 to 23 loop
     Label : for index in 0 to 100 loop

**Fix**

.. code-block:: vhdl

     label : for index in 4 to 23 loop
     label : for index in 0 to 100 loop

loop_statement_504
##################

|phase_6| |error| |case| |case_label|

This rule checks the proper case of the end label on a loop statement.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

     end loop LABEL;
     end loop Label;

**Fix**

.. code-block:: vhdl

     end loop label;
     end loop label;

