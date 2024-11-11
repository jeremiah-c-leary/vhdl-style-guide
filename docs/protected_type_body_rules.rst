.. include:: includes.rst

Protected Type Body Rules
-------------------------

protected_type_body_500
#######################

|phase_6| |error| |case| |case_keyword|

This rule checks the **protected** keyword in **protected body** has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   type sharedcounter is PROTECTED body

**Fix**

.. code-block:: vhdl

   type sharedcounter is protected body

protected_type_body_501
#######################

|phase_6| |error| |case| |case_keyword|

This rule checks the **body** keyword in **protected body** has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   type sharedcounter is protected BODY

**Fix**

.. code-block:: vhdl

   type sharedcounter is protected body

protected_type_body_502
#######################

|phase_6| |error| |case| |case_keyword|

This rule checks the **end** keyword in **end protected body** has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   END protected body sharedcounter;

**Fix**

.. code-block:: vhdl

   end protected body sharedcounter;

protected_type_body_503
#######################

|phase_6| |error| |case| |case_keyword|

This rule checks the **protected** keyword in **end protected body** has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   end PROTECTED body sharedcounter;

**Fix**

.. code-block:: vhdl

   end protected body sharedcounter;

protected_type_body_504
#######################

|phase_6| |error| |case| |case_keyword|

This rule checks the **body** keyword in **end protected body** has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   end protected BODY sharedcounter;

**Fix**

.. code-block:: vhdl

   end protected body sharedcounter;
