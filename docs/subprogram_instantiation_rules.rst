.. include:: includes.rst

Subprogram Instantiation Rules
------------------------------

subprogram_instantiation_200
############################

|phase_3| |error| |blank_line|

This rule checks for blank lines below the subprogram instantiation.

|configuring_blank_lines_link|

The default style is :code:`no_blank_line`.

**Violation**

.. code-block:: vhdl

   procedure my_proc is new my_generic_proc

     generic map (

**Fix**

.. code-block:: vhdl

   procedure my_proc is new my_generic_proc
     generic map (

subprogram_instantiation_500
############################

|phase_6| |error| |case| |case_name|

This rule checks the instantiated package name has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   procedure MY_PROC is new my_generic_proc

**Fix**

.. code-block:: vhdl

   procedure my_proc is new my_generic_proc

subprogram_instantiation_501
############################

|phase_6| |error| |case| |case_keyword|

This rule checks the **is** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   procedure my_proc IS new my_generic_proc

**Fix**

.. code-block:: vhdl

   procedure my_proc is new my_generic_proc

subprogram_instantiation_502
############################

|phase_6| |error| |case| |case_keyword|

This rule checks the **new** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   procedure my_proc is NEW my_generic_proc

**Fix**

.. code-block:: vhdl

   procedure my_proc is new my_generic_proc

subprogram_instantiation_503
############################

|phase_6| |error| |case| |case_name|

This rule checks the uninstantiated subprogram name has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   procedure my_proc is new MY_GENERIC_PROC

**Fix**

.. code-block:: vhdl

   procedure my_proc is new my_generic_proc
