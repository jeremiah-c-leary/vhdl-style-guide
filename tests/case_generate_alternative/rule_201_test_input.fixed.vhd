
architecture ARCH of ENTITY is

begin

     gen_label : case boolean_1 generate

      when STATE_1 =>

      -- Comment
      when STATE_2 =>

     end generate;

  -- Violations below

     gen_label : case boolean_1 generate

      when STATE_1 =>

      -- Comment
      when STATE_2 =>

     end generate;

     gen_label : case boolean_2 generate

       -- Comment
       when STATE_1 =>
     end generate;

end architecture ARCH;
