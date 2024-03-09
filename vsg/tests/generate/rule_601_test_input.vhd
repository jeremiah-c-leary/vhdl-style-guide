architecture rtl of test is

begin

  g_label : for gv_index in t_range generate
  end generate g_label;

  -- Violation below

  g_label : for index in t_range generate
  end generate g_label;

  g_label : for range_index in t_range generate
  end generate g_label;

end architecture;
