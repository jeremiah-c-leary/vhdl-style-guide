
architecture RTL of FIFO is

begin

  -- These are passing

  a <= b;
  a <= when c = '0' else '1';
  with z select
     a <= b when z = "000",
          c when z = "001";
  a <= b;
  a <= when c = '0' else '1';

  -- Failing variations

  a <= b;
  a <= when c = '0' else '1';
  with z select
     a <= b when z = "000",
          c when z = "001";
  a <= b;
  a <= when c = '0' else '1';

  -- Testing generate breaks

  a <= b;
  gen : if '1' = '1' generate
    anExtraLoooooooooooooooooooongName <= c;
  end generate gen;
  aSlighltyLongerName <= d;
  b                   <= c;

  a <= b;
  gen : for i in 0 to 7 generate
    anExtraLoooooooooooooooooooongName <= c;
  end generate gen;
  aSlighltyLongerName <= d;
  b                   <= c;

  a                     <= b;
  aSlightlyLooongerName <= c;
  LABEL0 : case a & b & c generate
    when "000" =>
      anExtraLoooooooooooooooooooongName <= c;
      anExtraLoooooooooooongName         <= c;
    when "001" =>
      anExtraLoooooooooooooooongName          <= c;
      anExtraLooooooooooooooooooooooooongName <= c;
  end generate LABEL0;
  aSlighltyLongerName <= d;
  b                   <= c;

end architecture RTL;
