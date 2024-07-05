
architecture RTL of FIFO is

begin

  process
  begin

    loop
      a <= b;
    end loop;

    c <= d;

    -- Violations below

    loop
      a <= b;
    end loop;
    c <= d;

  end process;

end;
