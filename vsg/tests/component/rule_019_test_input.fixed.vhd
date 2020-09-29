
architecture RTl of FIFO is

  component fifo is
    generic (
      gen_dec1 : integer := 0;
      gen_dec2 : integer := 1;
      gen_dec3 : integer := 2
    );
    port (
      sig1 : std_logic;
      sig2 : std_logic;
      sig3 : std_logic
    );
  end component fifo;

  -- Failures below
  component fifo is
    generic (
      gen_dec1   : integer := 0;
      gen_dec2     : integer := 1;
      gen_dec3  : integer := 2
    );
    port (
      sig1     : std_logic;
      sig2  : std_logic;
      sig3   : std_logic
    );
  end component fifo;

begin

end architecture RTL;
