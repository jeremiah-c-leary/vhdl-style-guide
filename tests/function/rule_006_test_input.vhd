
architecture RTL of FIFO is

  function func1 return integer;

  pure function func1 return integer;

  impure function func1 return integer;

  -- Violations follow

  function func1 return integer;
  function func1 return integer;

  pure function func1 return integer;
  pure function func1 return integer;

  impure function func1 return integer;
  impure function func1 return integer;

begin

end architecture RTL;
