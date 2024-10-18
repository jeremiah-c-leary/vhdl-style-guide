.. include:: includes.rst

Next Statement Rules
--------------------

next_statement_300
##################

|phase_4| |error| |indent|

This rule checks the indentation of the **next** keyword.

**Violation**

.. code-block:: vhdl

     next when condition;
     end function;

**Fix**

.. code-block:: vhdl

       next when condition;
     end function;

next_statement_500
##################

|phase_6| |error| |case| |case_keyword|

This rule checks the **next** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   NEXT when condition;

**Fix**

.. code-block:: vhdl

   next when condition;

next_statement_501
##################

|phase_6| |error| |case| |case_keyword|

This rule checks the **when** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   next WHEN condition;

**Fix**

.. code-block:: vhdl

   next when condition;
