
architecture RTL of ENTITY_NAME is

begin

  process
  begin

    SEL_LABEL : with some expression select ?
        some target <= transport some expression when some choice | some other choice | some other other choice,
                                 some expression when some choice,
                                 some expression when some choice | some other choice;


    SEL_LABEL : with some expression select ?
        some target <= some expression when some choice | some other choice | some other other choice,
                       some expression when some choice,
                       some expression when some choice | some other choice;


    SEL_LABEL : with some expression select
        some target <= transport some expression when some choice | some other choice | some other other choice,
                                 some expression when some choice,
                                 some expression when some choice | some other choice;


    SEL_LABEL : with some expression select ?
        some target <= transport some expression when some choice;


    with some expression select ?
        some target <= some expression when some choice | some other choice | some other other choice,
                       some expression when some choice,
                       some expression when some choice | some other choice;

    with some expression select ?
        some target <= some expression after 10 ns when some choice | some other choice | some other other choice,
                       null when some choice,
                       null after 20 ns when some choice | some other choice,
                       some expression after 10 ns, some other expression after 20 ns, some last expression when some choice | some other choice,
                       unaffected when some last choice;

  end process;

end architecture RTL;
