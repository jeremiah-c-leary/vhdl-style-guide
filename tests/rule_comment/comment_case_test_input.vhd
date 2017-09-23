
architecture ARCH of ENTITY

begin

  PROC_1 : process (a) is
  begin

    case CASE1 is

      when a => --
        x <= y;
        z <= a;
      --
      when b => --
        x <= y;
        z <= a;
        --
      when b => --
        x <= y;
        z <= a;
     -- Comment
      when b => --
        x <= y;
        z <= a;
         -- Comment
    end case;

end architecture ARCH;
