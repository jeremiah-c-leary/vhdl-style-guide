-- VHDL-2019 allows an optional trailing semicolon in interface lists

entity FIFO is
  generic (
    G_WIDTH : integer := 8;
    G_DEPTH : integer := 16;
  );
  port (
    a : in    std_logic;
    b : out   std_logic;
  );
end entity FIFO;

architecture RTL of FIFO is

  procedure proc (
    a : in    integer;
  ) is
  begin
  end procedure proc;

  function func (a : integer; b : integer;) return integer is
  begin
    return a;
  end function func;

begin

end architecture RTL;
