
architecture rtl of fifo is

begin

  with mux_sel select addr <=
    c_input_data when 0,
    c_output_data when 1,
    (others => 'X') when others;

  with mux_sel select addr <=
    c_input_data_2           when 0,
    c_output_data_2    when 1,
    (others => 'X')               when others;


end architecture rtl;
