
architecture ARCH of ENTITY

begin

  PROC_1 : process (a) is
  begin

    case CASE1 is

      when a => -- Comment
        -- Comment
        x <= y;
        z <= a;
      -- Comment
      when b => -- Comment
        x <= y;
        z <= a;
        --
      when b => -- Comment
        x <= y;
        z <= a;
     -- Comment
      when b => -- Comment
        x <= y;
        z <= a;
         -- Comment
    end case;

end architecture ARCH;
