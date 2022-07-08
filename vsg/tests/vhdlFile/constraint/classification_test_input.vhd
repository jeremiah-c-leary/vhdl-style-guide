architecture rtl of fifo is

signal sig8 : record_type_3(
  element1(7 downto 0),
  element2(4 downto 0)(7 downto 0)(
    elementA(7 downto 0),
    elementB(3 downto 0)
  ),
  element3(3 downto 0)(
    elementC(4 downto 1),
    elementD(1 downto 0)
  ),
  element5(
    elementE(3 downto 0),
    elementF(7 downto 0)
  ),
  element6(4 downto 0),
  element7(7 downto 0)
);

  signal sig9 : record_type_3(func1(A, 5, 6) downto func2(4, 6, 8));

  signal sig9 : record_type_3(7 downto 0);

  signal sig9 : record_type_3(0 to 7);

  signal sig9 : record_type_3(7 downto 0, 3 to 4);

  signal sig9 : record_type_3(blah'range);

  signal sig9 : record_type_3(element1(7 downto 0));

  signal sig9 : record_type_3(blah'range);

  signal sig9 : record_type_3( blah'range );

  signal sig9 : record_type_3( blah'range --Comment
 );

  signal sig9 : integer range 0 to 31;

  signal sig9 : integer range 0 to 31 := 20;

begin

end architecture rtl;
