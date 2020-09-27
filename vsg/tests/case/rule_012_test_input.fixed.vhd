
architecture ARCH of ENTITY is

begin

  PROC_1 : process (a, b, c) is
  begin

    case boolean_1 is

      when STATE_1 =>
        a <= b;

      when STATE_1 => -- This is okay
        a <= b;

      when STATE_1 =>-- This is okay
        a <= b;

      when STATE_2 =>
 a <= b;
      when STATE_3 =>
a <= b;
      when STATE_4 =>
null;

    end case;

  end process PROC_1;

end architecture ARCH;
