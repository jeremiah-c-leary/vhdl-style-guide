
architecture rtl of fifo is

begin

  gen0 : if condition generate
  begin
  end generate;

  -- Violations below

  gen1 : if condition generate begin
  end generate;

  gen2 : if condition generate begin end generate;

end;
