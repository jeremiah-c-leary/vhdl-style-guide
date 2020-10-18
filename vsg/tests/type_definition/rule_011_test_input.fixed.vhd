
architecture RTL of FIFO is

  type state_machine is (idle, write, read, done);

  signal sig1 : std_logic;

  -- Violations below

  type state_machine is (idle, write, read, done);

  signal sig1 : std_logic;

begin

end architecture RTL;
