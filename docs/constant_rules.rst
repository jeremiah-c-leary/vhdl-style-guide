Constant Rules
--------------

constant_010
############

This rule checks for at least a single space before the := keyword in constant declarations.
Having a space makes it clearer where the assignment occurs on the line.

**Violation**

.. code-block:: vhdl

   constant size integer:= 1;

**Fix**

.. code-block:: vhdl

   constant size integer := 1;

