.. include:: icons.rst

Loop Statement Rules
--------------------

loop_statement_001
##################

|phase_1| |error|

This rule checks for the existence of the loop label.

Refer to the section `Configuring Optional Items <configuring.html#configuring-optional-items>`_ for options.

**Violation**

.. code-block:: vhdl

   loop

**Fix**

.. code-block:: vhdl

   LOOP_LABEL : loop

loop_statement_002
##################

|phase_1| |error|

This rule checks for the existence of the loop label after the **end loop** keywords.

Refer to the section `Configuring Optional Items <configuring.html#configuring-optional-items>`_ for options.

**Violation**

.. code-block:: vhdl

   end loop;

**Fix**

.. code-block:: vhdl

   end loop LOOP_LABEL;

loop_statement_003
##################

|phase_1| |error|

This rule checks the loop label and the **while**, **for** or **loop** keywords are on the same line.

**Violation**

.. code-block:: vhdl

   loop_label :
     loop

**Fix**

.. code-block:: vhdl

   loop_label : loop

loop_statement_004
##################

|phase_1| |error|

This rule checks for code after the **loop** keyword.

**Violation**

.. code-block:: vhdl

   loop a <= b;

**Fix**

.. code-block:: vhdl

   loop
     a <= b;

loop_statement_005
##################

|phase_1| |error|

This rule checks the **end** keyword is on it's own line.

**Violation**

.. code-block:: vhdl

   a <= b; end loop;

**Fix**

.. code-block:: vhdl

   a <= b;
   end loop;

loop_statement_006
##################

|phase_1| |error|

This rule checks the **end** keyword is on the same line as the **loop** keyword.

**Violation**

.. code-block:: vhdl

   end
   loop;

**Fix**

.. code-block:: vhdl

   end loop;

loop_statement_007
##################

|phase_1| |error|

This rule checks the **end loop** keyword is on the same line as the semicolon.

**Violation**

.. code-block:: vhdl

   end loop
   ;

**Fix**

.. code-block:: vhdl

   end loop;

loop_statement_200
##################

|phase_3| |error|

This rule checks for blank lines or comments above the **loop** label, **while** keyword, **for** keyword or **loop** keyword.

Refer to `Configuring Previous Line Rules <configuring.html#configuring-previous-line-rules>`_ for options.

The default style is :code:`no_code`.

**Violation**

.. code-block:: vhdl

   a <= b;
   while true

**Fix**

.. code-block:: vhdl

   a <= b;

   while true

loop_statement_201
##################

|phase_3| |error|

This rule checks for a blank line below the **loop** keyword.

Refer to the section `Configuring Blank Lines <configuring.html#configuring-blank-lines>`_ for options regarding comments.

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

|phase_3| |error|

This rule checks for blank lines or comments above the block label.

Refer to `Configuring Previous Line Rules <configuring.html#configuring-previous-line-rules>`_ for options.

**Violation**

.. code-block:: vhdl

   a <= b;
   block_label : block is

**Fix**

.. code-block:: vhdl

   a <= b;

   block_label : block is

loop_statement_203
##################

|phase_3| |error|

This rule checks for a blank line below the **end loop** keywords.

Refer to the section `Configuring Blank Lines <configuring.html#configuring-blank-lines>`_ for options regarding comments.

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

loop_statement_500
##################

|phase_6| |error|

This rule checks the label has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   LOOP_LABEL : loop

**Fix**

.. code-block:: vhdl

   loop_label : loop

loop_statement_501
##################

|phase_6| |error|

This rule checks the **loop** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   loop_label : LOOP

**Fix**

.. code-block:: vhdl

   loop_label : loop

loop_statement_502
##################

|phase_6| |error|

This rule checks the **end** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   END loop;

**Fix**

.. code-block:: vhdl

   end loop;

loop_statement_503
##################

|phase_6| |error|

This rule checks the **loop** keyword after **end** has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   end LOOP;

**Fix**

.. code-block:: vhdl

   end loop;

loop_statement_504
##################

|phase_6| |error|

This rule checks the ending loop label has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   end loop LOOP_LABEL;

**Fix**

.. code-block:: vhdl

   end loop loop_label;
