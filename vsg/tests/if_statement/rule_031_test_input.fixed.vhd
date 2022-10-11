
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

    -- Test exceptions

    z <= a;

    if a then
      if b then
        a <= b;
      end if;
    end if;

    z <= a;

    if a then
      if b then
        a <= b;
        if c then
          if d then
            a <= b;
          end if;
        end if;
      end if;
    end if;

  end process;

end architecture RTL;
