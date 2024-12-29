.. include:: includes.rst

Unbounded Array Definition Rules
--------------------------------

unbounded_array_definition_500
##############################

|phase_6| |error| |case| |case_keyword|

This rule checks the **array** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   type t_u_array_unconstrained is ARRAY(natural range <>) of unsigned;

**Fix**

.. code-block:: vhdl

   type t_u_array_unconstrained is array(natural range <>) of unsigned;

unbounded_array_definition_501
##############################

|phase_6| |error| |case| |case_keyword|

This rule checks the **of** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   type t_u_array_unconstrained is array(natural range <>) OF unsigned;

**Fix**

.. code-block:: vhdl

   type t_u_array_unconstrained is array(natural range <>) of unsigned;
