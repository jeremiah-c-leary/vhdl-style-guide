
architecture RTL of ENTITY1 is

  subtype read_size is range 0 to 9;
  subtype write_size is range 0 to 9;

  signal read  : read_size;
  signal write : write_size;

  constant read_sz  : read_size := 8;
  constant write_sz : write_size := 1;

begin

end architecture RTL;
