entity_019
##########

This rule checks for the entity name in the *end entity* statement.
It is clearer to the reader to state which entity the end statement is closing.

**Violation**

.. code-block:: vhdl

   end entity;

**Fix**

.. code-block:: vhdl

   end entity ENTITY_NAME;

