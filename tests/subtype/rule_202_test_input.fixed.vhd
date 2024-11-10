
architecture RTL of FIFO is

  subtype counter is unsigned(4 downto 0);

  signal sig1 : std_logic;

  -- Violations below

  subtype counter is unsigned(4 downto 0);

  signal sig1 : std_logic;

begin

end architecture RTL;
