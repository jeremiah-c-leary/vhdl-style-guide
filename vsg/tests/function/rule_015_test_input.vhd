
architecture RTL of FIFO is

  function func_1 (a : integer) return integer is
    constant c : integer;
    variable v : integer;
    file     f : something;
    alias    a is name;
  begin
  end function func1;

  function func_1 (a : integer) return integer is
    constant  c : integer;
    variable   v : integer;
    file f : something;
    alias a is name;
  begin
  end function func1;

  procedure proc_1 (a : integer) is
    constant  c : integer;
    variable   v : integer;
    file f : something;
    alias a is name;
  begin
  end procedure proc_1;

begin

end architecture RTL;

