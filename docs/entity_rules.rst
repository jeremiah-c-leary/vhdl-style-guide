Entity Rules
------------

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

