
architecture RTL of FIFO is

begin

  FOR_LABEL : for i in 0 to 7 generate

  end generate;

  IF_LABEL : if a = '1' generate

  end generate;

  CASE_LABEL : case data generate

  end generate;

  -- Violations below

  FOR_LABEL
  : for i in 0 to 7 generate

  end generate;

  IF_LABEL
  : if a = '1' generate

  end generate;

  CASE_LABEL
  : case data generate

  end generate;

end;
