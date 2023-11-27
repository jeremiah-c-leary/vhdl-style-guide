
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

  -- Violations

  CLK_PROC : process (reset, clk) is
  begin

    if (reset = '1') then
       a <= '0';
       b <= '1';
       c <= '0';
       d <= '1';
    elsif (clk'event and clk = '1') then
       a <= b             after 1 ns;
       b <= c             after 1 ns;
       -- Comment
       c <= d   after 1 ns;

       d <= e  after 1 ns;
    end if;
  end process CLK_PROC;

end architecture ARCH;

