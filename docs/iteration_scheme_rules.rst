.. include:: icons.rst

Interation Scheme Rules
-----------------------

iteration_scheme_100
####################

|phase_2| |error| |whitespace|

This rule checks that a single space exists after the **while** keyword.

**Violation**

.. code-block:: vhdl

   while(condition)

   while      (condition)

**Fix**

.. code-block:: vhdl

   while (condition)

   while (condition)

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

iteration_scheme_501
####################

|phase_6| |error| |case| |case_keyword|

This rule checks the **for** keyword has proper case.

Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

**Violation**

.. code-block:: vhdl

   FOR x in (31 downto 0) loop

**Fix**

.. code-block:: vhdl

   for x in (31 downto 0) loop

