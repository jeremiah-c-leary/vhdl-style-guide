.. include:: includes.rst

After Rules
-----------

after_001
#########

|phase_1| |disabled| |error| |structure|

This rule checks for **after x** in signal assignments in clock processes.

**Violation**

.. code-block:: vhdl

   clk_proc : process(clock, reset) is
   begin
     if (reset = '1') then
       a <= '0';
       b <= '1';
     elsif (clock'event and clock = '1') then
       a <= d;
       b <= c;
     end if;
   end process clk_proc;

**Fix**

.. code-block:: vhdl

   clk_proc : process(clock, reset) is
   begin
     if (reset = '1') then
       a <= '0';
       b <= '1';
     elsif (clock'event and clock = '1') then
       a <= d after 1 ns;
       b <= c after 1 ns;
     end if;
   end process clk_proc;

.. NOTE::  This rule has two configurable items:

   * magnitude
   * units

   The **magnitude** is the number of units.  Default is *1*.

   The **units** is a valid time unit: ms, us, ns, ps etc...  Default is *ns*.

after_002
#########

|phase_5| |disabled| |error| |alignment|

This rule checks the *after* keywords are aligned in a clock process.

|configuring_keyword_alignment_rules_link|

**Violation**

.. code-block:: vhdl

   clk_proc : process(clock, reset) is
   begin
     if (reset = '1') then
       a <= '0';
       b <= '1';
     elsif (clock'event and clock = '1') then
       a <= d     after 1 ns;
       b <= c   after 1 ns;
     end if;
   end process clk_proc;

**Fix**

.. code-block:: vhdl

   clk_proc : process(clock, reset) is
   begin
     if (reset = '1') then
       a <= '0';
       b <= '1';
     elsif (clock'event and clock = '1') then
       a <= d     after 1 ns;
       b <= c     after 1 ns;
     end if;
   end process clk_proc;

after_003
#########

|phase_1| |disabled| |error| |structure|

This rule checks the *after* keywords do not exist in the reset portion of a clock process.

**Violation**

.. code-block:: vhdl

   clk_proc : process(clock, reset) is
   begin
     if (reset = '1') then
       a <= '0' after 1 ns;
       b <= '1' after 1 ns;
     elsif (clock'event and clock = '1') then
       a <= d after 1 ns;
       b <= c after 1 ns;
     end if;
   end process clk_proc;

**Fix**

.. code-block:: vhdl

   clk_proc : process(clock, reset) is
   begin
     if (reset = '1') then
       a <= '0';
       b <= '1';
     elsif (clock'event and clock = '1') then
       a <= d  after 1 ns;
       b <= c  after 1 ns;
     end if;
   end process clk_proc;
