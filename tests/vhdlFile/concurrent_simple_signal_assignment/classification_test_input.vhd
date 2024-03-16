
architecture RTL of FIFO is

begin

  -- Simple form
  a <= b;

  -- with guarded
  a <= guarded b;

  -- with transport delay mechanism
  a <= transport b;

  -- with inertial delay mechanism
  a <= inertial b;

  -- with reject delay mechanism
  a <= reject 10 ns inertial b;

  -- with guarded and transport delay mechanism
  a <= guarded transport b;

  -- with guarded and inertial delay mechanism
  a <= guarded inertial b;

  -- with guarded and reject delay mechanism
  a <= guarded reject 10 ns inertial b;

  -- test unary operators
  a <= (others => func(and b, or b, nand b, or b, nor b, xnor b));
  a <= (others => func(nand b));
  a <= (others => func(or b));
  a <= (others => func(nor b));
  a <= (others => func(xor b));
  a <= (others => func(xnor b));

  U_FIFO : entity something.somethingelse
    generic map (
      G_FIRST => (blah <= 0),
      G_SECOND => 3
    )
    port map (
      I_INPUT => blah2
    );

end architecture RTL;
