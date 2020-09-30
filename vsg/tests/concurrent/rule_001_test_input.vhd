
architecture RTL of FIFO is

begin

  -- These are passing

  SIG_LABEL : postponed a <= b;

  SIG_LABEL : postponed a <= when c = '0' else '1';

  SIG_LABEL : postponed with z select
     a <= b when z = "000",
          c when z = "001";

  -- Failing variations

    SIG_LABEL : postponed a <= b;

SIG_LABEL : postponed a <= when c = '0' else '1';

   SIG_LABEL : postponed with z select
     a <= b when z = "000",
          c when z = "001";

   -- Remove the labels

    postponed a <= b;

postponed a <= when c = '0' else '1';

   postponed with z select
     a <= b when z = "000",
          c when z = "001";

   -- Remove the postponed keyword

    a <= b;

a <= when c = '0' else '1';

   with z select
     a <= b when z = "000",
          c when z = "001";

end architecture RTL;
