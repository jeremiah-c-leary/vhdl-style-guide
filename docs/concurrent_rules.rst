Concurrent Rules
----------------

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

