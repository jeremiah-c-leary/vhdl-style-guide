
architecture RTL of FIFO is

  shared variable shar_var1 : integer;

begin

  process
    variable var1 : integer;
  begin
  end process;

end architecture RTL;

-- Violations below

architecture RTL of FIFO is

  shared VARIABLE shar_var1 : integer;

begin

  process
    VARIABLE var1 : integer;
  begin
  end process;

end architecture RTL;
