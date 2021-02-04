Procedure Call Rules
--------------------

These rules handle **procedure_call_statement** and **concurrent_procedure_call_statement** elements.

Structural Rules
################

procedure_call_001
^^^^^^^^^^^^^^^^^^

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

This rule checks for labels on concurrent procedure call statements.
Labels on procedure calls are optional and do not provide additional information.

**Violation**

.. code-block:: vhdl

   WR_EN_OUTPUT : WR_EN(parameter);

**Fix**

.. code-block:: vhdl

   WR_EN(parameter);

Whitespacing Rules
##################

procedure_call_100
^^^^^^^^^^^^^^^^^^

This rule checks for a single space between the following block elements:  label, label colon, **postponed** keyword and the *procedure*_name.

**Violation**

.. code-block:: vhdl

   procedure_label   :    postponed   WR_EN(parameter);

**Fix**

.. code-block:: vhdl

   procedure_label : postponed WR_EN(parameter);

Vertical Spacing Rules
######################

No rules have been identified at this time.

Indentation Rules
#################

procedure_call_300
^^^^^^^^^^^^^^^^^^

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

This rule checks the indent of the *procedure*_name.

**Violation**

.. code-block:: vhdl

   a <= b;

     WR_EN(parameter);

**Fix**

.. code-block:: vhdl

   a <= b;

   WR_EN(parameter);

Alignment Rules
###############

No rules have been identified at this time.

Captialization Rules
####################

procedure_call_500
^^^^^^^^^^^^^^^^^^

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

This rule checks the **postponed** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   POSTPONED WR_EN(parameter)

**Fix**

.. code-block:: vhdl

   postponed WR_EN(parameter)

Naming Convention Rules
#######################

No rules have been identified at this time.
