
architecture RTL of FIFO is

begin

  BLOCK_LABEL : block is begin end block BLOCK_LABEL;

  BLOCK_LABEL_1 : block is begin

    BLOCK_LABEL_2 : block is begin
    end block BLOCK_LABEL_2;

  end block BLOCK_LABEL_1;

  -- Violations below

  BLOCK_LABEL : block is begin end block BLOCK_LABEL;

  BLOCK_LABEL_1 : block is begin

    BLOCK_LABEL_2 : block is begin
    end block BLOCK_LABEL_2;

  end block BLOCK_LABEL_1;

end architecture RTL;
