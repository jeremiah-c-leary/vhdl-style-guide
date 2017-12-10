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

generic_017
###########

This rule checks the generic type is lowercase.

**Violation**

.. code-block:: vhdl

  generic (
    WIDTH : STD_LOGIC := '0';
    DEPTH : Std_logic := '1'
  );


**Fix**

.. code-block:: vhdl

  generic (
    WIDTH : std_logic := '0';
    DEPTH : std_logic := '1'
  );


