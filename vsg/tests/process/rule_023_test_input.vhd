
architecture RTL of FIFO is

begin


  process 
  begin

    a <= b;

  end process;

  -- Violations below

  process 
  begin

    a <= b;
  end process;


end architecture RTL;
