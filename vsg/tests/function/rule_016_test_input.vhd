
architecture RTL of FIFO is

  function func1 return integer is
  begin
    return 99;
  end func1;

  -- Violations follow

  function func1 return integer is
  begin
         return 99;
  end func1;

  function func1 return integer is
  begin
return 99;
  end func1;


begin

end architecture RTL;
