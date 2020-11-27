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

This rule checks alignment of multiline concurrent simple signal assignments.
Succesive lines should align to the space after the assignment operator.
However, there is a special case if there are parenthesis in the assignment.
If the parenthesis are not closed on the same line, then the next line will be aligned to the parenthesis.
Aligning to the parenthesis improves readability.

**Violation**

.. code-block:: vhdl

   O_FOO <= (1 => q_foo(63 downto 32),
            0 => q_foo(31 downto  0));

   n_foo <= resize(unsigned(I_FOO) +
            unsigned(I_BAR), q_foo'length);

**Fix**

.. code-block:: vhdl

   O_FOO <= (1 => q_foo(63 downto 32),
             0 => q_foo(31 downto  0));

   n_foo <= resize(unsigned(I_FOO) +
                   unsigned(I_BAR), q_foo'length);

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
Refer to the section `Configuring Keyword Alignment Rules <configuring_keyword_alignment.html>`_ for information on changing the configurations.

**Violation**

.. code-block:: vhdl

   wr_en <= '0';
   rd_en   <= '1';
   data <= (others => '0');

**Fix**

.. code-block:: vhdl

   wr_en <= '0';
   rd_en <= '1';
   data  <= (others => '0');

concurrent_007
##############

This rule checks for code after the **else** keyword.

.. NOTE:: There is a configuration option **allow_single_line** which allows single line concurrent statements.

allow_single_line set to False (Default)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Violation**

.. code-block:: vhdl

   wr_en <= '0' when overflow = '0' else '1';
   wr_en <= '0' when overflow = '0' else '1' when underflow = '1' else sig_a;

**Fix**

.. code-block:: vhdl

   wr_en <= '0' when overflow = '0' else
            '1';
   wr_en <= '0' when overflow = '0' else
            '1' when underflow = '1' else
            sig_a;

allow_single_line set to True
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Violation**

.. code-block:: vhdl

   wr_en <= '0' when overflow = '0' else '1';
   wr_en <= '0' when overflow = '0' else '1' when underflow = '1' else sig_a;

**Fix**

.. code-block:: vhdl

   wr_en <= '0' when overflow = '0' else '1';
   wr_en <= '0' when overflow = '0' else
            '1' when underflow = '1' else
            sig_a;

concurrent_008
##############

This rule checks the alignment of inline comments in sequential concurrent statements.
Refer to the section `Configuring Keyword Alignment Rules <configuring_keyword_alignment.html>`_ for information on changing the configurations.

**Violation**

.. code-block:: vhdl

   wr_en <= '0';     -- Write enable
   rd_en <= '1';   -- Read enable
   data  <= (others => '0'); -- Write data

**Fix**

.. code-block:: vhdl

   wr_en <= '0';             -- Write enable
   rd_en <= '1';             -- Read enable
   data  <= (others => '0'); -- Write data

concurrent_009
##############

This rule checks alignment of multiline concurrent conditional signal statements.
The waveform should align to the space after the assignment operator.
Conditions should align with the **when** keyword.

However, there is a special case if there are parenthesis in the assignment.
If the parenthesis are not closed on the same line, then the next line will be aligned to the parenthesis.
Aligning to the parenthesis improves readability.

**Violation**

.. code-block:: vhdl

   wr_en <= '0' when q_wr_en = '1' else
        '1';

   w_foo <= I_FOO when ((I_BAR = '1') and
            (I_CRUFT = '1')) else
            '0';

**Fix**

.. code-block:: vhdl

   wr_en <= '0' when q_wr_en = '1' else
            '1';

   w_foo <= I_FOO when ((I_BAR = '1') and
                        (I_CRUFT = '1')) else
            '0';

concurrent_010
##############

This rule removes blank lines within concurrent signal assignments.

**Violation**

.. code-block:: vhdl

   wr_en <= '0' when q_wr_en = '1' else

        '1';

   w_foo <= I_FOO when ((I_BAR = '1') and

                        (I_CRUFT = '1')) else

            '0';

**Fix**

.. code-block:: vhdl

   wr_en <= '0' when q_wr_en = '1' else
            '1';

   w_foo <= I_FOO when ((I_BAR = '1') and
                        (I_CRUFT = '1')) else
            '0';
