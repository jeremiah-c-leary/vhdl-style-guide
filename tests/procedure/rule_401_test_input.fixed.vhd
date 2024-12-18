
architecture RTL of FIFO is

  procedure proc1 is
    constant   c : integer;
    variable  v  : integer;
    file     f   : something;
    alias a      is name;
    alias a      : subtype_indicator is name;
  begin
  end procedure proc1;

  procedure proc1 is
    constant   c : integer;
    variable  v  : integer;
    file     f   : something;
    alias a      is name;
    alias a      : subtype_indicator is name;
  begin
  end procedure proc1;

  procedure proc1 is
    -- Checking exclusions
    constant c_abc : integer;
    function my_func return integer is
      constant c_abc : integer;
    begin
    end function;
    constant c_abc : integer;
    type     flag_pt is protected body
      variable flag  : boolean;
    end protected body;
  begin
  end procedure proc1;

  function func1 return integer is
    constant   c    : integer;
    variable  v       : integer;
    file     f     : something;
  begin
  end function func1;

begin

end architecture RTL;
