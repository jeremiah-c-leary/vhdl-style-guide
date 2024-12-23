.. include:: includes.rst

Constrained Array Definition Rules
----------------------------------

constrained_array_definition_500
################################

|phase_6| |error| |case| |case_keyword|

This rule checks the **array** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   type t_u_array is ARRAY(1 downto 0) of unsigned;

**Fix**

.. code-block:: vhdl

   type t_u_array is array(1 downto 0) of unsigned;

constrained_array_definition_501
################################

|phase_6| |error| |case| |case_keyword|

This rule checks the **of** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   type t_u_array is ARRAY(1 downto 0) of unsigned;

**Fix**

.. code-block:: vhdl

   type t_u_array is array(1 downto 0) of unsigned;
