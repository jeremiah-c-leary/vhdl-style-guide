
architecture RTL of FIFO is

  type Operation is record
      Mnemonic : String (1 to 10);
      OpCode : Bit_Vector(3 downto 0);
      Op1, Op2, Res : RegName;
  end record;

  type Operation is record
      Mnemonic : String (1 to 10);
      OpCode : Bit_Vector(3 downto 0);
      Op1, Op2, Res : RegName;
  end record Operation;

begin

end architecture RTL;
