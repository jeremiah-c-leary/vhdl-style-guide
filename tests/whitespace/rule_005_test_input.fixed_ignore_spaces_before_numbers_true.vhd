
architecture RTL of FIFO is

  signal sig1 : std_logic_vector(31 downto 0);
  signal sig2 : std_logic_vector( 3 downto 0);
  signal sig3 : std_logic_vector(c_width downto 0);

  -- Violations

  signal sig1 : std_logic_vector( 31 downto 0);
  signal sig2 : std_logic_vector(3 downto 0);
  signal sig3 : std_logic_vector(c_width downto 0);

begin

end architecture RTL;
