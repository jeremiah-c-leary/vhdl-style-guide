
architecture RTL of FIFO is

  function func1 return integer;

  pure function func1 return integer;

  impure function func1 return integer;

  function func1 return integer is

  begin

  end function func1;

  -- Violations follow

  function Func1 return integer;

  function FUNC1 return integer;

  pure function fUNc1 return integer;
  pure function funC1 return integer;

  impure function FUNC1 return integer;
  impure function func1 return integer;

begin

end architecture RTL;
