
architecture RTL of FIFO is

  file defaultImage : load_file_type open read_mode is load_file_name;

  file defaultImage : load_file_type
    open read_mode is load_file_name;

  file defaultImage : load_file_type
    open read_mode
    is load_file_name;

  -- Violations below

  file defaultImage : load_file_type open read_mode is load_file_name;

  file defaultImage : load_file_type
    open read_mode is load_file_name;

  file defaultImage : load_file_type
    open read_mode
    is load_file_name;

begin

end;
