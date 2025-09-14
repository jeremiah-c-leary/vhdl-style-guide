
architecture RTL of FIFO is

begin

  my_proc : process

    variable c_width : integer;

    variable c_width : integer := 16;

    variable c_depth : integer
    := 512;

    variable AVMM_MASTER_NULL  : avmm_master_t := (
      (others => '0'),
      (others => '0'),
      '0',
      '0'
    );

    --! Test stimulus
      CONSTANT c_stimulus : t_stimulus_array :=
      (
          (
              name      => "Hold in reset       ",
              clk_in    => "0101010101010101",
              rst_in    => "1111111111111111",
              cnt_en_in => "0000000000000000",
              cnt_out   => "0000000000000000"
          ),
          (
              name      => "Not enabled         ",
              clk_in    => "0101010101010101",
              rst_in    => "0000000000000000",
              cnt_en_in => "0000000000000000",
              cnt_out   => "0000000000000000"
          )
    );

  begin

  end process;

end architecture RTL;
