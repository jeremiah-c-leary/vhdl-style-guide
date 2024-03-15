
architecture RTL of FIFO is

begin

  process
  begin

    SIMPLE_LABEL : x := z;
    a := b;

    CONDITIONAL_LABEL : x := z when b = 0 else y;
    x := z when b = 0 else y;

    SELECTED_LABEL : with some_expression select a := b when z = 1;
    with some_expression select a := b when z = 1;

  end process;

end architecture;

-- Violations below

architecture RTL of FIFO is

begin

  process
  begin

    a := b or c -- comment
         d and z
         w or x; -- This should stay

    x := z when b = 0 else  -- check for something
         y;

    with some_expression
     --comment
     select a := b
     --comment
      when z = 1;

  end process;

end architecture;
