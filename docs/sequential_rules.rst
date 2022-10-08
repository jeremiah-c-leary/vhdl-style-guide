.. include:: includes.rst

Sequential Rules
----------------

sequential_001
##############

|phase_4| |error| |indent|

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

|phase_2| |error| |whitespace|

This rule checks for a single space after the **<=** operator.

|configuring_whitespace_rules_link|

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

|phase_2| |error| |whitespace|

This rule checks for at least a single space before the **<=** operator.

|configuring_whitespace_rules_link|

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

|phase_5| |error| |alignment|

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

This rule has been deprecated and replaced with rule `process_400 <process_rules.html#process-400>`_.

sequential_006
##############

|phase_2| |error| |structure|

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

sequential_007
##############

|phase_1| |error| |structure|

This rule checks for code after a sequential assignment.

**Violation**

.. code-block:: vhdl

    a <= '0'; b <= '1'; c <= '0'; -- comment

**Fix**

.. code-block:: vhdl

    a <= '0';
    b <= '1';
    c <= '0'; -- comment

sequential_008
##############

|phase_1| |error| |structure|

This rule checks the structure of simple and conditional sequential signal assignments.

|configuring_multiline_structure_rules_link|

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

sequential_009
##############

|phase_1| |error| |structure|

This rule checks the structure of multiline simple sequential signal assignments that contain arrays.

|configuring_multiline_structure_rules_link|

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

sequential_400
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

sequential_401
##############

|phase_5| |error| |alignment|

This rule checks alignment of multiline sequential conditional signal assignments.

|configuring_concurrent_alignment_rules_link|

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

