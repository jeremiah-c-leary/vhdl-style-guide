
architecture rtl of fifo is

  constant c_zeros : std_logic_vector(7 downto 0) := (others => '0');
  constant c_one   : std_logic_vector(7 downto 0) := (0 => '1', (others => '0'));
  constant c_two   : std_logic_vector(7 downto 0) := (1 => '1', (others => '0'));

  constant c_stimulus : t_stimulus_array := ((name => "Hold in reset", clk_in => "01", rst_in => "11", cnt_en_in => "00", cnt_out => "00"), (name => "Not enabled", clk_in => "01", rst_in => "00", cnt_en_in => "00", cnt_out => "00"));

  constant c_stimulus : t_stimulus_array := (
                      (name => "Hold in reset", clk_in => "01", rst_in => "11", cnt_en_in => "00", cnt_out => "00"), (name => "Not enabled", clk_in => "01", rst_in => "00", cnt_en_in => "00", cnt_out => "00"));

  constant c_stimulus : t_stimulus_array :=
     ((name => "Hold in reset", clk_in => "01", rst_in => "11", cnt_en_in => "00", cnt_out => "00"), (name => "Not enabled", clk_in => "01", rst_in => "00", cnt_en_in => "00", cnt_out => "00"));

  constant c_stimulus : t_stimulus_array :=
((name => "Hold in reset", clk_in => "01", rst_in => "11", cnt_en_in => "00", cnt_out => "00"), (name => "Not enabled", clk_in => "01", rst_in => "00", cnt_en_in => "00", cnt_out => "00"));

  constant c_stimulus : t_stimulus_array :=
  (
    (name => "Hold in reset", clk_in => "01", rst_in => "11", cnt_en_in => "00", cnt_out => "00"),
    (name => "Not enabled", clk_in => "01", rst_in => "00", cnt_en_in => "00", cnt_out => "00"));

  constant c_stimulus : t_stimulus_array :=
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
      cnt_out => "00"));

  constant c_stimulus : t_stimulus_array :=
  (
    (
      name => "Hold in reset",
      clk_in => "01",
      rst_in => "11",
      cnt_en_in => "00",
      cnt_out => "00"),
    (
      name => "Not enabled",
      clk_in => "01",
      rst_in => "00",
      cnt_en_in => "00",
      cnt_out => "00"));

  constant c_stimulus : t_stimulus_array :=
  (
    (
      name => "Hold in reset",
      clk_in => "01",
      rst_in => "11",
      cnt_en_in => "00",
      cnt_out => "00"
    ),
    (
      name => "Not enabled",
      clk_in => "01",
      rst_in => "00",
      cnt_en_in => "00",
      cnt_out => "00"
    ));

begin

end architecture rtl;
