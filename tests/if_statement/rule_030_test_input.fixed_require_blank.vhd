
architecture RTL of FIFO is

begin

  process

  begin

    if a then
      if b then
        if c then
          c <= d;
        end if;
        a <= b;
      end if;
      b <= c;
    end if;

    z <= a;

    -- Violations below

    if a then
      if b then
        if c then
          c <= d;
        end if;
        a <= b;
      end if;
      b <= c;
    end if;

    z <= a;

  end process;

end architecture RTL;
