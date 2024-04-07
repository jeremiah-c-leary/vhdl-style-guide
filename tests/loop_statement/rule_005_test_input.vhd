
architecture RTL of FIFO is

begin

  process
  begin

    LOOP_LABEL: loop end loop;

    LOOP_LABEL: while condition loop end loop;

    LOOP_LABEL: for x in range(15 downto 0) loop end loop;


    LOOP_LABEL:
      loop end loop;

    LOOP_LABEL:
      while condition loop end loop;

    LOOP_LABEL:
      for x in range(15 downto 0) loop end loop;

  end process;

end;
