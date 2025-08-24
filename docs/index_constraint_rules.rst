.. include:: includes.rst

Index Constraint Rules
----------------------

index_constraint_100
####################

|phase_2| |error| |whitespace|

This rule checks for whitespace before the opening parenthesis.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

  subtype my_array3 is my_array2(open)         (7 downto 0);

**Fix**

.. code-block:: vhdl

  subtype my_array3 is my_array2(open)(7 downto 0);
