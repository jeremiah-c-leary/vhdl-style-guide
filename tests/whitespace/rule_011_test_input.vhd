
architecture RTL of FIFO is

  constant c_con1 : std_logic_vector(-1 to -4);
  type t_typ1 is range -2 to -4;

begin

  a <= b + c;
  a <= b - c;
  a <= b / c;
  a <= b * c;
  a <= b ** c;

  a <= (b) + (c);
  a <= (b) - (c);
  a <= (b) / (c);
  a <= (b) * (c);
  a <= (b) ** (c);

  -- violations below

  a <= b+ c;
  a <= b +c;
  a <= b+c;

  a <= b- c;
  a <= b -c;
  a <= b-c;

  a <= b/ c;
  a <= b /c;
  a <= b/c;

  a <= b* c;
  a <= b *c;
  a <= b*c;

  a <= b** c;
  a <= b **c;
  a <= b**c;

  a <= (b)+ (c);
  a <= (b) +(c);
  a <= (b)+(c);

  a <= (b)- (c);
  a <= (b) -(c);
  a <= (b)-(c);

  a <= (b)/ (c);
  a <= (b) /(c);
  a <= (b)/(c);

  a <= (b)* (c);
  a <= (b) *(c);
  a <= (b)*(c);

  a <= (b)** (c);
  a <= (b) **(c);
  a <= (b)**(c);

  a(N-1 downto 0);
  a(N+1 downto 0);

end architecture RTL;

architecture RTL of FIFO is

  constant c_con2 : t_type := (
    -900, -- comment 1
    -901, -- comment 2
    -902, -- comment 3
    +903, -- comment 4
    -904  -- comment 5
  );

  constant c_con3 : t_type := (
    -12.36e-47,
    45.67e+67,
    58.6729e1093,
    -2346.7921e90,
    401e56
  );

begin

end architecture RTL;

architecture RTL of FIFO is

begin

  a(c + d) <= '0';
  a(c - d) <= '0';
  a(c / d) <= '0';
  a(c * d) <= '0';
  a(c ** d) <= '0';

  a(c+ d) <= '0';
  a(c- d) <= '0';
  a(c/ d) <= '0';
  a(c* d) <= '0';
  a(c** d) <= '0';

  a(c +d) <= '0';
  a(c -d) <= '0';
  a(c /d) <= '0';
  a(c *d) <= '0';
  a(c **d) <= '0';

  a(c+d) <= '0';
  a(c-d) <= '0';
  a(c/d) <= '0';
  a(c*d) <= '0';
  a(c**d) <= '0';

end architecture RTL;

-- test sign is not triggered

architecture RTL of FIFO is

begin

  a <= -1 + 10;

end architecture RTL;

-- test attributes

architecture rtl of fifo is

begin

   -- passing
   a <= b'left + type_bits;
   a <= b'right - type_bits;
   a <= b'left / type_bits;
   a <= b'right * type_bits;
   a <= b'left ** type_bits;

   -- failing
   a <= b'left+type_bits;
   a <= b'right-type_bits;
   a <= b'left/type_bits;
   a <= b'right*type_bits;
   a <= b'left**type_bits;

end architecture rtl;
