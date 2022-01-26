
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

  process

    procedure some_procedure (count : integer) is

      variable v_count      : std_logic_vector(SOME_CONSTANT - 1 downto 0);

    begin

    end procedure;

    variable var1  : integer := 0;
    file     file1 : load_file_file open read_mode is load_file_name;
    constant con1  : std_logic := '1';

  begin end process;

end architecture RTL;
