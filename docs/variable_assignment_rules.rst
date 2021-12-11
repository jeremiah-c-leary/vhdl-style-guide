.. include:: icons.rst

Variable Assignment Rules
-------------------------

variable_assignment_001
#######################

|phase_4| |error|

This rule checks the indent of a variable assignment.

**Violation**

.. code-block:: vhdl

   proc : process () is
   begin

       counter := 0;
   count := counter + 1;


**Fix**

.. code-block:: vhdl

   proc : process () is
   begin

     counter := 0;
     count   := counter + 1;


variable_assignment_002
#######################

|phase_2| |error|

This rule checks for a single space after the assignment.

**Violation**

.. code-block:: vhdl

     counter :=0;
     count   :=     counter + 1;

**Fix**

.. code-block:: vhdl

     counter := 0;
     count   := counter + 1;

variable_assignment_003
#######################

|phase_2| |error|

This rule checks for at least a single space before the assignment.

**Violation**

.. code-block:: vhdl

     counter:= 0;
     count := counter + 1;

**Fix**

.. code-block:: vhdl

     counter := 0;
     count := counter + 1;

variable_assignment_004
#######################

|phase_4| |error|

This rule checks the alignment of multiline variable assignments.

**Violation**

.. code-block:: vhdl

     counter := 1 + 4 + 10 + 25 +
          30 + 35;

**Fix**

.. code-block:: vhdl

     counter := 1 + 4 + 10 + 25 +
                30 + 35;

variable_assignment_005
#######################

This rule has been deprecated and replaced with rule `process_400 <process_rules.html#process-400>`_.

variable_assignment_006
#######################

|phase_2| |error|

This rule checks for comments in multiline variable assignments.

**Violation**

.. code-block:: vhdl

     counter := 1 + 4 + 10 + 25 +
                -- Add in more stuff
                30 + 35;

**Fix**

.. code-block:: vhdl

     counter := 1 + 4 + 10 + 25 +
                30 + 35;

