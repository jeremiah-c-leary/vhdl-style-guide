
architecture RTL of FIFO is

begin

  BLOCK_LABEL : block is begin end block;


  BLOCK_LABEL : block is begin end block;

  BLOCK_LABEL : block is--Comment
    begin end block;

  BLOCK_LABEL : block is --Comment
    begin end block;

  BLOCK_LABEL : block --Comment
    is begin end block;

  BLOCK_LABEL : block (guard_condition)is begin end block;

  BLOCK_LABEL : block (guard_condition) is begin end block;

  BLOCK_LABEL : block (guard_condition)is
    begin end block;

  BLOCK_LABEL : block is
    begin end block;

end architecture RTL;
