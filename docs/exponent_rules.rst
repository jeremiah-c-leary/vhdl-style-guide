.. include:: includes.rst

Exponent Rules
--------------

exponent_500
############

|phase_6| |error| |case| |case_keyword|

This rule checks the e keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

    12.5E-90
    6E57

**Fix**

.. code-block:: vhdl

    12.5e-90
    6e57
