
architecture RTL of FIFO is

begin

  -- These are passing

  a <= b or
       d;

  a <= '0' when c = '0' else
       '1' when d = '1' else
       'Z';

  with z select
     a <= b when z = "000",
          c when z = "001";

  -- Failing variations

  a <= b or

       d;

  a <= '0' when c = '0' else

       '1' when d = '1' else

       'Z';

  with z select

     a <= b when z = "000",

          c when z = "001";

end architecture RTL;
