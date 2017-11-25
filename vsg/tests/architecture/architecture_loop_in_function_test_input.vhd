

architecture ARCH of ENTITY is

  function FUNC1 return RESULT is
    variable a : integer;
    variable b : integer;
  begin

    for i in 0 to 32 loop
      a(i) := 0;
    end loop;
    return a;

  end FUNC1;

begin



end architecture ARCH;


