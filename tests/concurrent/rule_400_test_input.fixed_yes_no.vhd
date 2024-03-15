
architecture rtl of fifo is begin

  s_foo <= (
            item         => 12,
            another_item => 34
          );

  s_foo <= (
            item         => 12,
            another_item => 34
          );

  s_foo <= ( item1 => 12,
             item2 => f(a, b ,c),
             item3 => 36
           );

  s_foo <= (a and
            b and
            c);

  -- Test hierarchical assignments

  test_signal <= (
    others => (
      data => (others => '0'),
      update_pulse => '0'
    )
  );

  test_signal <= (
    others => (
      data => (others => '0'),
      update_pulse => '0'
    )
  );

end architecture rtl;
