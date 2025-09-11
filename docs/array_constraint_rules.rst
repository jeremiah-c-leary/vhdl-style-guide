.. include:: includes.rst

Array Constraint Rules
----------------------

array_constraint_100
####################

|phase_2| |error| |whitespace|

This rule checks for whitespace before the opening parenthesis.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

  subtype my_array3 is my_array2       (open)(7 downto 0);

**Fix**

.. code-block:: vhdl

  subtype my_array3 is my_array2(open)(7 downto 0);

array_constraint_500
####################

|phase_6| |error| |case| |case_keyword|

This rule checks the **open** keyword in array constraints has the proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   subtype t_my_array is t_array(OPEN)(t_range);


**Fix**

.. code-block:: vhdl

   subtype t_my_array is t_array(open)(t_range);
