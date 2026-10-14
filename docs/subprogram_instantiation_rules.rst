.. include:: includes.rst

Subprogram Instantiation Rules
------------------------------

subprogram_instantiation_001
############################

|phase_1| |error| |structure|

This rule checks the new subprogram identifier is on the same line as the **procedure** keyword.

**Violation**

.. code-block:: vhdl

   procedure
   my_proc is new my_generic_proc

**Fix**

.. code-block:: vhdl

   procedure my_proc is new my_generic_proc

subprogram_instantiation_002
############################

|phase_1| |error| |structure|

This rule checks the new subprogram identifier is on the same line as the **function** keyword.

**Violation**

.. code-block:: vhdl

   function
   my_func is new my_generic_func

**Fix**

.. code-block:: vhdl

   function my_func is new my_generic_func

subprogram_instantiation_003
############################

|phase_1| |error| |structure|

This rule checks the **is** keyword is on the same line as the new subprogram identifier.

**Violation**

.. code-block:: vhdl

   procedure my_proc
   is new my_generic_proc

**Fix**

.. code-block:: vhdl

   procedure my_proc is new my_generic_proc

subprogram_instantiation_004
############################

|phase_1| |error| |structure|

This rule checks the **new** keyword is on the same line as the **is** keyword.

**Violation**

.. code-block:: vhdl

   procedure my_proc is
   new my_generic_proc

**Fix**

.. code-block:: vhdl

   procedure my_proc is new my_generic_proc

subprogram_instantiation_005
############################

|phase_1| |error| |structure|

This rule checks the uninstantiated subprogram name is on the same line as the **new** keyword.

**Violation**

.. code-block:: vhdl

   procedure my_proc is new
   my_generic_proc

**Fix**

.. code-block:: vhdl

   procedure my_proc is new my_generic_proc

subprogram_instantiation_100
############################

|phase_2| |error| |whitespace|

This rule checks for a single space between the **procedure** keyword and the new subprogram identifier.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   procedure       my_proc is new my_generic_proc

**Fix**

.. code-block:: vhdl

   procedure my_proc is new my_generic_proc

subprogram_instantiation_101
############################

|phase_2| |error| |whitespace|

This rule checks for a single space between the **function** keyword and the new subprogram identifier.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   function       my_func is new my_generic_func

**Fix**

.. code-block:: vhdl

   function my_func is new my_generic_func

subprogram_instantiation_102
############################

|phase_2| |error| |whitespace|

This rule checks for a single space between the new subprogram identifier and the **is** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   procedure my_proc    is new my_generic_proc

**Fix**

.. code-block:: vhdl

   procedure my_proc is new my_generic_proc

subprogram_instantiation_103
############################

|phase_2| |error| |whitespace|

This rule checks for a single space between the **is** keyword and the **new** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   procedure my_proc is     new my_generic_proc

**Fix**

.. code-block:: vhdl

   procedure my_proc is new my_generic_proc

subprogram_instantiation_104
############################

|phase_2| |error| |whitespace|

This rule checks for a single space between **new** keyword and the uninstantiated subprogram name.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   procedure my_proc is new     my_generic_proc

**Fix**

.. code-block:: vhdl

   procedure my_proc is new my_generic_proc

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
