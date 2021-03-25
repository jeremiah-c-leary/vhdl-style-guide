
architecture RTL of FIFO is

begin

  a <= b and c or d xor e nand f nor g xor h xnor i;

  a <= (b) and (c) or (d) xor (e) nand (f) nor (g) xor (h) xnor (i);

  -- Violations

  a <= b  and  c  or  d  xor  e  nand  f  nor  g  xor  h  xnor  i;

  a <= (b)and(c)or(d)xor(e)nand(f)nor(g)xor(h)xnor(i);

  -- Unary operators should be ignored
  a <= (others => func(and b, or b, nand b, or b, nor b, xnor b));
  a <= (others => func(nand b));
  a <= (others => func(or b));
  a <= (others => func(nor b));
  a <= (others => func(xor b));
  a <= (others => func(xnor b));

end architecture RTL;
