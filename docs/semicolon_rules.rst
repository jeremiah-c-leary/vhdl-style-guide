Semicolon Rules
---------------

These rules cover issues with semicolons.

semicolon_001
#############

This rule checks for multiple consecutive semicolons.

**Violation**

.. code-block:: vhdl

   sig1 <= sig2;;;;

**Fix**

.. code-block:: vhdl

   sig1 <= sig2;
