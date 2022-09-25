
architecture rtl of fifo is begin

  process is begin

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

  end process;

end architecture rtl;
