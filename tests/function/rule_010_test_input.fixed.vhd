
architecture RTL of FIFO is

  function func_1 (a : integer) return integer;
  function func_2 (b : integer) return integer;

  signal sig1 : integer := func_1;

begin

  OUT1 <= func_1;

  PROC1 : process () is
  begin

     sig1 <= func_1;
     sig2 <= func_1(a) or func_2(b);
     sig3 <= func_1 or func_2;

  end process;

end architecture RTL;
