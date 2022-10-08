.. include:: includes.rst

Variable Assignment Rules
-------------------------

variable_assignment_001
#######################

|phase_4| |error| |indent|

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

|phase_2| |error| |whitespace|

This rule checks for a single space after the assignment.

|configuring_whitespace_rules_link|

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

|phase_2| |error| |whitespace|

This rule checks for at least a single space before the assignment.

|configuring_whitespace_rules_link|

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

|phase_5| |error| |alignment|

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

|phase_2| |error| |structure|

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

variable_assignment_007
#######################

|phase_1| |error| |structure|

This rule checks the structure of simple and conditional variable assignments.

|configuring_multiline_structure_rules_link|

**Violation**

.. code-block:: vhdl

   wr_en :=
     '0' when q_wr_en = '1' else
            '1';

   w_foo :=
     I_FOO when ((I_BAR = '1') and
                        (I_CRUFT = '1')) else
            '0';

**Fix**

.. code-block:: vhdl

   wr_en := '0' when q_wr_en = '1' else
            '1';

   w_foo := I_FOO when ((I_BAR = '1') and
                        (I_CRUFT = '1')) else
            '0';

variable_assignment_008
#######################

|phase_1| |error| |structure|

This rule checks the structure of multiline variable assignments that contain arrays.

|configuring_multiline_structure_rules_link|

**Violation**

.. code-block:: vhdl

   wr_data := (0, 65535, 32768);

**Fix**

.. code-block:: vhdl

   wr_data :=
   (
     0,
     65535,
     32768
   );

