
architecture RTL of FIFO is

begin

  a <= b & c;

  -- violations

  a <= b & c;

  a <= b & c;

  a <= b & c;

  -- Multiple violations

  a <= b & c & d & e;

  -- Extra spaces

  a <= b & c & d & e;

  -- This is okay

  a <= b
       & c
       & d;

end architecture RTL;
