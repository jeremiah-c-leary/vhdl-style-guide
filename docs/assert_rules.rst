Assert Rules
------------

assert_001
##########

This rule checks indent of multiline assert statements.

**Violation**

.. code-block:: vhdl

   assert WIDTH > 16
        report "FIFO width is limited to 16 bits."
    severity FAILURE;

**Fix**

.. code-block:: vhdl

   assert WIDTH > 16
     report "FIFO width is limited to 16 bits."
     severity FAILURE;

assert_002
==========

This rule checks the **report** keyword is on it's own line for concurrent assertion statements.

**Violation**

.. code-block:: vhdl

   architecture rtl of fifo is
   begin

     assert WIDTH > 16 report "FIFO width is limited to 16 bits."
       severity FAILURE;

   end architecture rtl;

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is
   begin

     assert WIDTH > 16
       report "FIFO width is limited to 16 bits."
       severity FAILURE;

   end architecture rtl;

assert_003
==========

This rule checks the **report** keyword is on it's own line for assertion statements.

**Violation**

.. code-block:: vhdl

   architecture rtl of fifo is
   begin

     process
     begin

       assert WIDTH > 16 report "FIFO width is limited to 16 bits."
         severity FAILURE;

     end process;

   end architecture rtl;

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is
   begin

     process
     begin

       assert WIDTH > 16
         report "FIFO width is limited to 16 bits."
         severity FAILURE;

     end process;

   end architecture rtl;

assert_004
==========

This rule checks the **severity** keyword is on it's own line for concurrent assertion statements.

**Violation**

.. code-block:: vhdl

   architecture rtl of fifo is
   begin

     assert WIDTH > 16
       report "FIFO width is limited to 16 bits." severity FAILURE;

   end architecture rtl;

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is
   begin

     assert WIDTH > 16
       report "FIFO width is limited to 16 bits."
       severity FAILURE;

   end architecture rtl;

Alignment Rules (400 - 499)
###########################

assert_400
^^^^^^^^^^

This rule checks the alignment of the report expressions.

.. NOTE:: There is a configuration option **alignment** which changes the indent location of multiple lines.

alignment set to 'report' (Default)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Violation**

.. code-block:: vhdl

   assert WIDTH > 16
     report "FIFO width is limited" &
   " to 16 bits."
     severity FAILURE;

**Fix**

.. code-block:: vhdl

   assert WIDTH > 16
     report "FIFO width is limited" &
            " to 16 bits."
     severity FAILURE;

alignment set to 'left'
^^^^^^^^^^^^^^^^^^^^^^^

**Violation**

.. code-block:: vhdl

   assert WIDTH > 16
     report "FIFO width is limited" &
   " to 16 bits."
     severity FAILURE;

**Fix**

.. code-block:: vhdl

   assert WIDTH > 16
     report "FIFO width is limited" &
       " to 16 bits."
     severity FAILURE;
