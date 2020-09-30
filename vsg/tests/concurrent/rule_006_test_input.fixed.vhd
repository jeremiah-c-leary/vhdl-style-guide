
architecture RTL of FIFO is

begin

  -- These are passing

  a <= b;
  a <= when c = '0' else '1';
  with z select
     a <= b when z = "000",
          c when z = "001";
  a <= b;
  a <= when c = '0' else '1';

  -- Failing variations

  a <= b;
  a <= when c = '0' else '1';
  with z select
     a <= b when z = "000",
          c when z = "001";
  a <= b;
  a <= when c = '0' else '1';

end architecture RTL;
