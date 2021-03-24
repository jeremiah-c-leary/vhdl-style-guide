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

Following extra configurations are supported:

* :code:`if_control_statements_end_group`,
* :code:`case_control_statements_end_group`.

Refer to the section `Configuring Keyword Alignment Rules <configuring.html#configuring-keyword-alignment-rules>`_ for information on changing the configurations.

**Violation**

.. code-block:: vhdl

   wr_en <= '1';
   rd_en   <= '0';

**Fix**

.. code-block:: vhdl

   wr_en <= '1';
   rd_en <= '0';

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

sequential_007
##############

This rule checks for code after a sequential assignment.

**Violation**

.. code-block:: vhdl

    a <= '0'; b <= '1'; c <= '0'; -- comment

**Fix**

.. code-block:: vhdl

    a <= '0';
    b <= '1';
    c <= '0'; -- comment
