.. include:: includes.rst

Exit Rules
----------

exit_statement_300
##################

|phase_4| |error| |indent|

This rule checks the indent of the **exit** keyword.

**Violation**

.. code-block:: vhdl

   end if;

     exit;

**Fix**

.. code-block:: vhdl

   end if;

   exit;

exit_statement_500
##################

|phase_6| |error| |case| |case_keyword|

This rule checks the **exit** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   EXIT when condition;

**Fix**

.. code-block:: vhdl

   exit when condition;

exit_statement_501
##################

|phase_6| |error| |case| |case_keyword|

This rule checks the **when** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   exit WHEN condition;

**Fix**

.. code-block:: vhdl

   exit when condition;
