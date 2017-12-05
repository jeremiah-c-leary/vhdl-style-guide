entity_015
##########

This rule checks for the keyword *entity* in the *end entity* statement.
It is clearer to the reader to state what is ending.

**Violation**

.. code-block:: vhdl

   end ENTITY_NAME;

   end;

**Fix**

.. code-block:: vhdl

   end entity ENTITY_NAME;

   end entity;

