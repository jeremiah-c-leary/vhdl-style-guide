Entity Specification Rules
--------------------------

Structural Rules (000 - 099)
############################

No rules identified.

Whitespacing Rules (100 - 199)
##############################

entity_specification_100
^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^

This rule checks for at least a single space before the :.

**Violation**

.. code-block:: vhdl

   attribute coordinate of comp_1: component is (0.0, 17.5);

   attribute coordinate of comp_1     : component is (0.0, 17.5);

**Fix**

.. code-block:: vhdl

   attribute coordinate of comp_1 : component is (0.0, 17.5);

   attribute coordinate of comp_1     : component is (0.0, 17.5);

Vertical Spacing Rules (200 - 299)
##################################

No rules have been identified.

Indentation Rules (300 - 399)
#############################

No rules have been identified.

Alignment Rules (400 - 499)
###########################

No rules have been identified.

Capitalization Rules (500 - 599)
################################

entity_specification_500
^^^^^^^^^^^^^^^^^^^^^^^^

This rule checks the **others** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   attribute coordinate of OTHERS : component is (0.0, 17.5);

**Fix**

.. code-block:: vhdl

   attribute coordinate of others : component is (0.0, 17.5);

entity_specification_501
^^^^^^^^^^^^^^^^^^^^^^^^

This rule checks the **all** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   attribute coordinate of ALL : component is (0.0, 17.5);

**Fix**

.. code-block:: vhdl

   attribute coordinate of all : component is (0.0, 17.5);

entity_specification_502
^^^^^^^^^^^^^^^^^^^^^^^^

This rule checks the *entity_designator* has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   attribute coordinate of COMP_1, COMP_2 : component is (0.0, 17.5);

**Fix**

.. code-block:: vhdl

   attribute coordinate of comp_1, comp_2 : component is (0.0, 17.5);

entity_specification_503
^^^^^^^^^^^^^^^^^^^^^^^^

This rule checks the *entity_class* has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring_case.html>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   attribute coordinate of comp_1 : COMPONENT is (0.0, 17.5);

**Fix**

.. code-block:: vhdl

   attribute coordinate of comp_1 : component is (0.0, 17.5);

Naming Convention Rules (600 - 699)
###################################

No rules have been identified.
