
entity fifo is
  generic (
    gen_dec1   : integer := 0; -- Comment
    gen_dec2   : integer := 1; -- Comment
    gen_dec3   : integer := 1; -- Comment
    gen_dec4   : integer := 1; -- Comment

    gen_dec5   : integer := 1; -- Comment
    gen_dec6   : integer := 1; -- Comment
    gen_dec7   : integer := 1; -- Comment
    -- Comment
    gen_dec3  : integer := 2 -- Comment
  );
  port (
    sig1     : std_logic := '0'; -- Comment
    sig2     : std_logic := '1'; -- Comment
    sig3     : std_logic := '1'; -- Comment
    sig4     : std_logic := '1'; -- Comment
    --Comment
    sig5     : std_logic := '1'; -- Comment
    sig6     : std_logic := '1'; -- Comment

    sig7     : std_logic := 'Z' -- Comment
  );
end entity fifo;
