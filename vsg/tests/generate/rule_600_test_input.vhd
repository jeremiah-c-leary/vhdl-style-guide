
architecture RTL of FIFO is

begin

  FOR_LABEL_GEN : for i in 0 to 7 generate

  end generate FOR_LABEL_GEN;

  IF_LABEL_GEN : if a = '1' generate

  end generate IF_LABEL_GEN;

  CASE_LABEL_GEN : case data generate

  end generate CASE_LABEL_GEN;

  -- Violations below

  FOR_LABEL : for i in 0 to 7 generate

  end generate FOR_LABEL;

  IF_LABEL : if a = '1' generate

  end generate IF_LABEL;

  CASE_LABEL : case data generate

  end generate CASE_LABEL;

end;
