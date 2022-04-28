
architecture RTL of FIFO is

begin

  BLOCK_LABEL : block is begin end block;

  BLOCK_LABEL_1 : block is begin

    BLOCK_LABEL_2 : block is begin
    end block;

  end block;

  -- Violations below

  BLOCK_LABEL : block is begin end block;

  BLOCK_LABEL_1 : block is begin

    BLOCK_LABEL_2 : block is begin
    end block;

  end block;

end architecture RTL;
