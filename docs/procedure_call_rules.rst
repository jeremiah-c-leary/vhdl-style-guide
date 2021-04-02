.. include:: icons.rst

Procedure Call Rules
--------------------

These rules handle **procedure_call_statement** and **concurrent_procedure_call_statement** elements.

.. _procedure_call_structural_rules:

Structural Rules
################

procedure_call_001
^^^^^^^^^^^^^^^^^^

|phase_1| |error|

This rule checks for labels on procedure call statements.
Labels on procedure calls are optional and do not provide additional information.

**Violation**

.. code-block:: vhdl

   WR_EN_OUTPUT : WR_EN(parameter);

**Fix**

.. code-block:: vhdl

   WR_EN(parameter);

procedure_call_002
^^^^^^^^^^^^^^^^^^

|phase_1| |error|

This rule checks for labels on concurrent procedure call statements.
Labels on procedure calls are optional and do not provide additional information.

**Violation**

.. code-block:: vhdl

   WR_EN_OUTPUT : WR_EN(parameter);

**Fix**

.. code-block:: vhdl

   WR_EN(parameter);

.. _procedure_call_whitespacing_rules:

Whitespacing Rules
##################

procedure_call_100
^^^^^^^^^^^^^^^^^^

|phase_2| |error|

This rule checks for a single space between the following block elements:  label, label colon, **postponed** keyword and the *procedure* name.

**Violation**

.. code-block:: vhdl

   procedure_label   :    postponed   WR_EN(parameter);

**Fix**

.. code-block:: vhdl

   procedure_label : postponed WR_EN(parameter);

.. _procedure_call_vertical_spacing_rules:

Vertical Spacing Rules
######################

No rules have been identified at this time.

.. _procedure_call_indentation-rules:

Indentation Rules
#################

procedure_call_300
^^^^^^^^^^^^^^^^^^

|phase_4| |error|

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
^^^^^^^^^^^^^^^^^^

|phase_4| |error|

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
^^^^^^^^^^^^^^^^^^

|phase_4| |error|

This rule checks the indent of the *procedure* name.

**Violation**

.. code-block:: vhdl

   a <= b;

     WR_EN(parameter);

**Fix**

.. code-block:: vhdl

   a <= b;

   WR_EN(parameter);

.. _procedure_call_alignment_rules:

Alignment Rules
###############

No rules have been identified at this time.

.. _procedure_call_capitalization_rules:

Capitalization Rules
####################

procedure_call_500
^^^^^^^^^^^^^^^^^^

|phase_6| |error|

This rule checks the label has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   PROCEDURE_CALL_LABEL : WR_EN(paremeter);

**Fix**

.. code-block:: vhdl

   procedure_call_label : WR_EN(paremeter);

procedure_call_501
^^^^^^^^^^^^^^^^^^

|phase_6| |error|

This rule checks the **postponed** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   POSTPONED WR_EN(parameter)

**Fix**

.. code-block:: vhdl

   postponed WR_EN(parameter)

.. _procedure_call_naming_convention_rules:

Naming Convention Rules
#######################

No rules have been identified at this time.
