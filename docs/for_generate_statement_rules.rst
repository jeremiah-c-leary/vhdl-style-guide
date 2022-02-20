.. include:: includes.rst

For Generate Statement Rules
----------------------------

for_generate_statement_500
##########################

|phase_6| |error| |case| |case_keyword|

This rule checks the *for* keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   FOR x in range (3 downto 0) generate

**Fix**

.. code-block:: vhdl

   for x in range (3 downto 0) generate

for_generate_statement_501
##########################

|phase_6| |error| |case| |case_keyword|

This rule checks the *generate* keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   for x in range (3 downto 0) GENERATE

**Fix**

.. code-block:: vhdl

   for x in range (3 downto 0) generate

