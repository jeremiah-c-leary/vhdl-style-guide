
architecture RTL of FIFO is

  type NotGood is (X, '0', '1', X); -- illegal

  type MyBit is (L, H);

  type Test is ('0', '1', L, H);
  
  type FSM_States is (Init, Read, Decode, Execute, Write);

begin

end architecture RTL;
