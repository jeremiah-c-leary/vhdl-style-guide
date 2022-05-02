.. include:: includes.rst

Report Statement Rules
----------------------

report_statement_001
####################

|phase_1| |error| |structure|

This rule removes labels on report_statement_statements.

**Violation**

.. code-block:: vhdl

    REPORT_LABEL : report "FIFO width is limited to 16 bits.";

**Fix**

.. code-block:: vhdl

    report "FIFO width is limited to 16 bits.";

report_statement_002
####################

|phase_1| |error| |structure|

This rule checks the **severity** keyword is on its own line.

**Violation**

.. code-block:: vhdl

    report "FIFO width is limited to 16 bits." severity FAILURE;

**Fix**

.. code-block:: vhdl

    report "FIFO width is limited to 16 bits."
      severity FAILURE;

report_statement_100
####################

|phase_2| |error| |whitespace|

This rule checks for a single space after the **report** keyword.

**Violation**

.. code-block:: vhdl

    report     "FIFO width is limited to 16 bits.";

**Fix**

.. code-block:: vhdl

    report "FIFO width is limited to 16 bits.";

report_statement_101
####################

|phase_2| |error| |whitespace|

This rule checks for a single space after the **severity** keyword.

**Violation**

.. code-block:: vhdl

    report "FIFO width is limited to 16 bits."
      severity    FAILURE;

**Fix**

.. code-block:: vhdl

    report "FIFO width is limited to 16 bits."
      severity FAILURE;

report_statement_300
####################

|phase_4| |error| |indent|

This rule checks indent of multiline report statements.

**Violation**

.. code-block:: vhdl

    report "FIFO width is limited to 16 bits."
            severity FAILURE;

**Fix**

.. code-block:: vhdl

    report "FIFO width is limited to 16 bits."
      severity FAILURE;

report_statement_400
####################

|phase_5| |error| |alignment|

This rule checks the alignment of the report expressions.

.. NOTE:: There is a configuration option **alignment** which changes the indent location of multiple lines.

alignment set to 'report' (Default)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Violation**

.. code-block:: vhdl

   report "FIFO width is limited" &
   " to 16 bits."
     severity FAILURE;

**Fix**

.. code-block:: vhdl

   report "FIFO width is limited" &
          " to 16 bits."
     severity FAILURE;

alignment set to 'left'
^^^^^^^^^^^^^^^^^^^^^^^

**Violation**

.. code-block:: vhdl

   report "FIFO width is limited" &
   " to 16 bits."
     severity FAILURE;

**Fix**

.. code-block:: vhdl

     report "FIFO width is limited" &
         " to 16 bits."
       severity FAILURE;

report_statement_500
####################

|phase_6| |error| |case| |case_keyword|

This rule checks the **report** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

    REPORT "FIFO width is limited to 16 bits."
      severity FAILURE;

.. code-block:: vhdl

    report "FIFO width is limited to 16 bits."
      severity FAILURE;

report_statement_501
####################

|phase_6| |error| |case| |case_keyword|

This rule checks the **severity** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

    report "FIFO width is limited to 16 bits."
      SEVERITY FAILURE;

.. code-block:: vhdl

    report "FIFO width is limited to 16 bits."
      severity FAILURE;

