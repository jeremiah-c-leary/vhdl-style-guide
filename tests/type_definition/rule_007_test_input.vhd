
architecture RTL of FIFO is

  type state_machine is (idle, write, read, done);
  type size is range 0 to 9;
  type mem1 is array (integer range <>) of std_logic;
  type mem2 is array (0 to 511) of std_logic;
  type rec1 is record wr_full : std_logic; end record;
  type access1 is access std_logic;
  type file1 is file of std_logic;

  -- Violations below

  type state_machine is    (idle, write, read, done);
  type size is    range 0 to 9;
  type mem1 is    array (integer range <>) of std_logic;
  type mem2 is    array (0 to 511) of std_logic;
  type rec1 is    record wr_full : std_logic; end record;
  type access1 is    access std_logic;
  type file1 is    file of std_logic;

begin

end architecture RTL;
