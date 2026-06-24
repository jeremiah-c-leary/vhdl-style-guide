.. include:: includes.rst

Subprogram Kind Rules
---------------------

subprogram_kind_300
###################

|phase_4| |error| |indent|

This rule checks the indent of the **procedure** keyword.

**Violation**

.. code-block:: vhdl

   library ieee;

     procedure my_proc is new my_generic_proc

**Fix**

.. code-block:: vhdl

   library ieee;

   procedure my_proc is new my_generic_proc

subprogram_kind_301
###################

|phase_4| |error| |indent|

This rule checks the indent of the **function** keyword.

**Violation**

.. code-block:: vhdl

   library ieee;

     function my_func is new my_generic_func

**Fix**

.. code-block:: vhdl

   library ieee;

   function my_func is new my_generic_func

subprogram_kind_500
###################

|phase_6| |error| |case| |case_keyword|

This rule checks that the **procedure** keyword in subprogram kinds has the proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   end PROCEDURE parity;

   PROCEDURE my_proc is new my_generic_proc

**Fix**

.. code-block:: vhdl

   end procedure parity;

   procedure my_proc is new my_generic_proc

subprogram_kind_501
###################

|phase_6| |error| |case| |case_keyword|

This rule checks that the **function** keyword in subprogram kinds has the proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   end FUNCTION parity;

   FUNCTION my_func is new my_generic_func

**Fix**

.. code-block:: vhdl

   end function parity;

   function my_func is new my_generic_func
