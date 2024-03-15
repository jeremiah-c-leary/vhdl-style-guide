
architecture RTL of FIFO is

  type state_machine is (idle, write, read, done);

  -- Violations below

  type STATE_MACHINE is (idle, write, read, done);

begin

end architecture RTL;
