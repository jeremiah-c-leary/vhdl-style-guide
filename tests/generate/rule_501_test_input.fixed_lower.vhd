
architecture RTL of FIFO is

begin

  FOR_LABEL : for i in 0 to 7 generate
    begin
    end;
  end generate;

  IF_LABEL : if a = '1' generate
    begin
    end;
  end generate;

  CASE_LABEL : case data generate
    when choice =>
      begin
      end;
  end generate;

  -- Violations below

  FOR_LABEL : for i in 0 to 7 generate
    begin
    end;
  end generate;

  IF_LABEL : if a = '1' generate
    begin
    end;
  end generate;

  CASE_LABEL : case data generate
    when choice =>
      begin
      end;
  end generate;

end;
