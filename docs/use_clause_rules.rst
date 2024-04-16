.. include:: includes.rst

Use Clause Rules
----------------

use_clause_500
##############

|phase_6| |error| |case| |case_name|

This rule checks the library name called out in the selected name has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   use IEEE.std_logic_1164.all;

   use my_LIB.all;

**Fix**

.. code-block:: vhdl

   use ieee.std_logic_1164.all;

   use my_lib.all;

use_clause_501
##############

|phase_6| |error| |case| |case_name|

This rule checks the package name called out in the selected name has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   use ieee.STD_LOGIC_1164.all;

**Fix**

.. code-block:: vhdl

   use ieee.std_logic_1164.all;

use_clause_502
##############

|phase_6| |error| |case| |case_name|

This rule checks the item name called out in the selected name has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   use my_lib.Increment;

**Fix**

.. code-block:: vhdl

   use my_lib.increment;

use_clause_503
##############

|phase_6| |error| |case| |case_keyword|

This rule checks the **all** keyword called out in the selected name has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   use ieee.std_logic_1164.ALL;

**Fix**

.. code-block:: vhdl

   use ieee.std_logic_1164.all;
