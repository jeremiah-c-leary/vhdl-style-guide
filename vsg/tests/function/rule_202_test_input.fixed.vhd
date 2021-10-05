
architecture RTL of FIFO is

  function func1 return integer is
  begin
     return 0;
  end function func1;

  function func1 return integer is
     constant width : integer := 32;

  begin
     return 0;
  end function func1;

  pure function func1 return integer is
  begin
     return 0;
  end function func1;

  pure function func1 return integer is
     constant width : integer := 32;

  begin
     return 0;
  end function func1;

  impure function func1 return integer is
  begin
     return 0;
  end function func1;

  impure function func1 return integer is
     constant width : integer := 32;

  begin
     return 0;
  end function func1;

  -- Violations follow

  function func1 return integer is
     constant width : integer := 32;

  begin
     return 0;
  end function func1;

  pure function func1 return integer is
     constant width : integer := 32;

  begin
     return 0;
  end function func1;

  impure function func1 return integer is
     constant width : integer := 32;

  begin
     return 0;
  end function func1;

begin

end architecture RTL;
