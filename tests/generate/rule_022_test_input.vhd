architecture RTL of FIFO is

begin

  gen0 : for i in 0 to 7 generate
  begin
  end generate;

  -- Violations below

  gen1 : for i in 0 to 7 generate
  end generate;

  gen2 : for i in 0 to 7 generate end generate;

end;
