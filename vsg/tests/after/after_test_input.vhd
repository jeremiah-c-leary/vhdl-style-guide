
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
       b <= c;
       c <= d;
       d <= e after 1 ns;
    end if;
  end process CLK_PROC;

  -- This process checks for incorrect times
  CLK_PROC : process (reset, clk) is
  begin

    if (reset = '1') then
       a <= '0';
       b <= '1';
       c <= '0';
       d <= '1';
    elsif (rising_edge(clk)) then
       a <= b after 1 s;
       b <= c after 1 ms;
       c <= d after 200 ns;
       d <= e after 10 ns;
    end if;
  end process CLK_PROC;

  -- This process checks for unalined after statements
  CLK_PROC : process (reset, clk) is
  begin

    if (reset = '1') then
       a <= '0';
       b <= '1';
       c <= '0';
       d <= '1';
    elsif (falling_edge(clk)) then
       a <= b after 1 ns;
       b <= c after 1 ns;
       c <= d after 1 ns;
       d <= e after 1 ns;
    end if;
  end process CLK_PROC;

  -- This checks detection of after outside clock processes
  a <= b after 10 ns;

end architecture ARCH;

