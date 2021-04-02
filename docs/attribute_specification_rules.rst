.. include:: icons.rst

Attribute Specification Rules
-----------------------------

Structural Rules (000 - 099)
############################

No rules have been identified.

Whitespacing Rules (100 - 199)
##############################

attribute_specification_100
^^^^^^^^^^^^^^^^^^^^^^^^^^^

|phase_2| |error|

This rule checks for a single space after the following attribute_specification elements:  **attribute** keyword, *attribute_designator*, **of** keyword and **is** keyword.

**Violation**

.. code-block:: vhdl

   attribute   coordinate   of   comp_1:component   is   (0.0, 17.5);

   attribute   coordinate   of   comp_1:component   is(0.0, 17.5);

**Fix**

.. code-block:: vhdl

   attribute coordinate of comp_1:component   is (0.0, 17.5);

   attribute coordinate of comp_1:component   is (0.0, 17.5);

attribute_specification_101
^^^^^^^^^^^^^^^^^^^^^^^^^^^

|phase_2| |error|

This rule checks for a single space before the **is** keyword.

**Violation**

.. code-block:: vhdl

   attribute coordinate of comp_1 : component   is (0.0, 17.5);

**Fix**

.. code-block:: vhdl

   attribute coordinate of comp_1 : component is (0.0, 17.5);

   attribute coordinate of comp_1 : component is (0.0, 17.5);

Vertical Spacing Rules (200 - 299)
##################################

No rules have been identified at this time.

Indentation Rules (300 - 399)
#############################

attribute_specification_300
^^^^^^^^^^^^^^^^^^^^^^^^^^^

|phase_4| |error|

This rule checks the indent of the **attribute** keyword.

**Violation**

.. code-block:: vhdl

   signal sig1 : std_logic;
      attribute coordinate of comp_1 : component is (0.0, 17.5);

**Fix**

.. code-block:: vhdl

   signal sig1 : std_logic;
   attribute coordinate of comp_1 : component is (0.0, 17.5);

Alignment Rules (400 - 499)
###########################

Alignment rules would be handled by the element using attributes.

Capitalization Rules (500 - 599)
################################

attribute_specification_500
^^^^^^^^^^^^^^^^^^^^^^^^^^^

|phase_6| |error|

This rule checks the **attribute** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   ATTRIBUTE coordinate of comp_1 : component is (0.0, 17.5);

**Fix**

.. code-block:: vhdl

   attribute coordinate of comp_1 : component is (0.0, 17.5);

attribute_specification_501
^^^^^^^^^^^^^^^^^^^^^^^^^^^

|phase_6| |error|

This rule checks the *attribute_designator* has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   attribute COORDINATE of comp_1 : component is (0.0, 17.5);

**Fix**

.. code-block:: vhdl

   attribute coordinate of comp_1 : component is (0.0, 17.5);

attribute_specification_502
^^^^^^^^^^^^^^^^^^^^^^^^^^^

|phase_6| |error|

This rule checks the **of** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   attribute coordinate OF comp_1 : component is (0.0, 17.5);

**Fix**

.. code-block:: vhdl

   attribute coordinate of comp_1 : component is (0.0, 17.5);

attribute_specification_503
^^^^^^^^^^^^^^^^^^^^^^^^^^^

|phase_6| |error|

This rule checks the **is** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   attribute coordinate of comp_1 : component IS (0.0, 17.5);

**Fix**

.. code-block:: vhdl

   attribute coordinate of comp_1 : component is (0.0, 17.5);

Naming Convention Rules (600 - 699)
###################################

No rules have been identified.
