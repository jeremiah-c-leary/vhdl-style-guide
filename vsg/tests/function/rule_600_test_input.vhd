
architecture RTL of FIFO is

  function f_func1 return integer;

  pure function f_func1 return integer;

  impure function f_func1 return integer;

  function f_func1 return integer is

  begin

  end function func1;

  -- Violations follow

  function func1 return integer;

  function func1 return integer;

  pure function func1 return integer;
  pure function func1 return integer;

  impure function func1 return integer;
  impure function func1 return integer;

begin

end architecture RTL;
