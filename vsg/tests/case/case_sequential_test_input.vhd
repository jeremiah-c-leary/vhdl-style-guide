
architecture ARCH of ENTITY is

begin

  PROC_1 : process (a,b,c) is
  begin

    case A is

      when 0 => b <= '0';
      when 1 => c <= '1';
        d <= '0';
      when 2 =>
        e <= '1';
      when others => f <= '0';

    end case;

  end process PROC_1;

end architecture ARCH;
