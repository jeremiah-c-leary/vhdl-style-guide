
architecture ARCH of ENTITY is

begin

     gen_label : case boolean_1 generate

      when STATE_1 =>

        a <= b;
        b <= c;
        c <= d;

     end generate;


     gen_label : case boolean_1 generate

      when STATE_1=>

        a <= b;
        b <= c;
        c <= d;

     end generate;

end architecture ARCH;
