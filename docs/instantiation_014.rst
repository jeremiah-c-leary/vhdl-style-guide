instantiation_014
#################

This rule checks for the closing parenthesis *);* on generic maps are on their own line.
Having the parenthesis on it's own line makes the deliniation clearer between the generic map and the port map.

**Violation**

.. code-block:: vhdl

   INSTANCE_NAME : ENTITY_NAME
     generic_map (
       GENERIC_1 => 0,
       GENERIC_2 => TRUE,
       GENERIC_3 => FALSE);

**Fix**

.. code-block:: vhdl

   INSTANCE_NAME : ENTITY_NAME
     generic_map (
       GENERIC_1 => 0,
       GENERIC_2 => TRUE,
       GENERIC_3 => FALSE
     );

