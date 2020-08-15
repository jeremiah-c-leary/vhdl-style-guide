
architecture RTL of FIFO is

begin

  Proc1 (Clock, A, Sig1, Sig2, Var1, Var2, Period);
  READ (L => BufLine, VALUE => Q);


  LABEL1: Proc1 (Clock);
  LABEL2 : READ (L     => BufLine,
                 VALUE => Q);

  LABEL1: postponed Proc1 (Clock);
  LABEL2 : postponed READ (L     => BufLine,
                 VALUE => Q);

  postponed Proc1 (Clock);
  postponed READ (L     => BufLine,
                 VALUE => Q);


end architecture RTL;
