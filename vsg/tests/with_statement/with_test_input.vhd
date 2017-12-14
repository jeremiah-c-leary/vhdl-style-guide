
architecture RTL of FIFO is

begin

  with buttons select
    tmp <= "000" when x"1",
           "001" when x"2",
           "010" when x"4",  
           "011" when x"8",
           "100" when others;

end architecture RTL;
