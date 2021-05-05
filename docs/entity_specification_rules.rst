.. include:: icons.rst

Entity Specification Rules
--------------------------

entity_specification_100
########################

|phase_2| |error|

This rule checks for a single space after the colon.

**Violation**

.. code-block:: vhdl

   attribute coordinate of comp_1 :component is (0.0, 17.5);
   attribute coordinate of comp_1 :    component is (0.0, 17.5);

**Fix**

.. code-block:: vhdl

   attribute coordinate of comp_1 : component is (0.0, 17.5);
   attribute coordinate of comp_1 : component is (0.0, 17.5);

entity_specification_101
########################

|phase_2| |error|

This rule checks for at least a single space before the colon.

**Violation**

.. code-block:: vhdl

   attribute coordinate of comp_1: component is (0.0, 17.5);

   attribute coordinate of comp_1     : component is (0.0, 17.5);

**Fix**

.. code-block:: vhdl

   attribute coordinate of comp_1 : component is (0.0, 17.5);

   attribute coordinate of comp_1     : component is (0.0, 17.5);

entity_specification_500
########################

|phase_6| |error|

This rule checks the **others** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   attribute coordinate of OTHERS : component is (0.0, 17.5);

**Fix**

.. code-block:: vhdl

   attribute coordinate of others : component is (0.0, 17.5);

entity_specification_501
########################

|phase_6| |error|

This rule checks the **all** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   attribute coordinate of ALL : component is (0.0, 17.5);

**Fix**

.. code-block:: vhdl

   attribute coordinate of all : component is (0.0, 17.5);

entity_specification_502
########################

|phase_6| |error|

This rule checks the *entity_designator* has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   attribute coordinate of COMP_1, COMP_2 : component is (0.0, 17.5);

**Fix**

.. code-block:: vhdl

   attribute coordinate of comp_1, comp_2 : component is (0.0, 17.5);

entity_specification_503
########################

|phase_6| |error|

This rule checks the *entity_class* has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   attribute coordinate of comp_1 : COMPONENT is (0.0, 17.5);

**Fix**

.. code-block:: vhdl

   attribute coordinate of comp_1 : component is (0.0, 17.5);
