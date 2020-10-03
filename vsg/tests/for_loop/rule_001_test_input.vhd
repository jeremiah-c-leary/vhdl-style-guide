
architecture RTL of FIFO is

begin

  process
  begin

    FOR_LABEL : for index in 4 to 23 loop

    end loop;

    for index in 4 to 23 loop

    end loop;

    for index in 4 to 23 loop

      for j in 0 to 127 loop

      end loop;

    end loop;

    -- Violations below

      FOR_LABEL : for index in 4 to 23 loop

    end loop;

for index in 4 to 23 loop

    end loop;

     for index in 4 to 23 loop

   for j in 0 to 127 loop

      end loop;

    end loop;

  end process;

end;
