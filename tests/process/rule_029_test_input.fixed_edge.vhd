
architecture RTL of FIFO is

begin

  process
  begin

    if (rst = c_asserted) then
    elsif (rising_edge(clk)) then
    end if;

    if (rst = c_asserted) then
    elsif (falling_edge(clk)) then
    end if;

    if (rst = c_asserted) then
    elsif (rising_edge(clk)) then
    end if;

    if (rst = c_asserted) then
    elsif (falling_edge(clk)) then
    end if;

  end process;

end architecture RTL;
