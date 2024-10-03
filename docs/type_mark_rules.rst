.. include:: includes.rst

Type Mark Rules
---------------

type_mark_500
#############

|phase_6| |error| |case| |case_name|

This rule checks that the type name has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

  signal s_my_subtype : MY_EXTERNAL_SUBTYPE;

**Fix**

.. code-block:: vhdl

  signal s_my_subtype : my_external_subtype;
