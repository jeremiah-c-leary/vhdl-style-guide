
architecture RTL of FIFO is

begin

  FOR_LABEL : for i in 0 to 7 generate

  end generate for_label;

  IF_LABEL : if a = '1' generate

  end generate if_label;

  CASE_LABEL : case data generate

  end generate case_label;

  -- Violations below

  FOR_LABEL : for i in 0 to 7 generate

  end generate for_label;

  IF_LABEL : if a = '1' generate

  end generate if_label1;

  CASE_LABEL : case data generate

  end generate case_label;

end;
