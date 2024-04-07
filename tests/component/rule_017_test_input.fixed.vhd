
architecture RTl of FIFO is

  component fifo is
    generic (
      gen1 : integer := 0; -- Comment
      gen2 : integer := 1; -- Comment
      gen3 : integer := 2  -- Comment
    );
    port (
      sig1 : std_logic; -- Comment
      sig2 : std_logic; -- Comment
      sig3 : std_logic  -- Comment
    );
  end component fifo;

  -- Failures below
  component fifo is
    generic (
      gen1 : integer := 0; -- Comment
      gen2 : integer := 1; -- Comment
      gen3 : integer := 2  -- Comment
    );
    port (
      sig1 : std_logic; -- Comment
      sig2 : std_logic; -- Comment
      sig3 : std_logic  -- Comment
    );
  end component fifo;

begin

end architecture RTL;
