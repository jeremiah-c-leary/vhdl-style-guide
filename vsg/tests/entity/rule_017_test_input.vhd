

entity fifo is
  generic (
    gen_dec1 : integer := 0; -- Comment
    gen_dec2 : integer := 1; -- Comment
    gen_dec3 : integer := 2  -- Comment
  );
  port (
    sig1 : std_logic; -- Comment
    sig2 : std_logic; -- Comment
    sig3 : std_logic  -- Comment
  );
end entity fifo;

-- Failures below
entity fifo is
  generic (
    gen_dec1   : integer := 0; -- Comment
    gen_dec2     : integer := 1; -- Comment
    gen_dec3  : integer := 2  -- Comment
  );
  port (
    sig1     : std_logic; -- Comment
    sig2  : std_logic; -- Comment
    sig3   : std_logic  -- Comment
  );
end entity fifo;

