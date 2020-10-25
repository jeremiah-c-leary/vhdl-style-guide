
architecture RTL of FIFO is

begin

  process
  begin

    if (rst = c_asserted) then
    elsif (clk'event and clk = '1') then
    end if;

    if (rst = c_asserted) then
    elsif (clk'event and clk = '0') then
    end if;

    if (rst = c_asserted) then
    elsif (clk'event and clk = '1') then
    end if;

    if (rst = c_asserted) then
    elsif (clk'event and clk = '0') then
    end if;

  end process;

end architecture RTL;
