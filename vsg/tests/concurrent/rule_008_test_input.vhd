
architecture RTL of FIFO is

begin

  -- These are passing

  a <= b;                     -- Comment 1
  a <= when c = '0' else '1'; -- Comment 2
  a <= b;                     -- Comment 3
  a <= when c = '0' else '1'; -- Comment 4

  -- Failing variations

  a <= b;-- Comment 1
  a <= when c = '0' else '1';     -- Comment 2
  a <= b; -- Comment 3
  a <= when c = '0' else '1';-- Comment 4

  process
  begin

    a <= b; -- Comment
    b <= c;         -- Comment
    c <= d;      -- Comment
  end process;

end architecture RTL;
