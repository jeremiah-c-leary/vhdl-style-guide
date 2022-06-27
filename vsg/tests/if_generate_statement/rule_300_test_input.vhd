
architecture RTL of FIFO is

begin

  IF_LABEL : if a = '1' generate

  elsif a = '0' generate

  end generate;

  -- Violations below

  IF_LABEL : if a = '1' generate

elsif a = '0' generate

  end generate;


  IF_LABEL : if a = '1' generate

     elsif a = '0' generate

  end generate;

end;
