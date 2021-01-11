
architecture RTL of FIFO is

begin


  process

    variable var1  : integer := 0;
    file     file1 : load_file_file open read_mode is load_file_name;
    constant con1  : std_logic := '1';

  begin
  end process;

  -- Violations below

  process

    variable var1  : integer := 0;
    file     file1 : load_file_file open read_mode is load_file_name;
    constant con1  : std_logic := '1';

  begin
  end process;


end architecture RTL;
