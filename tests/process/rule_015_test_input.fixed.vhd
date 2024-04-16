
architecture RTL of FIFO is

begin

  process is
  begin
  end process;

  -- Comments are allowed
  PROC_LABEL : process
  begin
  end process;

  -- Violations below
  a <= b;

  process is begin
  end process;

  b <= z;

  PROC_LABEL : process begin
  end process;

end architecture RTL;
