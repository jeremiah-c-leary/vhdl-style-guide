
architecture ARCH of ENTITY is

begin

  PROC_1 : process
  begin

     case boolean_1 is

      when STATE_1 =>

     end case;

     case boolean_1 is
      when STATE_1 =>

     end case;

     case boolean_1 is
      -- Comment
      when STATE_1 =>

     end case;

  end process PROC_1;

  -- Violations below

  PROC_1 : process
  begin

     case boolean_1 is

      when STATE_1 =>

     end case;

     case boolean_1 is

      when STATE_1 =>

     end case;

     case boolean_1 is

      -- Comment
      when STATE_1 =>

     end case;

  end process PROC_1;

end architecture ARCH;
