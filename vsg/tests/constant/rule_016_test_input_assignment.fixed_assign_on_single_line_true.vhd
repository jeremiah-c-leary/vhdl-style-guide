
architecture rtl of fifo is

  constant cons1 : t_type :=
 (
    1 => func1(std_logic_vector(G_GEN), G_GEN2),
 2 => func1(std_logic_vector(G_GEN3), G_GEN4)
 );

  constant cons1 : t_type :=
 (
    1 => func1(std_logic_vector(G_GEN), G_GEN2),
    2 => func1( std_logic_vector(G_GEN3), G_GEN4)
  );

  constant cons1 : t_type :=
 (
    1 => func1(std_logic_vector(G_GEN), G_GEN2),
    (others => '0'),
    2 => func2(std_logic(  G_GEN), G_GEN2)
 );

begin

end architecture rtl;
