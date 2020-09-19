
architecture ARCH of ENTITY is

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
    -- Comment 1
            -- Comment 2
          -- Comment 3
      when b => -- Comment
        x <= y;
        z <= a;
         -- Comment
    end case;

  end process PROC_1;

end architecture ARCH;
