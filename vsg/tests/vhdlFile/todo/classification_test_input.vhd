
architecture rtl of fifo is

begin

  a <= b('0');

  a <= b(x, y, z);

  a <= b(x(3, 4, 5), y(6, 7, 8), z(9, 0, 1));

  a <= (x(3, 4, 5), y(6, 7, 8), z(9, 0, 1));

  a <= ((3, 4, 5), (6, 7, 8), (9, 0, 1));

  a <= a, b;

  a <= b(x => 3, y => 2, z => 1);

 end architecture;
