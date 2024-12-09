
architecture RTL of FIFO is

  function func_1 (a : integer) return integer is
    constant c : integer;
    variable v : integer;
    file f     : something;
    alias a    : subtype_indicator is name;
    alias a    is name;
  begin
  end function func1;

  function func_1 (a : integer) return integer is
    constant c : integer;
    variable v : integer;
    file f     : something;
    alias a    : subtype_indicator is name;
    alias a    is name;

    -- Checking exclusions
    constant c_abc   : integer;
    function my_func return integer is
      constant c_abc : integer;
    begin
    end function;
    constant c_abc   : integer;
    type flag_pt is protected body
      variable flag : boolean;
    end protected body;

  begin
  end function func1;

  procedure proc_1 is
    constant c   : integer;
    variable v : integer;
    file f         : something;
  begin
  end procedure proc_1;

begin

end architecture RTL;
