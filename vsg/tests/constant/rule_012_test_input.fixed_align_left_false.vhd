
architecture rtl of fifo is

  constant cons1 : t_type := (
                              1 => func1(
                                         G_GENERIC1, G_GENERIC2),
                              2 => func2(
                                         func3(func4(
                                                     func5(
                                                           G_GENERIC3
                                                          )
                                                    )
                                              )
                                        )
                             );

begin end architecture rtl;
