
architecture RTL of FIFO is

begin

  process
  begin

    LOOP_LABEL :
      loop end loop;

    LOOP_LABEL :    -- Comment
      loop end loop;

    LOOP_LABEL : loop end loop;

    LOOP_LABEL :loop end loop;

    LOOP_label :    loop end loop;



    FOR_LABEL :
      for index in 4 to 23 loop end loop;

    FOR_LABEL :    -- Comment
      for index in 4 to 23 loop end loop;

    FOR_LABEL : for index in 4 to 23 loop end loop;

    FOR_LABEL :for index in 4 to 23 loop end loop;

    FOR_LABEL :    for index in 4 to 23 loop end loop;



    WHILE_LABEL :
      while condition loop end loop;

    WHILE_LABEL :      -- Comment
      while condition loop end loop;

    FOR_LABEL : while condition loop end loop;

    FOR_LABEL :while condition loop end loop;

    FOR_LABEL :    while condition loop end loop;

  end process;

end;
