Assert Rules
------------

assert_001
##########

This rule checks alignment of multiline assert statements.

**Violation**

.. code-block:: vhdl

   assert WIDTH > 16
        report "FIFO witdth is limited to 16 bits."
    severity FAILURE;

**Fix**

.. code-block:: vhdl

   assert WIDTH > 16
   report "FIFO witdth is limited to 16 bits."
   severity FAILURE;
