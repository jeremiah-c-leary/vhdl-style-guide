
architecture RTL of FIFO is

begin

  -- Basic version
  with sel select
    out1 <= a when "00",
            b when "01",
            c when "10",
            d when others;


  --with guarded keyword
  with sel select
    out1 <= guarded a when "00",
                    b when "01",
                    c when "10",
                    d when others;


  --with transport delay mechanism
  with sel select
    out1 <= transport a when "00",
                      b when "01",
                      c when "10",
                      d when others;

  --with inertial delay mechanism
  with sel select
    out1 <= inertial a when "00",
                     b when "01",
                     c when "10",
                     d when others;

  --with reject inertial delay mechanism
  with sel select
    out1 <= reject 10 ns inertial a when "00",
                                  b when "01",
                                  c when "10",
                                  d when others;

end architecture RTL;
