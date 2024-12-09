
architecture RTL of FIFO is

begin


  process

    variable var1   : integer := 0;
    file     file1  : load_file_file open read_mode is load_file_name;
    constant con1   : std_logic := '1';
    alias    alias1 is name;
    alias    alias1 : subtype_indicator is name;

  begin
  end process;

  -- Violations below

  process

    variable var1   : integer := 0;
    file     file1  : load_file_file open read_mode is load_file_name;
    constant con1   : std_logic := '1';
    alias    alias1 is name;
    alias    alias1 : subtype_indicator is name;

  begin
  end process;

  process

    procedure some_procedure (count : integer) is

      variable v_count      : std_logic_vector(SOME_CONSTANT - 1 downto 0);

    begin

    end procedure;

    variable var1   : integer := 0;
    file     file1  : load_file_file open read_mode is load_file_name;
    constant con1   : std_logic := '1';
    alias    alias1 is name;
    alias    alias1 : subtype_indicator is name;

  begin end process;

  process

    variable var1   : integer := 0;
    file     file1  : load_file_file open read_mode is load_file_name;
    constant con1   : std_logic := '1';
    alias    alias1 is name;
    alias    alias1 : subtype_indicator is name;

    constant c_abc      : integer;
    type flag_pt is protected body
      variable flag  : boolean;
    end protected body;
    constant constant_1 : integer;
  begin end process;

end architecture RTL;
