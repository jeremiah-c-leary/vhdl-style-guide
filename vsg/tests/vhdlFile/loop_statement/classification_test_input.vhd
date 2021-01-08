
architecture RTL of ENTITY_NAME is

begin

  process

  begin

    WHILE_LABEL : while a < 50 loop

        null;

    end loop WHILE_LABEL;

    while a < 50 loop

        null;

    end loop;


    FOR_LABEL : for count in 1 to 8 loop

        null;

    end loop FOR_LABEL;


    for count in 1 to 8 loop

        null;

    end loop;


    loop

        null;

    end loop;

    FOR_LABEL : loop
      null;
    end loop;

  end process;

end architecture RTL;
