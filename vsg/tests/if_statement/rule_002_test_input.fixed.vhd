
architecture RTL of FIFO is

begin

  process

  begin

    if (a = '1') then
      b <= '0';
    elsif (c = '1') then
      b <= '1';
    elsif (a(3 downto 0) = 0) then
      b <= '0';
    elsif (a(3 downto 0) + f(34, 56, 72) - g(f(35, 25, 60) downto h(45, 32))) then
      b <= '1';
    end if;

    -- Violations below

    if (a = '1') then
      b <= '0';
    elsif (c = '1') then
      b <= '1';
    elsif (a(3 downto 0) = 0) then
      b <= '0';
    elsif (a(3 downto 0) + f(34, 56, 72) - g(f(35, 25, 60) downto h(45, 32))) then
      b <= '1';
    end if;

  end process;

end architecture RTL;
