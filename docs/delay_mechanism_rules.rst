.. include:: includes.rst

Delay Mechanism Rules
---------------------

delay_mechanism_500
###################

|phase_6| |error| |case| |case_keyword|

This rule checks the *transport* keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   a <= TRANSPORT 1 after 10 ns;

**Fix**

.. code-block:: vhdl

   a <= transport 1 after 10 ns;

delay_mechanism_501
###################

|phase_6| |error| |case| |case_keyword|

This rule checks the *inertial* keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   a <= INERTIAL 1 after 10 ns;

**Fix**

.. code-block:: vhdl

   a <= inertial 1 after 10 ns;

delay_mechanism_502
###################

|phase_6| |error| |case| |case_keyword|

This rule checks the *reject* keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   a <= REJECT 2ns inertial 1 after 10 ns;

**Fix**

.. code-block:: vhdl

   a <= reject 2ns inertial 1 after 10 ns;
