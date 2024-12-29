package test is

  type t_u_array is array(1 downto 0) of unsigned;

  type t_u_array_unconstrained is array(natural range <>) OF unsigned;

end package test;

package test is

  type t_u_array is array(1 downto 0) OF unsigned;

  type t_u_array_unconstrained is array(natural range <>) OF unsigned;

end package test;
