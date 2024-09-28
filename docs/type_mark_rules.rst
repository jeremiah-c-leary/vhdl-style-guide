.. include:: includes.rst

Type Mark Rules
---------------

type_mark_500
#############

|phase_6| |error| |case| |case_name|

This rule checks that the name has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

  subtype my_subtype is MY_EXTERNAL_TYPE range 10 to 20;


**Fix**

.. code-block:: vhdl

  subtype my_subtype is my_external_type range 10 to 20;

