.. include:: includes.rst

Assert Rules
------------

assert_001
##########

|phase_4| |error| |indent|

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
##########

|phase_1| |error| |structure|

This rule checks the **report** keyword is on its own line for concurrent assertion statements.

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
##########

|phase_1| |error| |structure|

This rule checks the **report** keyword is on its own line for sequential assertion statements.

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
##########

|phase_1| |error| |structure|

This rule checks the **severity** keyword is on its own line for concurrent assertion statements.

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

assert_005
##########

|phase_1| |error| |structure|

This rule checks the **severity** keyword is on its own line for sequential assertion statements.

**Violation**

.. code-block:: vhdl

   architecture rtl of fifo is
   begin

     process begin

       assert WIDTH > 16 report "FIFO width is limited to 16 bits." severity FAILURE;

     end process;

   end architecture rtl;

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is
   begin

     process begin

       assert WIDTH > 16 report "FIFO width is limited to 16 bits."
         severity FAILURE;

     end process;

   end architecture rtl;

assert_100
##########

|phase_2| |error| |whitespace|

This rule checks for a single space after the **assert** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   assert         WIDTH > 16
     report "FIFO width is limited to 16 bits."
     severity FAILURE;

**Fix**

.. code-block:: vhdl

   assert WIDTH > 16
     report "FIFO width is limited to 16 bits."
     severity FAILURE;

assert_101
##########

|phase_2| |error| |whitespace|

This rule checks for a single space after the **report** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   assert WIDTH > 16
     report      "FIFO width is limited to 16 bits."
     severity FAILURE;

**Fix**

.. code-block:: vhdl

   assert WIDTH > 16
     report "FIFO width is limited to 16 bits."
     severity FAILURE;

assert_102
##########

|phase_2| |error| |whitespace|

This rule checks for a single space after the **severity** keyword.

|configuring_whitespace_rules_link|

**Violation**

.. code-block:: vhdl

   assert WIDTH > 16
     report "FIFO width is limited to 16 bits."
     severity       FAILURE;

**Fix**

.. code-block:: vhdl

   assert WIDTH > 16
     report "FIFO width is limited to 16 bits."
     severity FAILURE;

assert_400
##########

|phase_4| |error| |alignment|

This rule checks the alignment of the report expressions.

.. NOTE:: There is a configuration option **alignment** which changes the indent location of multiple lines.

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

assert_500
##########

|phase_6| |error| |case| |case_keyword|

This rule checks the **assert** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   ASSERT WIDTH > 16
     report "FIFO width is limited to 16 bits."
     severity FAILURE;

.. code-block:: vhdl

   assert WIDTH > 16
     report "FIFO width is limited to 16 bits."
     severity FAILURE;

assert_501
##########

|phase_6| |error| |case| |case_keyword|

This rule checks the **report** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   assert WIDTH > 16
     REPORT "FIFO width is limited to 16 bits."
     severity FAILURE;

.. code-block:: vhdl

   assert WIDTH > 16
     report "FIFO width is limited to 16 bits."
     severity FAILURE;

assert_502
##########

|phase_6| |error| |case| |case_keyword|

This rule checks the **severity** keyword has proper case.

|configuring_uppercase_and_lowercase_rules_link|

**Violation**

.. code-block:: vhdl

   assert WIDTH > 16
     report "FIFO width is limited to 16 bits."
     SEVERITY FAILURE;

.. code-block:: vhdl

   assert WIDTH > 16
     report "FIFO width is limited to 16 bits."
     severity FAILURE;
