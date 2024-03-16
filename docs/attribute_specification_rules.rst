.. include:: includes.rst

Attribute Specification Rules
-----------------------------

attribute_specification_100
###########################

|phase_2| |error| |whitespace|

This rule checks for a single space after the following attribute_specification elements:  **attribute** keyword, *attribute_designator*, **of** keyword and **is** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   attribute   coordinate   of   comp_1:component   is   (0.0, 17.5);

   attribute   coordinate   of   comp_1:component   is(0.0, 17.5);

**Fix**

.. code-block:: vhdl

   attribute coordinate of comp_1:component   is (0.0, 17.5);

   attribute coordinate of comp_1:component   is (0.0, 17.5);

attribute_specification_101
###########################

|phase_2| |error| |whitespace|

This rule checks for a single space before the **is** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   attribute coordinate of comp_1 : component   is (0.0, 17.5);

**Fix**

.. code-block:: vhdl

   attribute coordinate of comp_1 : component is (0.0, 17.5);

   attribute coordinate of comp_1 : component is (0.0, 17.5);

attribute_specification_300
###########################

|phase_4| |error| |indent|

This rule checks the indent of the **attribute** keyword.

**Violation**

.. code-block:: vhdl

   signal sig1 : std_logic;
      attribute coordinate of comp_1 : component is (0.0, 17.5);

**Fix**

.. code-block:: vhdl

   signal sig1 : std_logic;
   attribute coordinate of comp_1 : component is (0.0, 17.5);

attribute_specification_500
###########################

|phase_6| |error| |case| |case_keyword|

This rule checks the **attribute** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   ATTRIBUTE coordinate of comp_1 : component is (0.0, 17.5);

**Fix**

.. code-block:: vhdl

   attribute coordinate of comp_1 : component is (0.0, 17.5);

attribute_specification_501
###########################

|phase_6| |error| |case| |case_name|

This rule checks the *attribute_designator* has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   attribute COORDINATE of comp_1 : component is (0.0, 17.5);

**Fix**

.. code-block:: vhdl

   attribute coordinate of comp_1 : component is (0.0, 17.5);

attribute_specification_502
###########################

|phase_6| |error| |case| |case_keyword|

This rule checks the **of** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   attribute coordinate OF comp_1 : component is (0.0, 17.5);

**Fix**

.. code-block:: vhdl

   attribute coordinate of comp_1 : component is (0.0, 17.5);

attribute_specification_503
###########################

|phase_6| |error| |case| |case_keyword|

This rule checks the **is** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   attribute coordinate of comp_1 : component IS (0.0, 17.5);

**Fix**

.. code-block:: vhdl

   attribute coordinate of comp_1 : component is (0.0, 17.5);
