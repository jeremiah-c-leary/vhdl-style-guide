
architecture RTL of FIFO is

  shared variable shar_var1 : INTEGER;
  shared variable shar_var2 : STD_LOGIC_VECTOR(3 downto 0);

begin

  process
    variable var1 : INTEGER;
    variable var2 : STD_LOGIC_VECTOR(3 downto 0);
  begin
  end process;

end architecture RTL;

-- Violations below

architecture RTL of FIFO is

  shared variable shar_var1 : INTEGER;
  shared variable shar_var2 : STD_LOGIC_VECTOR(3 downto 0);

begin

  process
    variable var1 : INTEGER;
    variable var2 : STD_LOGIC_VECTOR(3 downto 0);
  begin
  end process;

end architecture RTL;
