
architecture ARCH of ENTITY is

begin

  PROC_1 : process (a, b, c) is
  begin

    case boolean_1 is

      when STATE_1 | STATE_2 |
           STATE_3 | STATE_4 |
           STATE_5 | STATE_6 =>
        a <= b;

      when STATE_2 =>
        b <= c;

      -- This should fail
      when STATE_1 | STATE_2 |
           | STATE_3 | STATE_4 |
           | STATE_5
           | STATE_6
           | STATE_7 =>
        a <= b;

    end case;

  end process PROC_1;


end architecture ARCH;
