.. include:: icons.rst

Alias Declaration Rules
-----------------------

alias_declaration_500
#####################

|phase_6| |error| |case| |case_keyword|

This rule checks the **alias** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   ALIAS alias_designator is name;

**Fix**

.. code-block:: vhdl

   alias alias_designator is name;

