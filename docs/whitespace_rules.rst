Whitespace Rules
----------------

whitespace_008
##############

This rule checks for spaces after the **std_logic_vector** keyword.

**Violation**

.. code-block:: vhdl

   signal data    : std_logic_vector (7 downto 0);
   signal counter : std_logic_vector    (7 downto 0);

**Fix**

.. code-block:: vhdl

   signal data    : std_logic_vector(7 downto 0);
   signal counter : std_logic_vector(7 downto 0);

