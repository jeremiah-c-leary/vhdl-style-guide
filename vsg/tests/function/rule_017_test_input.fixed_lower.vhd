
architecture RTL of FIFO is

  function func1 return integer;

  pure function func1 return integer;

  impure function func1 return integer;

  function func1 return integer is

  begin

  end function func1;

  -- Violations follow

  function func1 return integer;

  function func1 return integer;

  pure function func1 return integer;
  pure function func1 return integer;

  impure function func1 return integer;
  impure function func1 return integer;

  -- This should be ignored

  function "=" return boolean;

begin

end architecture RTL;
