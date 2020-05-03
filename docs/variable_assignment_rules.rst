Variable Assignment Rules
-------------------------

variable_assignment_001
#######################

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

This rule checks the alignment of **:=** operators over multiple lines.

Following extra configurations are supported:

* :code:`if_control_statements_end_group`.
* :code:`case_control_statements_end_group`,


Refer to the section `Configuring Keyword Alignment Rules <configuring_keyword_alignment.html>`_ for information on changing the configurations.

**Violation**

.. code-block:: vhdl

     counter := 0;
     count := counter + 1;

**Fix**

.. code-block:: vhdl

     counter := 0;
     count   := counter + 1;

variable_assignment_006
#######################

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

