
architecture RTL of FIFO is

  procedure average_samples;

begin

  average_samples;

  PROC1 : process () is
  begin

     average_samples;
     average_samples;
     average_samples;

  end process;

end architecture RTL;
