
architecture RTL of FIFO is

begin

  process
  begin

    SIMPLE_LABEL : x := z;
    a := b;
    (a, b) := c;

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

    SIMPLE_LABEL : x := z;
    SIMPLE_LABEL : x := z;
    a := b;
    a := b;
    (a, b) := c;
    (a, b) := c;

    CONDITIONAL_LABEL : x := z when b = 0 else y;
    CONDITIONAL_LABEL : x := z when b = 0 else y;
    x := z when b = 0 else y;
    x := z when b = 0 else y;

    SELECTED_LABEL : with some_expression select a := b when z = 1;
    SELECTED_LABEL : with some_expression select a := b when z = 1;
    with some_expression select a := b when z = 1;
    with some_expression select a := b when z = 1;


  end process;

end architecture;


-- Test aggregates

architecture rtl of fifo is

begin

  process
  begin

    (
      a,
      b,
      c
    ) := z;

    (
      a,
      b,
      c
    ) := z;

  end process;

end architecture rtl;
