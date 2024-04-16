
architecture RTL of FIFO is

  function func1 return integer is
  begin
     return 0;
  end function func1;

  function func1 return integer is
  begin
     return 0;
  end function;

  function func1 return integer is
  begin
     return 0;
  end func1;

  function func1 return integer is
  begin
  end;

  -- Fixes follow

  function func1 return integer is
  begin
     return 0;
  end     function func1;

  function func1 return integer is
  begin
     return 0;
  end function      func1;

  function func1 return integer is
  begin
     return 0;
  end     function      func1;

  function func1 return integer is
  begin
     return 0;
  end     function;

  function func1 return integer is
  begin
     return 0;
  end     func1;

begin

end architecture RTL;
