
architecture RTL of ENTITY_NAME is

begin

  process
  begin

    SEL_LABEL : with some expression select ?
        some target := some expression when some choice | some other choice | some other other choice,
                       some expression when some choice,
                       some expression when some choice | some other choice;

    SEL_LABEL : with some expression select
        some target := some expression when some choice | some other choice | some other other choice,
                       some expression when some choice,
                       some expression when some choice | some other choice;

    with some expression select ?
        some target := some expression when some choice | some other choice | some other other choice,
                       some expression when some choice,
                       some expression when some choice | some other choice;

  end process;

end architecture RTL;
