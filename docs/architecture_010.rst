architecture_010
################

This rule checks for the keyword *architecture* in the *end architecture* statement.
It is clearer to the reader to state what is ending.

**Violation**

.. code-block:: vhdl

   end ARCHITECTURE_NAME;

**Fix**

.. code-block:: vhdl

   end architecture ARCHITECTURE_NAME;

