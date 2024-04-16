
architecture RTl of FIFO is

  component fifo is
    generic (
      gen_dec1 : integer := 0; -- Comment
      -- Keep Comment
      gen_dec2 : integer := 1; -- Comment
      gen_dec3 : integer := 2  -- Comment
    );
    port (
      sig1 : std_logic; -- Comment
      -- Keep Comment
      sig2 : std_logic; -- Comment
      sig3 : std_logic  -- Comment
      -- Keep Comment
    );
  end component fifo;

  -- Failures below
  component fifo is
    generic (
      gen_dec1   : integer := 0;-- Comment
      -- Keep Comment
      gen_dec2     : integer := 1;
      gen_dec3  : integer := 2-- Comment
      -- Keep Comment
    );
    port (
      -- Keep Comment
      sig1     : std_logic; -- Comment
      -- Keep Comment
      sig2  : std_logic; -- Comment
      -- Keep Comment
      sig3   : std_logic  -- Comment
      -- Keep Comment
    );
  end component fifo;

begin

end architecture RTL;
