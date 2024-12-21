package test is

  subtype t_range is natural range 1 to 0;
  type t_u_array_unconstrained is array(natural range <>) of unsigned;

end package;


architecture rtl of fifo is

  subtype t_range is natural range 1 to 0;
  type t_u_array_unconstrained is array(natural range <>) of unsigned;


begin

end architecture rtl;

--  UPPERCASE below

package test is

  subtype t_range is natural RANGE 1 to 0;
  type t_u_array_unconstrained is array(natural RANGE <>) of unsigned;

end package;


architecture rtl of fifo is

  subtype t_range is natural RANGE 1 to 0;
  type t_u_array_unconstrained is array(natural RANGE <>) of unsigned;


begin

end architecture rtl;
