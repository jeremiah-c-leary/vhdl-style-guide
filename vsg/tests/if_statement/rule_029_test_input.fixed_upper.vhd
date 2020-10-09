
architecture RTL of FIFO is

begin

  process

  begin

    if a = '1' THEN
      b <= '0';
    elsif c = '1' THEN
      b <= '1';
    else
      if x = '1' THEN
        z <= '0';
      elsif x = '0' THEN
        z <= '1';
      else
        z <= 'Z';
      end if;
    end if;

    -- Violations below
    if a = '1' THEN
      b <= '0';
    elsif c = '1' THEN
      b <= '1';
    else
      if x = '1' THEN
        z <= '0';
      elsif x = '0' THEN
        z <= '1';
      else
        z <= 'Z';
      end if;
    end if;


  end process;

end architecture RTL;
