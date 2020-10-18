
architecture RTL of FIFO is

  signal sig1, sig3, sig4 : std_logic;
  signal sig2 : std_logic;

  -- Violations below

  signal sig1 : std_logic;
  signal sig2, sig3, sig4 : std_logic;


begin

end architecture RTL;
