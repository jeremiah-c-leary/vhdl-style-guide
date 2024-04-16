
architecture RTL of FIFO is

  constant con1 : integer := a + b + c + d;

  constant con1 : integer :=
                             a + b + c + d;

  constant con2 : integer := a + b +
                             c + d;

  constant con3 : integer :=
  (
   0,
   1,
   2,
   3
  );

  constant con4 : dictionary :=
  (
   (3, 4, 5),
   (1, 2, 3),
   (9, 8, 7)
  );


  -- Violations

  constant con2 : integer := a + b +
c + d;

  constant con2 : integer := a + b +
                                  c + d;

  constant con1 : integer :=
     a + b + c + d;

  constant con3 : integer :=
  (
   0,
   1,
   2,
   3
  );

  constant con4 : dictionary :=
  (
   (3, 4, 5),
   (1, 2, 3),
   (9, 8, 7)
  );


begin

end architecture RTL;
