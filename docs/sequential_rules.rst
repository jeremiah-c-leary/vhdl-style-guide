Sequential Rules
----------------

sequential_001
##############

This rule checks the indent of sequential statements.

**Violation**

.. code-block:: vhdl

   begin

       wr_en <= '1';
   rd_en <= '0';

**Fix**

.. code-block:: vhdl

   begin

     wr_en <= '1';
     rd_en <= '0';

sequential_002
##############

This rule checks for a single space after the **<=** operator.

**Violation**

.. code-block:: vhdl

   wr_en <=     '1';
   rd_en <='0';

**Fix**

.. code-block:: vhdl

   wr_en <= '1';
   rd_en <= '0';

sequential_003
##############

This rule checks for at least a single space before the **<=** operator.

**Violation**

.. code-block:: vhdl

   wr_en<= '1';
   rd_en   <= '0';

**Fix**

.. code-block:: vhdl

   wr_en <= '1';
   rd_en   <= '0';

sequential_004
##############

This rule checks the alignment of multiline sequential statements.

**Violation**

.. code-block:: vhdl

   overflow <= wr_en and
     rd_en;

**Fix**

.. code-block:: vhdl

   overflow <= wr_en and
               rd_en;

sequential_005
##############

This rule checks the alignment of the **<=** operators over consecutive sequential lines.

**Violation**

.. code-block:: vhdl

   wr_en <= '1';
   rd_en   <= '0';

**Fix**

.. code-block:: vhdl

   wr_en   <= '1';
   rd_en   <= '0';

sequential_006
##############

This rule checks for comments within multiline sequential statements.

**Violation**

.. code-block:: vhdl

   overflow <= wr_en and
    --         rd_address(0)
               rd_en;

**Fix**

.. code-block:: vhdl

   overflow <= wr_en and
               rd_en;
