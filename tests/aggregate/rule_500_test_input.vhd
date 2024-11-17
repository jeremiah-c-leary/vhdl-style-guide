
architecture rtl of test is

  signal sig : signed := (others => '0');

  function my_func (
    test : t_counter := (others => '0')
  ) return integer is
  begin
    return (others => '0');
  end function;

begin

  a <=
  (
    1      => '1',
    others => '0'
  );
  a <= (
         1 => '1',
         others => '0'
       ) when condition else
       (others => '0');
  with condition select a <=
    (others => '1') when x,
    (others => '0') when others;

  process is

    constant con : signed := (others => '0');
    variable var : signed := (others => '0');

  begin

    a <=
    (
      1      => '1',
      others => '0'
    );
    a <= (
           1 => '1',
           others => '0'
         ) when condition else
         (others => '0');
    with condition select a <=
    (others => '1') when x,
    (others => '0') when others;

    a :=
    (
      1 => '1',
      others => '0'
    );
    a := (
           1 => '1',
           others => '0'
         ) when condition else
         (others => '0');
    with condition select a :=
    (others => '1') when x,
    (others => '0') when others;

    case expression is

      when others =>

        null;

    end case;

  end process;

end architecture rtl;

architecture rtl of test is

  signal sig : signed := (OTHERS => '0');

  function my_func (
    test : t_counter := (OTHERS => '0')
  ) return integer is
  begin
    return (OTHERS => '0');
  end function;

begin

  a <=
  (
    1      => '1',
    OTHERS => '0'
  );
  a <= (
         1 => '1',
         OTHERS => '0'
       ) when condition else
       (OTHERS => '0');
  with condition select a <=
    (OTHERS => '1') when x,
    (OTHERS => '0') when others;

  process is

    constant con : signed := (OTHERS => '0');
    variable var : signed := (OTHERS => '0');

  begin

    a <=
    (
      1      => '1',
      OTHERS => '0'
    );
    a <= (
           1 => '1',
           OTHERS => '0'
         ) when condition else
         (OTHERS => '0');
    with condition select a <=
    (OTHERS => '1') when x,
    (OTHERS => '0') when others;

    a :=
    (
      1 => '1',
      OTHERS => '0'
    );
    a := (
           1 => '1',
           OTHERS => '0'
         ) when condition else
         (OTHERS => '0');
    with condition select a :=
    (OTHERS => '1') when x,
    (OTHERS => '0') when others;

    case expression is

      when others =>

        null;

    end case;

  end process;

end architecture rtl;
