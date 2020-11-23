
architecture RTL of FIFO is

  type Real_Matrix is array (1 to 10) of REAL;

  type BYTE is array (0 to 7) of BIT;

  type Log_4_Vector is array (POSITIVE range 1 to 8, POSITIVE range 1 to 2) of Log_4;

--  type X is (LOW, HIGH);

  type DATA_BUS is array (0 to 7, X) of BIT;

  type type1 is array (2**(a(b)) downto 2**(c(d))) of integer;

  type type2 is array (func1(a, b, c) downto func2(d, e, f)) of integer;

begin

end architecture RTL;
