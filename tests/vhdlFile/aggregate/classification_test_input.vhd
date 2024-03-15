
architecture rtl of fifo is begin

  s_foo <= (
            item    => 12,
            another_item => 34
          );

  proc_label : process is

  begin

    s_foo <= (
              item     => 12,
              another_item => 34
            );

  end process proc_label;

  s_foo <= ( item1 => 12,
             item2 => f(a, b ,c),
             item3 => 36,
             item4 => (
               itemA => 3,
               itemB => 4
             )
           );

end architecture rtl;
