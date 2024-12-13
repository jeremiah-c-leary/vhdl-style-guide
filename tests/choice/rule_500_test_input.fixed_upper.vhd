
architecture RTL of FIFO is

begin

  -- Lower

  with a select b <=
    c when OTHERS;

  a <= (OTHERS => (OTHERS => (OTHERS => '0')));

  process (all) is
  begin

    with a select b <=
      c when OTHERS;

    a <= (OTHERS => (OTHERS => (OTHERS => '0')));

    with a select b :=
      c when OTHERS;

    a := (OTHERS => (OTHERS => (OTHERS => '0')));

    case a is
      when OTHERS =>
        null;
    end case;

  end process;

  case_gen : case a generate
    when OTHERS =>
      a <= b;
  end generate;

  -- Upper

  with a select b <=
    c when OTHERS;

  a <= (OTHERS => (OTHERS => (OTHERS => '0')));

  process (all) is
  begin

    with a select b <=
      c when OTHERS;

    a <= (OTHERS => (OTHERS => (OTHERS => '0')));

    with a select b :=
      c when OTHERS;

    a := (OTHERS => (OTHERS => (OTHERS => '0')));

    case a is
      when OTHERS =>
        null;
    end case;

  end process;

  case_gen : case a generate
    when OTHERS =>
      a <= b;
  end generate;

end architecture RTL;
