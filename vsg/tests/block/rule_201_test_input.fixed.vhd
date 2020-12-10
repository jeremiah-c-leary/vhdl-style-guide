
architecture RTL of FIFO is

begin

  BLOCK_LABEL : block is
  begin
  end block;

  BLOCK_LABEL : block is

    signal sig1 : std_logic;
  begin
  end block;

  -- Violations below
  BLOCK_LABEL : block is

    signal sig1 : std_logic;
  begin
  end block;

end architecture RTL;
