
architecture ARCH of ENTITY is

begin

  PROC_1 : process
  begin

     case boolean_1 is

      when STATE_1 =>

      -- Comment
      when STATE_2 =>

     end case;

  end process PROC_1;

  -- Violations below

  PROC_1 : process
  begin

     case boolean_1 is

      when STATE_1 =>

      -- Comment
      when STATE_2 =>

     end case;

     case boolean_2 is

       -- Comment
       when STATE_1 =>
     end case;

  end process PROC_1;

end architecture ARCH;
