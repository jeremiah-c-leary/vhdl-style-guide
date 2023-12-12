
architecture RTL of FIFO is

begin

  BLOCK_LABEL : block is begin end block;

  BLOCK_LABEL : block (guard_condition) is begin end block;

  -- Violations below

  BLOCK_LABEL : block is
  begin end block;

  BLOCK_LABEL : block (guard_condition) is
  begin end block;

  BLOCK_LABEL : block
  -- synthesis translate_off
  is begin end block;

end architecture RTL;
