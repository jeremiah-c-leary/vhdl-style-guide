
architecture RTL of FIFO is

begin

  process_and_or : process(a,b,d,e) is
    signal a : std_logic;
  begin
    g <= (a and b) or (d and e);
  end process process_and_or;

  process_and_or : postponed process(a,b,d,e) is
    signal a : std_logic;
  begin
    g <= (a and b) or (d and e);
  end postponed process process_and_or;

  process_and_or : postponed process is
  begin
  end postponed process process_and_or;

  process_and_or : postponed process
  begin
  end postponed process process_and_or;

  process_and_or : process
  begin
  end process process_and_or;

  process
  begin
  end process;

  process is
  begin
  end process;

end architecture RTL;
