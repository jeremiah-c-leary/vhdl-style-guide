
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
      end IF;
    end IF;

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
      end IF;
    end IF;


  end process;

end architecture RTL;
