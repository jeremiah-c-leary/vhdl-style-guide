
architecture RTL of FIFO is

  function func1_f return integer;

  pure function func1_f return integer;

  impure function func1_f return integer;

  function func1_f return integer is

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
