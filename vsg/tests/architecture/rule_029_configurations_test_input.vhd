

architecture ARCH of ENTITY1 is

  signal sig1 : std_logic;
  file fil1 : something;
  -- Comment1
  type typ1 is range 31 downto 0;
  subtype sub1 is resolved std_ulogic;
  -- Comment1
  variable var1 : integer;
  constant con1 : integer := 0;

  attribute att1 : some_attr;

begin

end architecture ARCH;
