
architecture RTL of FIFO is

begin

  process
  begin

    loop

      a <= b;

    end loop;

    loop -- Comment

      a <= b;

    end loop;

    -- Violations below

    loop
 a <= b;

    end loop;

    loop
 a <= b; -- Comment

    end loop;

  end process;

end;
