.. include:: icons.rst

Exit Rules
----------

exit_statement_300
##################

|phase_4| |error|

This rule checks the indent of the **exit** keyword.

**Violation**

.. code-block:: vhdl

   end if;

     exit;

**Fix**

.. code-block:: vhdl

   end if;

   exit;
