
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
      end if;
    end if;

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
      end if;
    end if;

    -- case statement override

    if a = '1' then

        case x is
        end case;

    elsif c = '1' then

    end if;

    -- loop statement override

    if a = '1' then

        loop
        end loop;

    elsif c = '1' then

    end if;

  end process;

end architecture RTL;
