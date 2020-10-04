
architecture RTL of FIFO is

  function func1 (
    a : integer;
    constant b : integer;
    signal c : std_logic;
    variable v : std_logic;
    file f : std_logic
  ) return integer;

  --  Violations

  function func1 (
     a : integer;
   constant b : integer;
      signal c : std_logic;
  variable v : std_logic;
        file f : std_logic
  ) return integer;

begin

end architecture RTL;
