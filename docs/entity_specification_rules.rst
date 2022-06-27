.. include:: includes.rst

Entity Specification Rules
--------------------------

entity_specification_100
########################

|phase_2| |error| |whitespace|

This rule checks for a single space after the colon.

|configuring_whitespace_rules_link|

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

|phase_2| |error| |whitespace|

This rule checks for at least a single space before the colon.

|configuring_whitespace_rules_link|

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

|phase_6| |error| |case| |case_keyword|

This rule checks the **others** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   attribute coordinate of OTHERS : component is (0.0, 17.5);

**Fix**

.. code-block:: vhdl

   attribute coordinate of others : component is (0.0, 17.5);

entity_specification_501
########################

|phase_6| |error| |case| |case_keyword|

This rule checks the **all** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   attribute coordinate of ALL : component is (0.0, 17.5);

**Fix**

.. code-block:: vhdl

   attribute coordinate of all : component is (0.0, 17.5);

entity_specification_502
########################

This rule has been deprecated.  The case of *entity_designator* should be enforced by other rules.

entity_specification_503
########################

|phase_6| |error| |case| |case_name|

This rule checks the *entity_class* has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   attribute coordinate of comp_1 : COMPONENT is (0.0, 17.5);

**Fix**

.. code-block:: vhdl

   attribute coordinate of comp_1 : component is (0.0, 17.5);

