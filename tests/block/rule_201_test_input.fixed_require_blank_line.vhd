
architecture RTL of FIFO is

begin

  -- With no optional parameters
  BLOCK_LABEL : block
  begin
  end block;

  BLOCK_LABEL : block

    signal sig1 : std_logic;
  begin
  end block;

  -- With optional is keyword
  BLOCK_LABEL : block (guard) is
  begin
  end block;

  BLOCK_LABEL : block (guard) is

    signal sig1 : std_logic;
  begin
  end block;

  -- With optional guard
  BLOCK_LABEL : block (guard)
  begin
  end block;

  BLOCK_LABEL : block (guard)

    signal sig1 : std_logic;
  begin
  end block;

  -- multi line
  BLOCK_LABEL : block
  (guard)
  is
  begin
  end block;

  BLOCK_LABEL : block
  (guard)
  is

    signal sig1 : std_logic;
  begin
  end block;

  -- Violations below
  BLOCK_LABEL : block is

    signal sig1 : std_logic;
  begin
  end block;

  BLOCK_LABEL : block

    signal sig1 : std_logic;
  begin end block;

  BLOCK_LABEL : block (guard)

    signal sig1 : std_logic;
  begin end block;

end architecture RTL;
