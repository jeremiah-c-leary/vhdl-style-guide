
architecture RTL of FIFO is

begin

  process

  begin

    z <= a;

    if a then
      a <= b;
      if b then
        b <= c;
        if c then
        c <= d;
        end if;
      end if;
    end if;

    -- Comment
    if a then
      a <= b;
      if b then
        b <= c;
        if c then
        c <= d;
        end if;
      end if;
    end if;

    -- Violations below

    z <= a;
    if a then
      a <= b;
      if b then
        b <= c;
        if c then
        c <= d;
        end if;
      end if;
    end if;

  end process;

end architecture RTL;
