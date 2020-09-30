
architecture RTL of FIFO is

begin

  -- These are passing

  postponed a <= b;

  postponed a <= when c = '0' else '1';

  postponed with z select
     a <= b when z = "000",
          c when z = "001";

  a <= b;

  a <= when c = '0' else '1';

  with z select
     a <= b when z = "000",
          c when z = "001";

  -- These are failing

  postponed a <= b;

  postponed a <= when c = '0' else '1';

  postponed with z select
     a <= b when z = "000",
          c when z = "001";

end architecture RTL;
