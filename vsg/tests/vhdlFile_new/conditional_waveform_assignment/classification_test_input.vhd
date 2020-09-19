
architecture RTL of ENTITY_NAME is

begin

  process
  begin

    SEL_LABEL : some target <= transport some expression when some condition else
                                         some expression when some condition else
                                         some expression;

    SEL_LABEL : some target <= some expression when some condition else
                               some expression when some condition else
                               some expression;

    SEL_LABEL : some target <= some expression when some condition else
                               some expression when some condition;

    SEL_LABEL : some target <= some expression when some condition;

    -- Remove the labels

    some target <= transport some expression when some condition else
                             some expression when some condition else
                             some expression;

    some target <= some expression when some condition else
                   some expression when some condition else
                   some expression;

    some target <= some expression when some condition else
                   some expression when some condition;

    some target <= some expression when some condition;

  end process;

end architecture RTL;
