
architecture RTL of ENTITY_NAME is

  function func1 return integer is
  begin
    hpp := '1'  when (pf_vlan2x_tci(3 downto 0) >= x"A" and pf_vlan2x_tci(3 downto 0) <= x"F") else '0';
    hpp := '1' when a >= b and x <= y else '0';
    other_target <= '0' when x <= y;
  end function;

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
