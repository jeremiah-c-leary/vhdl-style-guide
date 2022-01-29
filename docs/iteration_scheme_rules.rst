.. include:: icons.rst

Interation Scheme Rules
-----------------------

iteration_scheme_500
####################

|phase_6| |error| |case| |case_keyword|

This rule checks the **while** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   WHILE (condition) loop

**Fix**

.. code-block:: vhdl

   while (condition) loop

