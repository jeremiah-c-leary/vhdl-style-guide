
architecture ARCH of ENTITY is

begin

  PROC_1 : process (a, b, c) is
  begin

     case boolean_1 is

      when STATE_1=>

        a <= b;
        b <= c;
        c <= d;

      when STATE_1   =>

        a <= b;
        b <= c;
        c <= d;

      when others=>

        z <= a;

      when others       =>

        z <= a;

     end case;

  end process PROC_1;

  gen_label : case boolean_1 generate

    when STATE_1 =>

      a <= b;
      b <= c;
      c <= d;

    when STATE_1 =>

      a <= b;
      b <= c;
      c <= d;

    when others =>

      z <= a;

    when others =>

      z <= a;

  end generate;

  gen_label : case boolean_1 generate

    when STATE_1 =>

      a <= b;
      b <= c;
      c <= d;

    when STATE_1 =>

      a <= b;
      b <= c;
      c <= d;

    when others =>

      z <= a;

    when others =>

      z <= a;

   end generate;

end architecture ARCH;
