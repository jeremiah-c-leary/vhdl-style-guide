Generic Rules
-------------

generic_016
###########

This rule checks for multiple generics defined on a single line.
It is easier to comprehend the generic map if each generic is on it's own line.

**Violation**

.. code-block:: vhdl

  generic (
    WIDTH : std_logic := '0';DEPTH : std_logic := '1'
  );

**Fix**

.. code-block:: vhdl

  generic (
    WIDTH : std_logic := '0';
    DEPTH : std_logic := '1'
  );

