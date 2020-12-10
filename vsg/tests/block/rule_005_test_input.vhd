
architecture RTL of FIFO is

begin

  BLOCK_LABEL : block is begin
    a <= b;
  end block;

  -- Violations below

  BLOCK_LABEL : block is begin a <= b; end block;

end architecture RTL;
