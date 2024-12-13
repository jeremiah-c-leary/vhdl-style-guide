.. include:: includes.rst

Choice Rules
------------

choice_500
##########

|phase_6| |error| |case| |case_keyword|

This rule checks the **others** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

    '0' when OTHERS;

**Fix**

.. code-block:: vhdl

   '0' when others;
