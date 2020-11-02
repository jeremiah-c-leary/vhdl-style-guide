
architecture RTL of FIFO is

begin

  a <= b and c or d xor e nand f nor g xor h xnor i;

  a <= (b) and (c) or (d) xor (e) nand (f) nor (g) xor (h) xnor (i);

  -- Violations

  a <= b  and  c  or  d  xor  e  nand  f  nor  g  xor  h  xnor  i;

  a <= (b)and(c)or(d)xor(e)nand(f)nor(g)xor(h)xnor(i);

end architecture RTL;
