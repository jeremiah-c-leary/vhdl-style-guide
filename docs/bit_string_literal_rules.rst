.. include:: includes.rst

Bit String Literal Rules
------------------------

bit_string_literal_500
######################

|phase_6| |error| |case|

This rule checks the base specifier has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

    signal test : my_vector := X"FFF";


**Fix**

.. code-block:: vhdl

   signal test : my_vector := x"FFF";

bit_string_literal_501
######################

|phase_6| |error| |case|

This rule checks the bit value has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

    signal test : my_vector := x"FFF";


**Fix**

.. code-block:: vhdl

   signal test : my_vector := x"fff";
