

entity fifo is
  generic (
    gen_dec1 : integer := 0; -- Comment
    gen_dec2 : integer := 1; -- Comment
    gen_dec3 : integer := 2  -- Comment
  );
  port (
    sig1 : std_logic := '0'; -- Comment
    sig2 : std_logic := '1'; -- Comment
    sig3 : std_logic := 'Z' -- Comment
  );
end entity fifo;

-- Failures below
entity fifo is
  generic (
    gen_dec1   : integer   := 0; -- Comment
    gen_dec2     : integer := 1; -- Comment
    gen_dec3  : integer    := 2  -- Comment
  );
  port (
    sig1     : std_logic := '0'; -- Comment
    sig2  : std_logic    := '1'; -- Comment
    sig3   : std_logic   := 'Z' -- Comment
  );
end entity fifo;
