
architecture RTL of FIFO is

  type state_machine is (idle, write, read, done);

  -- Violations below

  type state_machine is (idle,
    write, 
    read, done);

  type state_machine is (idle,
    write, read, done);

  type state_machine is (idle,
    write,
    read, 
    done);

begin

end architecture RTL;
