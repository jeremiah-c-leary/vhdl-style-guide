
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

    -- Check loop statements

    if a = '1' then

    else

        LOOP_LABEL : loop
        end loop;
    end if;

    if a = '1' then

    else

        loop
        end loop;
    end if;

    if a = '1' then

    else

        while a = 0
        loop
        end loop;
    end if;

    if a = '1' then

    else

        for i in 0 to 13
        loop
        end loop;
    end if;

  end process;

end architecture RTL;
