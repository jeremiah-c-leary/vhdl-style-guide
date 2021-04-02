.. include:: icons.rst

Assert Rules
------------

assert_001
##########

|phase_4| |error|

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

Alignment Rules (400 - 499)
###########################

assert_400
^^^^^^^^^^

|phase_4| |error|

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
