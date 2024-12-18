
architecture RTL of FIFO is

begin

  a <= b sll c srl d sla e sra f rol g ror h;

  a <= (b) sll (c) srl (d) sla (e) sra (f) rol (g) ror (h);

  -- Violations

  a <= (b)sll(c)srl(d)sla(e)sra(f)rol(g)ror(h);

end architecture RTL;
