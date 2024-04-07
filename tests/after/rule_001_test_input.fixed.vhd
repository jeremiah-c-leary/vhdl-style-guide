
architecture ARCH of ENTITY is

begin

  CLK_PROC : process (reset, clk) is
  begin

    if (reset = '1') then
       a <= '0';
       b <= '1';
       c <= '0';
       d <= '1';
    elsif (clk'event and clk = '1') then
       a <= b after 1 ns;
       b <= c after 1 ns;
       c <= d after 1 ns;
       d <= e after 1 ns;
    end if;
  end process CLK_PROC;

  -- This process checks for a clock process without a reset
  CLK_PROC : process (reset, clk) is
  begin

    if (falling_edge(clk)) then
       a <= b after 1 ns;
       b <= c after 1 ns;
       c <= d after 1 ns;
       d <= e after 1 ns;
    end if;
  end process CLK_PROC;

  -- This process checks for a clock process without a reset
  CLK_PROC : process (reset, clk) is
  begin

    if (rising_edge(clk)) then
       a <= b after 1 ns;
       b <= c after 1 ns;
       c <= d after 1 ns;
       d <= e after 1 ns;
    end if;
  end process CLK_PROC;

  -- This process checks for a clock process without a reset
  CLK_PROC : process (reset, clk) is
  begin

    if (clk'event and clk = '1') then
       a <= b after 1 ns;
       b <= c after 1 ns;
       c <= d after 1 ns;
       d <= e after 1 ns;
    end if;
  end process CLK_PROC;

  -- This checks detection of after outside clock processes
  a <= b after 10 ns;

  --  Violations below -----------------------------------

  -- This process checks for missing after statements
  CLK_PROC : process (reset, clk) is
  begin

    if (reset = '1') then
       a <= '0';
       b <= '1';
       c <= '0';
       d <= '1';
    elsif (clk'event and clk = '1') then
       a <= b after 1 ns;
       b <= c after 1 ns;
       c <= d after 1 ns;
       d <= e after 1 ns;
    end if;
  end process CLK_PROC;

  -- This process checks for a clock process without a reset
  CLK_PROC : process (reset, clk) is
  begin

    if (falling_edge(clk)) then
       a <= b after 1 ns;
       b <= c after 1 ns;
       c <= d after 1 ns;
       d <= e after 1 ns;
    end if;
  end process CLK_PROC;

  -- This process checks for a clock process without a reset
  CLK_PROC : process (reset, clk) is
  begin

    if (rising_edge(clk)) then
       a <= b after 1 ns;
       b <= c after 1 ns;
       c <= d after 1 ns;
       d <= e after 1 ns;
    end if;
  end process CLK_PROC;

  -- This process checks for a clock process without a reset
  CLK_PROC : process (reset, clk) is
  begin

    if (clk'event and clk = '1') then
       a <= b after 1 ns;
       b <= c after 1 ns;
       c <= d after 1 ns;
       d <= e after 1 ns;
    end if;
  end process CLK_PROC;

end architecture ARCH;
