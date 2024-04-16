
architecture RTL of FIFO is

begin

  process
  begin

    -- Comment
    loop end loop;

    -- Comment
    LOOP_LABEL : loop end loop;

    -- Comment
    while condition loop end loop;

    -- Comment
    for x in (31 downto 0) loop end loop;

    loop end loop;

    LOOP_LABEL : loop end loop;

    while condition loop end loop;

    for x in (31 downto 0) loop end loop;

    -- Violations below

    a <= b;
    loop end loop;

    a <= b;
    LOOP_LABEL : loop end loop;

    a <= b;
    while condition loop end loop;

    a <= b;
    for x in (31 downto 0) loop end loop;

  end process;

end;
