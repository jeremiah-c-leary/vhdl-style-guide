
architecture ARCH of ENTITY is

begin

  PROC_1 : process (a, b, c) is
  begin

    case boolean_1 is
        -- This is yet another ccmment

      -- This is another comment
      -- This is a comment
      when STATE_1 =>
        a <= b;
        -- This is yet another ccmment

      when STATE_2 =>
        b <= c;

        -- This is yet another ccmment

          -- This is another comment
    -- This is a comment
      when STATE_1 =>
        a <= b;

    end case;

  end process PROC_1;


end architecture ARCH;
