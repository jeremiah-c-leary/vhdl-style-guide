.. include:: icons.rst

Wait Rules
----------

wait_001
########

|phase_4| |error| |indent|

This rule checks for indentation of the **wait** keyword.
Proper indentation enhances comprehension.

**Violation**

.. code-block:: vhdl

   begin

       wait for 10ns;
    wait on a,b;
          wait until a = '0';

**Fix**

.. code-block:: vhdl

   begin

     wait for 10ns;
     wait on a,b;
     wait until a = '0';

