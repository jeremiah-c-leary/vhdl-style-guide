architecture RTL of FIFO is

  file F1 : IntegerFile;
  
  file F2 : IntegerFile is "test.dat";
  
  file F3 : IntegerFile open WRITE_MODEW is "test.dat";
  
  file F1, F2, F3 : IntegerFile open WRITE_MODEW is "test.dat";

  file F1 : IntegerFile open WRITE_MODEM is (something(else));

begin

end architecture RTL;
