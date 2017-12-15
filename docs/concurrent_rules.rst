Concurrent Rules
----------------


concurrent_001
##############

This rule checks the indent of concurrent assignments.

**Violation**

.. code-block:: vhdl

   architecture RTL of FIFO is
   begin

        wr_en <= '0';
   rd_en <= '1';

**Fix**

.. code-block:: vhdl

   architecture RTL of FIFO is
   begin

     wr_en <= '0';
     rd_en <= '1';

concurrent_002
##############

This rule checks for a single space after the **<=** operator.

**Violation**

.. code-block:: vhdl

   wr_en <=    '0';
   rd_en <=   '1';

**Fix**

.. code-block:: vhdl

   wr_en <= '0';
   rd_en <= '1';

concurrent_003
##############

This rule checks alignment of multiline concurrent assignments.

**Violation**

.. code-block:: vhdl

   wr_en <= '0' when q_wr_en = '1' else
        '1';

**Fix**

.. code-block:: vhdl

   wr_en <= '0' when q_wr_en = '1' else
            '1';

concurrent_004
##############

This rule checks for at least a single space before the **<=** operator.

**Violation**

.. code-block:: vhdl

   wr_en<= '0';

**Fix**

.. code-block:: vhdl

   wr_en <= '0';

concurrent_005
##############

This rule checks for labels on concurrent assignments.
Labels on concurrents are optional and do not provide additional information.

**Violation**

.. code-block:: vhdl

   WR_EN_OUTPUT : WR_EN <= q_wr_en;
   RD_EN_OUTPUT : RD_EN <= q_rd_en;

**Fix**

.. code-block:: vhdl

   WR_EN <= q_wr_en;
   RD_EN <= q_rd_en;

concurrent_006
##############

This rule checks the alignment of the **<=** operator over multiple consecutive lines.

**Violation**

.. code-block:: vhdl

   wr_en <= '0';
   rd_en   <= '1';
   data <= (others => '0');

**Fix**

.. code-block:: vhdl

   wr_en   <= '0';
   rd_en   <= '1';
   data    <= (others => '0');

concurrent_007
##############

This rule checks for code after the **else** keyword.

**Violation**

.. code-block:: vhdl

   wr_en <= '0' when overflow = '0' else '1';

**Fix**

.. code-block:: vhdl

   wr_en <= '0' when overflow = '0' else
            '1';

concurrent_008
##############

This rule checks the alignment of inline comments in sequential concurrent statements.

**Violation**

.. code-block:: vhdl

   wr_en   <= '0';    -- Write enable
   rd_en   <= '1';  -- Read enable
   data    <= (others => '0');   -- Write data


**Fix**

.. code-block:: vhdl

   wr_en   <= '0';               -- Write enable
   rd_en   <= '1';               -- Read enable
   data    <= (others => '0');   -- Write data

