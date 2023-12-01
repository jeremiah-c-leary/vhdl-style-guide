.. include:: includes.rst

Pragma Rules
------------

pragma_300
##########

|phase_4| |error| |indent|

This rule checks the indent of pragmas.

|configuring_pragmas_link|

**Violation**

.. code-block:: vhdl

   architecture rtl of fifo is

     -- synthesis translate_off
     signal wr_en : std_logic;
     signal rd_en : std_Logic;
     -- synthesis translate_on

   begin

**Fix**

.. code-block:: vhdl

   architecture rtl of fifo is

     -- synthesis translate_off
     signal wr_en : std_logic;
     signal rd_en : std_Logic;
   -- synthesis translate_on

   begin

