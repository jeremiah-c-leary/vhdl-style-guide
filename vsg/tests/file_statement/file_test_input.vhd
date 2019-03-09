
architecture RTL of FIFO is

  file defaultImage : load_file_type open read_mode is load_file_name;

  file defaultImage : load_file_type open read_mode
    is load_file_name;

   FILE     defaultImage : load_file_type open read_mode is load_file_name;

file defaultImage : load_file_type open read_mode
        is load_file_name;

begin

  U_INST : INST
  generic map (
    FILENAME => string'("out.txt")
  )
  port map (
    FILENAME => string'("out.txt")
  );

  FILE_PROC : process (filename) is

    file defaultImage : load_file_type open read_mode is load_file_name;
 
  begin
  
    FILENAME <= '1';

  end process FILE_PROC;


  

end architecture RTL;
