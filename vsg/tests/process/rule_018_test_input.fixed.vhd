
architecture RTL of FIFO is

begin

  process is begin end process;

  PROC_LABEL : process is
  begin
  end process PROC_LABEL;

  -- Violations below

  PROC_LABEL : process is
  begin
  end process PROC_LABEL;

  process is
  begin
  end process;

end architecture RTL;
