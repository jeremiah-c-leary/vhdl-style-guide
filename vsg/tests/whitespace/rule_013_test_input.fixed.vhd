
architecture RTL of FIFO is

begin

  a <= b and c or d xor e nand f nor g xor h xnor i;

  a <= (b) and (c) or (d) xor (e) nand (f) nor (g) xor (h) xnor (i);

  -- Violations

  a <= b  and  c  or  d  xor  e  nand  f  nor  g  xor  h  xnor  i;

  a <= (b) and (c) or (d) xor (e) nand (f) nor (g) xor (h) xnor (i);

  -- Unary operators should be ignored
  a <= (others => func(and b, or b, nand b, or b, nor b, xnor b));
  a <= (others => func(nand b));
  a <= (others => func(or b));
  a <= (others => func(nor b));
  a <= (others => func(xor b));
  a <= (others => func(xnor b));

  a <= and(some_signal);
  a <= nand(some_signal);
  a <= or(some_signal);
  a <= nor(some_signal);
  a <= xor(some_signal);
  a <= xnor(some_signal);

  a <= b and and(some_signal);
  a <= c and nand(some_signal);
  a <= d and or(some_signal);
  a <= e and nor(some_signal);
  a <= f and xor(some_signal);
  a <= g and xnor(some_signal);

end architecture RTL;
