.. include:: includes.rst

Procedure Call Rules
--------------------

These rules handle **procedure_call_statement** and **concurrent_procedure_call_statement** productions.

.. _procedure_call_structural_rules:

procedure_call_001
##################

|phase_1| |error| |structure|

This rule checks for labels on procedure call statements.
Labels on procedure calls are optional and do not provide additional information.

**Violation**

.. code-block:: vhdl

   WR_EN_OUTPUT : WR_EN(parameter);

**Fix**

.. code-block:: vhdl

   WR_EN(parameter);

procedure_call_002
##################

|phase_1| |error| |structure|

This rule checks for labels on concurrent procedure call statements.
Labels on procedure calls are optional and do not provide additional information.

**Violation**

.. code-block:: vhdl

   WR_EN_OUTPUT : WR_EN(parameter);

**Fix**

.. code-block:: vhdl

   WR_EN(parameter);

procedure_call_003
##################

|phase_1| |error| |structure|

This rule checks the structure of procedure calls.

|configuring_multiline_procedure_call_statement_rules_link|

**Violation**

.. code-block:: vhdl

   connect_ports(port_1 => data, port_2 => enable, port_3 => overflow, port_4 => underflow);

**Fix**

.. code-block:: vhdl

   connect_ports(
     port_1 => data,
     port_2 => enable,
     port_3 => overflow,
     port_4 => underflow
   );

.. _procedure_call_whitespacing_rules:

procedure_call_100
##################

|phase_2| |error| |whitespace|

This rule checks for a single space between the following block elements:  label, label colon, **postponed** keyword and the *procedure* name.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   procedure_label   :    postponed   WR_EN(parameter);

**Fix**

.. code-block:: vhdl

   procedure_label : postponed WR_EN(parameter);

procedure_call_101
##################

|phase_2| |error| |whitespace|

This rule checks for a single space after the **=>** operator in procedure calls.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   connect_ports(
     port_1 =>    data,
     port_2 =>enable,
     port_3 =>  overflow,
     port_4 => underflow
   );

**Fix**

.. code-block:: vhdl

   connect_ports(
     port_1 => data,
     port_2 => enable,
     port_3 => overflow,
     port_4 => underflow
   );

procedure_call_300
##################

|phase_4| |error| |indent|

This rule checks the indent of the procedure_call label.

**Violation**

.. code-block:: vhdl

   a <= b;

     procedure_label : WR_EN(parameter);

**Fix**

.. code-block:: vhdl

   a <= b;

   procedure_label : WR_EN(parameter);

procedure_call_301
##################

|phase_4| |error| |indent|

This rule checks the indent of the **postponed** keyword if it exists..

**Violation**

.. code-block:: vhdl

   a <= b;

     postponed WR_EN(parameter);

**Fix**

.. code-block:: vhdl

   a <= b;

   postponed WR_EN(parameter);

procedure_call_302
##################

|phase_4| |error| |indent|

This rule checks the indent of the *procedure* name.

**Violation**

.. code-block:: vhdl

   a <= b;

     WR_EN(parameter);

**Fix**

.. code-block:: vhdl

   a <= b;

   WR_EN(parameter);

procedure_call_400
##################

|phase_5| |error| |alignment|

This rule checks the alignment of multiline procedure calls.

|configuring_multiline_indent_rules_link|

**Violation**

.. code-block:: vhdl

   connect_ports(port_1, port_2, port_3,
         port_4, port_5,
                      port_6, port_7);

**Fix**

.. code-block:: vhdl

   connect_ports(port_1, port_2, port_3,
                 port_4, port_5,
                 port_6, port_7);

procedure_call_401
##################

|phase_5| |error| |alignment|

This rule checks the alignment of :code:`=>` keywords in procedure calls.

|configuring_keyword_alignment_rules_link|

**Violation**

.. code-block:: vhdl

   connect_ports(
     port_1=> data,
     port_2 => enable,
     port_3    => overflow,
     port_4  => underflow
   );

**Fix**

.. code-block:: vhdl

   connect_ports(
     port_1 => data,
     port_2 => enable,
     port_3 => overflow,
     port_4 => underflow
   );

procedure_call_500
##################

|phase_6| |error| |case| |case_label|

This rule checks the label has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   PROCEDURE_CALL_LABEL : WR_EN(paremeter);

**Fix**

.. code-block:: vhdl

   procedure_call_label : WR_EN(paremeter);

procedure_call_501
##################

|phase_6| |error| |case| |case_keyword|

This rule checks the **postponed** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   POSTPONED WR_EN(parameter)

**Fix**

.. code-block:: vhdl

   postponed WR_EN(parameter)

