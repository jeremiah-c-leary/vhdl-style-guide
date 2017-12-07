Component Rules
---------------

component_019
#############

This rule checks for comments at the end of the port and generic assignments in component declarations.
These comments represent additional maintainence.
They will be out of sync with the entity at some point.
Refer to the entity for port types, port directions and purpose.

**Violation**

.. code-block:: vhdl

   WR_EN : in    std_logic;  -- Enables write to RAM
   RD_EN : out   std_logic; -- Enable reads from RAM

**Fix**

.. code-block:: vhdl

   WR_EN : in    std_logic;
   RD_EN : out   std_logic;

