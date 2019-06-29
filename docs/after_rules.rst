After Rules
-----------

after_001
#########

This rule checks for **after x** in signal assignments in clock processes.

.. NOTE::  All rules in this group are disabled by default.
           Use a configuration to enable them.

**Violation**

.. code-block:: vhdl

   CLK_PROC : process(clock, reset) is
   begin
     if (reset = '1') then
       a <= '0';
       b <= '1';
     elsif (clock'event and clock = '1') then
       a <= d;
       b <= c;
     end if;
   end process CLK_PROC;

**Fix**

.. code-block:: vhdl

   CLK_PROC : process(clock, reset) is
   begin
     if (reset = '1') then
       a <= '0';
       b <= '1';
     elsif (clock'event and clock = '1') then
       a <= d after 1 ns;
       b <= c after 1 ns;
     end if;
   end process CLK_PROC;

.. NOTE::  This rule has two configurable items:

   * magnitude
   * units

   The **magnitude** is the number of units.  Default is *1*.

   The **units** is a valid time unit: ms, us, ns, ps etc...  Default is *ns*.

after_002
#########

This rule checks the *after* keywords are aligned in a clock process.

.. NOTE::  All rules in this group are disabled by default.
           Use a configuration to enable them.

**Violation**

.. code-block:: vhdl

   CLK_PROC : process(clock, reset) is
   begin
     if (reset = '1') then
       a <= '0';
       b <= '1';
     elsif (clock'event and clock = '1') then
       a <= d     after 1 ns;
       b <= c   after 1 ns;
     end if;
   end process CLK_PROC;

**Fix**

.. code-block:: vhdl

   CLK_PROC : process(clock, reset) is
   begin
     if (reset = '1') then
       a <= '0';
       b <= '1';
     elsif (clock'event and clock = '1') then
       a <= d     after 1 ns;
       b <= c     after 1 ns;
     end if;
   end process CLK_PROC;

