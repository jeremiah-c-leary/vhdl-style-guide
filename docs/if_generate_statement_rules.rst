.. include:: includes.rst

If Generate Statement Rules
---------------------------

if_generate_statement_300
#########################

|phase_4| |error| |indent|

This rule checks the indent of the *elsif* keyword.

**Violation**

.. code-block:: vhdl

   ram_array : if condition generate
      elsif condition generate
   end generate;

**Fix**

.. code-block:: vhdl

   ram_array : if condition generate
   elsif condition generate
   end generate;

if_generate_statement_301
#########################

|phase_4| |error| |indent|

This rule checks the indent of the *else* keyword.

**Violation**

.. code-block:: vhdl

   ram_array : if condition generate
      else
   end generate;

**Fix**

.. code-block:: vhdl

   ram_array : if condition generate
   else
   end generate;

if_generate_statement_500
#########################

|phase_6| |error| |case| |case_keyword|

This rule checks the *if* keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   IF condition generate

**Fix**

.. code-block:: vhdl

   if condition generate

if_generate_statement_501
#########################

|phase_6| |error| |case| |case_keyword|

This rule checks the *generate* keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   if condition GENERATE
   elsif condition GENERATE
   else GENERATE

**Fix**

.. code-block:: vhdl

   if condition generate
   elsif condition generate
   else generate

if_generate_statement_502
#########################

|phase_6| |error| |case| |case_keyword|

This rule checks the *elsif* keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   ELSIF condition generate

**Fix**

.. code-block:: vhdl

   elsif condition generate

if_generate_statement_503
#########################

|phase_6| |error| |case| |case_keyword|

This rule checks the *else* keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   ELSE generate

**Fix**

.. code-block:: vhdl

   else generate
