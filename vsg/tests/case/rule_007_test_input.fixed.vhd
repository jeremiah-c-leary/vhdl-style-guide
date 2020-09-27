
architecture ARCH of ENTITY is

begin

  PROC_1 : process (a, b, c) is
  begin
     -- Comments are fine
     case boolean_1 is

      when STATE_1 =>

        a <= b;
        b <= c;
        c <= d;

     end case;

  end process PROC_1;

  PROC_2 : process (a, b, c) is
  begin
     sig1 <= sig2;

     case boolean_1 is

      when STATE_1=>

        a <= b;
        b <= c;
        c <= d;

     end   case;

  end process PROC_2;

end architecture ARCH;
