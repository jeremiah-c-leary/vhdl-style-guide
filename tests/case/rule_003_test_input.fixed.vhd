
architecture ARCH of ENTITY is

begin

  PROC_1 : process (a, b, c) is
  begin

     case boolean_1 is

      when STATE_1 =>

        a <= b;
        b <= c;
        c <= d;

     end case;

  end process PROC_1;

  PROC_2 : process (a, b, c) is
  begin

     case boolean_1 is

      when STATE_1 =>

        a <= b;
        b <= c;
        c <= d;

     end case;

  end process PROC_2;

  gen_label : case boolean_1    generate

   when STATE_1 =>

     a <= b;
     b <= c;
     c <= d;

  end generate;

end architecture ARCH;
