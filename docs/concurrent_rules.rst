.. include:: icons.rst

Concurrent Rules
----------------

concurrent_001
##############

|phase_4| |error| |indent|

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

|phase_2| |error| |whitespace|

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

|phase_5| |error| |alignment|

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

|phase_2| |error| |whitespace|

This rule checks for at least a single space before the **<=** operator.

**Violation**

.. code-block:: vhdl

   wr_en<= '0';

**Fix**

.. code-block:: vhdl

   wr_en <= '0';

concurrent_005
##############

|phase_1| |error| |structure|

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

|phase_5| |error| |alignment|

This rule checks the alignment of the **<=** operator over multiple consecutive lines.
Refer to `Configuring Keyword Alignment Rules <configuring_keyword_alignment_rules.html>`_ for information on changing the configurations.

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

|phase_1| |error| |structure|

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

|phase_5| |error| |alignment|

This rule checks the alignment of inline comments in consecutive concurrent statements.
Refer to `Configuring Keyword Alignment Rules <configuring_keyword_alignment_rules.html>`_ for information on changing the configurations.

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

|phase_5| |error| |alignment|

This rule checks alignment of multiline concurrent conditional signal statements.

Refer to `Configuring Concurrent Alignment Rules <configuring_concurrent_alignment_rules.html>`_ for information on formatting options.

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

|phase_3| |error| |blank_line|

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

concurrent_011
##############

|phase_1| |error| |structure|

This rule checks the structure of simple and conditional concurrent statements.

Refer to `Configuring Multiline Structure Rules <configuring_multiline_structure_rules.html>`_ for information on formatting options.

**Violation**

.. code-block:: vhdl

   wr_en <=
     '0' when q_wr_en = '1' else
            '1';

   w_foo <=
     I_FOO when ((I_BAR = '1') and
                        (I_CRUFT = '1')) else
            '0';

**Fix**

.. code-block:: vhdl

   wr_en <= '0' when q_wr_en = '1' else
            '1';

   w_foo <= I_FOO when ((I_BAR = '1') and
                        (I_CRUFT = '1')) else
            '0';

