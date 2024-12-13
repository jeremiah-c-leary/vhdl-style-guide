.. include:: includes.rst

Case Generate Alternative Rules
-------------------------------

case_generate_alternative_300
#############################

The function of this rule has been superseded with comment indent updates and is handled by rule comment_010.

case_generate_alternative_500
#############################

|phase_6| |error| |case| |case_keyword|

This rule checks the *when* keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   WHEN choices =>

**Fix**

.. code-block:: vhdl

   when choices =>

case_generate_alternative_501
#############################

This rule has been deprecated and replaced with rule `choice_500 <choice_rules.html#choice-500>`_.
