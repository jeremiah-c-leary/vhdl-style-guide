
architecture RTl of FIFO is

  component fifo is

  end component fifo;

  -- Comments are fine
  component fifo   is

  end component fifo;

  -- This should fail
  signal sig1 : std_logic;

  component fifo    is

  end component fifo;

begin

end architecture RTL;
