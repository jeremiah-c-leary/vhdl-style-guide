.. include:: icons.rst

With Rules
----------

with_001
########

|phase_1| |error|

This rule checks for **with** statements.

**Violation**

.. code-block:: vhdl

   with buttons select

**Fix**

Refactor **with** statement into a process.

