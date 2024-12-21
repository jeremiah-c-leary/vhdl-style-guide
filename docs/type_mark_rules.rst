.. include:: includes.rst

Type Mark Rules
---------------

type_mark_500
#############

|phase_6| |error| |case| |case_name|

This rule checks that the type marks without declarations in the current file have proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

  signal my_sig : MY_TYPE_MARK;

**Fix**

.. code-block:: vhdl

  signal my_sig : my_type_mark;
