.. include:: includes.rst

Null Statement Rules
--------------------

null_statement_300
##################

|phase_4| |error| |indent|

This rule checks the indentation of the **null** keyword.

**Violation**

.. code-block:: vhdl

     null;
     end loop;

**Fix**

.. code-block:: vhdl

       null;
     end loop;

null_statement_301
##################

|phase_4| |error| |indent|

This rule checks the indentation of the label.

**Violation**

.. code-block:: vhdl

     null_label : null;
     end loop;

**Fix**

.. code-block:: vhdl

       null_label : null;
     end loop;

null_statement_500
##################

|phase_6| |error| |case| |case_keyword|

This rule checks the **null** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   NULL;

**Fix**

.. code-block:: vhdl

   null;
