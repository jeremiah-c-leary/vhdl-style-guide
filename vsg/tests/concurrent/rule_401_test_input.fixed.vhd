
architecture rtl of fifo is

begin



  wr_data <=
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



end architecture rtl;

