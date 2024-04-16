
architecture RTL of FIFO is

begin

  process
  begin

    for x in (0 to 30) loop

    end loop;

    loop

    end loop;

    -- Violations below

    for x in (0 to 30) loop

    end loop;

    for x in (0 to 30) loop

    end loop;

  end process;

end;
