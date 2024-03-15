
architecture RTL of FIFO is

begin

  process

  begin

    if a = '1' then
      b <= '0';
    elsif c = '1' then
      b <= '1';
    else
      if x = '1' then
        z <= '0';
      elsif x = '0' then
        z <= '1';
      else
        z <= 'Z';
      END if;
    END if;

    -- Violations below
    if a = '1' then
      b <= '0';
    elsif c = '1' then
      b <= '1';
    else
      if x = '1' then
        z <= '0';
      elsif x = '0' then
        z <= '1';
      else
        z <= 'Z';
      END if;
    END if;


  end process;

end architecture RTL;
