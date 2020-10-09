
architecture RTL of FIFO is

begin

  process

  begin

    if a = '1' then
      b <= '0';
    ELSIF c = '1' then
      b <= '1';
    else
      if x = '1' then
        z <= '0';
      ELSIF x = '0' then
        z <= '1';
      else
        z <= 'Z';
      end if;
    end if;

    -- Violations below
    if a = '1' then
      b <= '0';
    ELSIF c = '1' then
      b <= '1';
    else
      if x = '1' then
        z <= '0';
      ELSIF x = '0' then
        z <= '1';
      else
        z <= 'Z';
      end if;
    end if;


  end process;

end architecture RTL;
