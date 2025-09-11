.. include:: includes.rst

Case Generate Statement Rules
-----------------------------

case_generate_statement_100
###########################

|phase_2| |error| |whitespace|

This rule checks for a single space after the **case** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   case    data generate


**Fix**

.. code-block:: vhdl

   case data generate

case_generate_statement_101
###########################

|phase_2| |error| |whitespace|

This rule checks for a single space before the **generate** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   case data    generate

**Fix**

.. code-block:: vhdl

   case data generate

case_generate_statement_200
###########################

|phase_3| |error| |blank_line|

This rule checks for blank lines or comments above the **end** keyword.

|configuring_blank_lines_link|

**Violation**

.. code-block:: vhdl

     when others =>
       null;
   end generate;

**Fix**

.. code-block:: vhdl

     when others =>
       null;

   end generate;

case_generate_statement_400
###########################

|phase_5| |disabled| |error| |alignment|

This rule checks the *=>* are aligned in case_generate_alternatives.

.. NOTE:: The default configuration is :code:`compact_alignment`.

|configuring_keyword_alignment_rules_link|

**Violation**

.. code-block:: vhdl

   gc : case I generate
     when 1 =>
     when n_order =>
     when others =>
   end generate gc;

**Fix**

.. code-block:: vhdl

   gc : case I generate
     when 1       =>
     when n_order =>
     when others  =>
   end generate gc;

case_generate_statement_500
###########################

|phase_6| |error| |case| |case_keyword|

This rule checks the **case** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   CASE expression generate

**Fix**

.. code-block:: vhdl

   case expression generate

case_generate_statement_501
###########################

|phase_6| |error| |case| |case_keyword|

This rule checks the **generate** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   case expression GENERATE

**Fix**

.. code-block:: vhdl

   case expression generate
