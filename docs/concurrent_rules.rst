.. include:: includes.rst

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

|configuring_whitespace_rules_link|

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
Successive lines should align to the space after the assignment operator.
However, there is a special case if there are parenthesis in the assignment.
If the parenthesis are not closed on the same line, then the next line will be aligned to the parenthesis.
Aligning to the parenthesis improves readability.

|configuring_multiline_indent_rules_link|

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

|configuring_whitespace_rules_link|

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
|configuring_keyword_alignment_rules_link|

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

This rule has been renamed to `conditional_waveforms_001 <conditional_waveforms_rules.html#conditional-waveforms-001>`_.

concurrent_008
##############

|phase_5| |error| |alignment|

This rule checks the alignment of inline comments in consecutive concurrent statements.
|configuring_keyword_alignment_rules_link|

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

|configuring_conditional_multiline_indent_rules_link|

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

|configuring_simple_multiline_structure_rules_link|

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

concurrent_012
##############

|phase_1| |error| |structure|

This rule checks the structure of multiline concurrent simple signal assignments that contain arrays.

|configuring_array_multiline_structure_rules_link|

**Violation**

.. code-block:: vhdl

   wr_data <= (0, 65535, 32768);

**Fix**

.. code-block:: vhdl

   wr_data <=
   (
     0,
     65535,
     32768
   );

concurrent_400
##############

|phase_5| |error| |alignment|

This rule checks the alignment the => operator in record aggregates.

|configuring_keyword_alignment_rules_link|

**Violation**

.. code-block:: vhdl

   interface <= (
                 write_words => 12,
                 read_words => 32
                 address => 57
                );

**Fix**

.. code-block:: vhdl

   interface <= (
                 write_words => 12,
                 read_words  => 32
                 address     => 57
                );

concurrent_401
##############

|phase_5| |error| |alignment|

This rule checks the alignment of multiline concurrent simple signal assignments that contain arrays.

|configuring_multiline_indent_rules_link|

**Violation**

.. code-block:: vhdl

   wr_data <=
   (
            0,
        65535,
        32768
     );

**Fix**

.. code-block:: vhdl

   wr_data <=
   (
     0,
     65535,
     32768
   );

