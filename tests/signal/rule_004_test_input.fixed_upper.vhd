
architecture RTL of FIFO is

  signal SIG1, SIG3, SIG4 : std_logic;
  signal SIG2 : std_logic;

  -- Violations below

  signal SIG1 : std_logic;
  signal SIG2, SIG3, SIG4 : std_logic;


begin

end architecture RTL;
