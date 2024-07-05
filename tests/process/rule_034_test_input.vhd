
architecture RTL of FIFO is

begin


  process

    variable var1  : integer := 0;                                    -- Comment 1
    file     file1 : load_file_file open read_mode is load_file_name; -- Comment 2
    constant con1  : std_logic := '1';                                -- Comment 3

  begin
  end process;

  -- Violations below

  process

    variable var1 : integer := 0;-- Comment
    file     file1: load_file_file open read_mode is load_file_name;     -- Comment
    constant con1    : std_logic := '1';                                          -- Comment

  begin
  end process;


end architecture RTL;
