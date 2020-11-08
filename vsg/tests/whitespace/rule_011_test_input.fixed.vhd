
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

  a <= b + c;
  a <= b + c;
  a <= b + c;

  a <= b - c;
  a <= b - c;
  a <= b - c;

  a <= b / c;
  a <= b / c;
  a <= b / c;

  a <= b * c;
  a <= b * c;
  a <= b * c;

  a <= b ** c;
  a <= b ** c;
  a <= b ** c;

  a <= (b) + (c);
  a <= (b) + (c);
  a <= (b) + (c);

  a <= (b) - (c);
  a <= (b) - (c);
  a <= (b) - (c);

  a <= (b) / (c);
  a <= (b) / (c);
  a <= (b) / (c);

  a <= (b) * (c);
  a <= (b) * (c);
  a <= (b) * (c);

  a <= (b) ** (c);
  a <= (b) ** (c);
  a <= (b) ** (c);

end architecture RTL;
