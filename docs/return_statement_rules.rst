.. include:: includes.rst

Return Statement Rules
----------------------

return_statement_300
####################

|phase_4| |error| |indent|

This rule checks the indentation of the **return** keyword.

**Violation**

.. code-block:: vhdl

     return my_value;
     end function;

**Fix**

.. code-block:: vhdl

       return my_value;
     end function;

return_statement_500
####################

|phase_6| |error| |case| |case_keyword|

This rule checks the **return** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   RETURN my_value;

**Fix**

.. code-block:: vhdl

   return my_value;

