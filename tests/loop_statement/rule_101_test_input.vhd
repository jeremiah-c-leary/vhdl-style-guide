
architecture RTL of FIFO is

begin

  process
  begin

    loop

    end loop END_LOOP_LABEL;

    -- Violations below

    loop

    end loop   END_LOOP_LABEL;

  end process;

end;
