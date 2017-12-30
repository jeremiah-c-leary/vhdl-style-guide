
architecture ARCH of ENTITY_1 is

  function func_1 (a : integer) return integer is
  begin

    if (a > 2) then
      return 6;
    else
      return 0;
    end if;

  end;


 function  func_1 (a : integer) return integer is
   begin
     return 10;
 end;
   -- Blank lines above and below functions
   function func_1 (a : integer) return integer is
 begin
 return 11;
   end;
  signal a : std_logic;

  
  function func_1(a : integer
                   b : integer
                  ) return integer is
  BEGIN

  end;


  FUNCTION func_1 (a : integer) return integer is
  begin

    case A is
      when 0 =>
      when 1 =>
      when others =>
    end case;

  end;

  impure function func_1 (a : integer) return integer is
    variable var_a : std_logic;
    variable var_b : integer;
  begin
    return 0;
  end func_1;

  pure function func_1 (a : integer) return integer is
    variable var_a : std_logic;
    variable var_b : integer;
  begin
    return 0;
  end func_1;

  -- Variations on ), return, and is

  function func_2 (constant a : integer;
    variable b : integer;
    signal c : integer) return integer is
  begin
    return 0;
  end function func_2;

  function func_2 (constant a : integer;
    variable b : integer;
    signal c : integer
  ) return integer is
  begin
    return 0;
  end function func_2;

  function func_2 (constant a : integer;
    variable b : integer;
    signal c : integer
  )
  return integer is
  begin
    return 0;
  end function func_2;

  function func_2 (constant a : integer;
    variable b : integer;
    signal c : integer
  )
  return
  integer is
  begin
    return 0;
  end function func_2;
 
  function func_2 (constant a : integer;
    variable b : integer;
    signal c : integer
  )
  return
  integer
  is
  begin
    return 0;
  end function func_2;

  -- Declarative items 

  function func_2 (constant a : integer;
    variable b : integer;
    signal c : integer) return integer is
    variable var_1 : integer;
    variable var_2 : integer;
  begin
    return 0;
  end function func_2;

begin


end architecture ARCH;

package FIFO_PKG is

  function func_1 (a : integer) return integer;

  function func_2 (constant a : integer;
    variable b : integer;
    signal c : integer) return integer;

end package FIFO_PKG;
