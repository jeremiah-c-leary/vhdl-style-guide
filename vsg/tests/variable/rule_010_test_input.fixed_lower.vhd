
architecture RTL of FIFO is

  shared variable shar_var1 : integer;
  shared variable shar_var2 : std_logic_vector(3 downto 0);

begin

  process
    variable var1 : integer;
    variable var2 : std_logic_vector(3 downto 0);
  begin
  end process;

end architecture RTL;

-- Violations below

architecture RTL of FIFO is

  shared variable shar_var1 : integer;
  shared variable shar_var2 : std_logic_vector(3 downto 0);

begin

  process
    variable var1 : integer;
    variable var2 : std_logic_vector(3 downto 0);
  begin
  end process;

end architecture RTL;
