
architecture RTL of FIFO is

  type state_machine is (idle, write, read, done);

  -- Violations below

  type state_machine
  is (idle, write, read, done);

  type state_machine


  is (idle, write, read, done);

  -- Honor comments

  type state_machine
  -- some comment
  is (idle, write, read, done);

  type state_machine
  -- synthesis translate_off
  is (idle, write, read, done);

begin

end architecture RTL;
