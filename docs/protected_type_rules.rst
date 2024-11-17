.. include:: includes.rst

Protected Type Rules
--------------------

protected_type_300
##################

|phase_4| |error| |indent|

This rule checks the indent of the end protected type declaration.

**Violation**

.. code-block:: vhdl

   type flag_pt is protected
        end protected;

**Fix**

.. code-block:: vhdl

   type flag_pt is protected
   end protected;

protected_type_500
##################

|phase_6| |error| |case| |case_keyword|

This rule checks the **protected** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   type sharedcounter is PROTECTED

**Fix**

.. code-block:: vhdl

   type sharedcounter is protected

protected_type_501
##################

|phase_6| |error| |case| |case_keyword|

This rule checks the **end** keyword in **end protected** has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   END protected sharedcounter;

**Fix**

.. code-block:: vhdl

   end protected sharedcounter;

protected_type_502
##################

|phase_6| |error| |case| |case_keyword|

This rule checks the **protected** keyword in **end protected** has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   end PROTECTED sharedcounter;

**Fix**

.. code-block:: vhdl

   end protected sharedcounter;
