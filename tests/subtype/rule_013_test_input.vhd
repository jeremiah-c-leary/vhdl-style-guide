
architecture RTL of FIFO is

  subtype state_machine is (idle, write, read, done);

  -- Violations below

  SUBTYPE state_machine is (idle, write, read, done);

begin

end architecture RTL;
