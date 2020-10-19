
architecture RTL of ENTITY1 is

  function FUNC1 (A : in natural) return natural is
    variable temp : natural;
  begin
    temp := A;

    while (temp /= 10) loop
      temp := temp + 1;
    end loop;

    while (temp /= 20) loop
      temp := temp + 1;
end loop;

    while (temp /= 30) loop
      temp := temp + 1;
        end loop;

    return temp;
  end function FUNC1;

begin

end architecture RTL;
