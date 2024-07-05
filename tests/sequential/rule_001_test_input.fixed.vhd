
architecture RTL of FIFO is

begin

  process
  begin

    sig1 <= sig2;
    sig2 <= sig3;

    if a = b then
      sig3 <= sig4;
      sig4 <= sig5;
      if c = d then
        sig6 <= sig7;
        sig7 <= sig8;
      end if;
    end if;

    case address is

      when 0 =>
        sig5 <= sig6;
        sig6 <= sig7;
        sig8 <= '0' when b = '1';

    end case;

  end process;

  -- Violations below

  process
  begin

    sig1 <= sig2;
    sig2 <= sig3;

    if a = b then
      sig3 <= sig4;
      sig4 <= sig5;
      if c = d then
        sig6 <= sig7;
        sig7 <= sig8;
      end if;
    end if;

    case address is

      when 0 =>
        sig5 <= sig6;
        sig6 <= sig7;
        sig8 <= '0' when b = '1';

    end case;

  end process;

end architecture RTL;
