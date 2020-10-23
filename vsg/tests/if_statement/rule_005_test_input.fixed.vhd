
architecture RTL of FIFO is

begin

  process

  begin

    if (a = '1') then
      b <= '0';
    elsif (b = '0') then
      c <= '1';
    end if;

    -- Violations below
    if (a = '1') then
      b <= '0';
    elsif (b = '0') then
      c <= '1';
    end if;

    if (a = '1') then
      b <= '0';
    elsif (b = '0') then
      c <= '1';
    end if;


  end process;

end architecture RTL;
