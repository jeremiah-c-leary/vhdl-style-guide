
architecture rtl of fifo is

begin

  test1 <= reject 2 ns inertial 0 after 10 ns;

  test1 <= reject 2 ns INERTIAL 0 after 10 ns;

end architecture;
