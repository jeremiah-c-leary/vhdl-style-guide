
architecture RTL of FIFO is

begin

  process
  begin

    sig1 <= sig2;
    sig2 <= sig3;
    sig2 <= sig3;

    if a = b then
      sig3 <= sig4;
      sig4 <= sig5;
      sig4 <= sig5;
      if c = d then
        sig6 <= sig7;
        sig7 <= sig8;
        sig7 <= sig8;
      end if;
    end if;

    sig1_abcdefgh <= sig2;
    sig2_abcdefgh <= sig3;
    sig2_abcdefgh <= sig3;

    case address is

      when 0 =>
        sig5_a   <= sig6;
        sig6_a   <= sig7;
        sig6_a   <= sig7;
      when 1 =>
        sig5_abc <= sig6;
        sig6_abc <= sig7;
        sig6_abc <= sig7;

    end case;

  end process;

  -- Violations below

  process
  begin

    sig1 <= sig2;
    sig2 <= sig3;
    sig2 <= sig3;

    if a = b then
      sig3 <= sig4;
      sig4 <= sig5;
      sig4 <= sig5;
      if c = d then
        sig6 <= sig7;
        sig7 <= sig8;
        sig7 <= sig8;
      end if;
    end if;

    case address is

      when 0 =>
        sig5 <= sig6;
        sig6 <= sig7;
        sig6 <= sig7;

    end case;

    sig1_abcdefghijklmn   <= sig2;
    sig2_abcdefghijklmn   <= sig3;
    sig3_abcdefghijklmn   <= sig3;

    for index in 4 to 23 loop
      sig5_abc            <= sig6;
      sig6_abc            <= sig7;
      sig6_abc            <= sig7;
    end loop;

    while (temp /= 10) loop
      sig1_abcdefghijklmn <= sig2;
      sig2_abcdefghijklmn <= sig3;
      sig3_abcdefghijklmn <= sig3;
    end loop;

    loop
      sig5_a              <= sig6;
      sig6_a              <= sig7;
      sig6_a              <= sig7;
    end loop;

  end process;


end architecture RTL;
