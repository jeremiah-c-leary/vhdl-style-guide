
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
	((name => "Hold in reset", clk_in => "01", rst_in => "11", cnt_en_in => "00", cnt_out => "00"), (name => "Not enabled", clk_in => "01", rst_in => "00", cnt_en_in => "00", cnt_out => "00")
	);

  constant c_stimulus : t_stimulus_array :=
	(
	 (name => "Hold in reset", clk_in => "01", rst_in => "11", cnt_en_in => "00", cnt_out => "00"),
	 (name => "Not enabled", clk_in => "01", rst_in => "00", cnt_en_in => "00", cnt_out => "00")
	);

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
	  cnt_out => "00")
	);

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
	  cnt_out => "00")
	);

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
	 )
	);

begin

  proc_label : process

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
		 )
		);

  begin end process;


end architecture rtl;

architecture rtl of fifo is

  constant avmm_master_null : avmm_master_t := (
	                                              (others => '0'),
	                                              (others => '0'),
	                                              '0',
	                                              '0'
	                                             );

begin end architecture rtl;

architecture rtl of fifo is

  constant cons1 : t_type := (
	                            1 => func1(
	                                       G_GENERIC1, G_GENERIC2),
	                            2 => func2(
	                                       func3(func4(
	                                                   func5(
	                                                         G_GENERIC3
	                                                        )
	                                                  )
	                                            )
	                                      )
	                           );

  constant cons1 : t_type := (1 => func1(
	                                       G_GENERIC1, G_GENERIC2),
	                            2 => func2(
	                                       func3(func4(
	                                                   func5(G_GENERIC3))
	                                            ))
	                           );

  constant cons1 : t_type := (1 => func1(G_GENERIC1, G_GENERIC2),
	                            2 => func2(func3(func4(
	                                                   func5(G_GENERIC3))
	                                            )));

  constant cons1 : t_type :=
	(
	 1 => func1(
	            G_GENERIC1, G_GENERIC2),
	 2 => func2(
	            func3(func4(
	                        func5(
	                              G_GENERIC3
	                             )
	                       )
	                 )
	           )
	);

begin end architecture rtl;

architecture rtl of fifo is

  constant cons1 : t_type := '0';

  constant cons2 : t_type := '0' and '1'
       and '0' or '1';

  constant cons2 : t_type := func1(G_GENERIC1, G_GENERIC_2,
        func2(G_GENERIC3));

begin end architecture rtl;
