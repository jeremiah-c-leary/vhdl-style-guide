architecture RTL of FIFO is

  attribute Component_symbol of Comp_1 [name1, name2 return integer], Comp2 [name3, name4 return std_logic], Comp3 [name5, name6 return std_logic_vector] : component is "Counter_16";

  attribute Component_symbol of Comp_1 [name1, name2 return integer] : component is "Counter_16";

  attribute Component_symbol of Comp_1 : component is "Counter_16";

  attribute Coordinate of Comp_1: component is (0.0, 17.5);

  attribute Pin_code of Sig_1: signal is 17;

  attribute Max_delay of Const_1: constant is 10 ns;

begin

end architecture RTL;
