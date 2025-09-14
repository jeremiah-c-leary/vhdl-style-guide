
architecture rtl of fifo is

begin

  my_proc : process

    variable wr_data : my_type :=
    (
      (name => "Hold in reset",
        clk_in => "01",
        rst_in => "11",
        cnt_en_in => "00",
        cnt_out => "00"),
      (name => "Not enabled",
        clk_in => "01",
        rst_in => "00",
        cnt_en_in => "00",
        cnt_out => "00")
    );

    variable d : my_type :=
            (d2 xor to_stdulogic(gen2)) &
            (d1 xor to_stdulogic(gen1));

  begin

  end process;

end architecture rtl;
