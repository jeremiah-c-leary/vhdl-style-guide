
architecture RTL of FIFO is

begin

  GEN_FOR_LABEL : for i in 0 to 7 generate

  end generate GEN_FOR_LABEL;

  GEN_IF_LABEL : if a = '1' generate

  end generate GEN_IF_LABEL;

  GEN_CASE_LABEL : case data generate

  end generate GEN_CASE_LABEL;

  -- Violations below

  FOR_LABEL : for i in 0 to 7 generate

  end generate FOR_LABEL;

  IF_LABEL : if a = '1' generate

  end generate IF_LABEL;

  CASE_LABEL : case data generate

  end generate CASE_LABEL;

end;
