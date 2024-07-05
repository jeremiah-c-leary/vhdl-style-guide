
architecture RTL of FIFO is

  function func_1 (a : integer) return integer;
  function func_2 (b : integer) return integer;

  signal sig1 : integer := FUNC_1;

begin

  OUT1 <= Func_1;

  PROC1 : process () is
  begin

     sig1 <= FUNC_1;
     sig2 <= FUNC_1(a) or funC_2(b);
     sig3 <= func_1 or func_2;

  end process;

end architecture RTL;
