
architecture RTL of FIFO is

  signal sig1 : std_logic;

  type state_machine is (idle, write, read, done);

  -- Violations below

  signal sig1 : std_logic;
  type state_machine is (idle, write, read, done);

begin

end architecture RTL;
