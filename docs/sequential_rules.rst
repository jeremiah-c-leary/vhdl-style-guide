.. include:: icons.rst

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

|phase_4| |error| |alignment|

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

