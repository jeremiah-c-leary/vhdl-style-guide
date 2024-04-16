
architecture RTL of FIFO is

  type state_machine is (idle, write, read, done);

  -- Violations below

  type state_machine is (IDLE, WRITE, READ, DONE);

begin

end architecture RTL;
