
architecture ARCH of ENTITY is

begin

  PROC_1 : process (a,b,c,d) is
  begin

    if a = 1 then


      case b is
        when 1 =>
          c <= d;
        when 2 =>
          d <= f;
      end case;


    elsif (b = 1) then


      case b is
        when 1 =>
          c <= d;
        when 2 =>
          d <= f;
      end case;


    else


      case b is
        when 1 =>
          c <= d;
        when 2 =>
          d <= f;
      end case;


    end if;

  end process PROC_1;

end architecture ARCH;

