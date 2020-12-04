
architecture RTL of FIFO is

  function FUNC1 return integer;

  pure function FUNC1 return integer;

  impure function FUNC1 return integer;

  function FUNC1 return integer is

  begin

  end function func1;

  -- Violations follow

  function FUNC1 return integer;

  function FUNC1 return integer;

  pure function FUNC1 return integer;
  pure function FUNC1 return integer;

  impure function FUNC1 return integer;
  impure function FUNC1 return integer;

begin

end architecture RTL;
