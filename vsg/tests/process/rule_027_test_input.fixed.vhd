
architecture RTL of FIFO is

begin


  process
    variable var1 : integer;

  begin
  end process;

  process (a, b)
    variable var1 : integer;

  begin
  end process;

  process is
    variable var1 : integer;

  begin
  end process;

  -- Violations below

  process
    variable var1 : integer;

  begin
  end process;

  process (a, b)
    variable var1 : integer;

  begin
  end process;

  process is
    variable var1 : integer;

  begin
  end process;


end architecture RTL;
