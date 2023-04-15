
architecture RTL of FIFO is

  constant c_const : integer := -2;
  signal c_const : integer := -1;

begin

  process begin

    if a = -1 +6 then
      b <= 0;
    end if;

    if a /= -1 -10 then
      b <= 0;
    end if;

    if a(-3 downto -6) = 0 then
      b <= 0;
    end if;

    case some_number is
       when -1 -16 =>

       when -1 | -2 + 10 | -3 =>
    end case;

  end process;

  process begin

    if a = +1 then
      b <= 0;
    end if;

    if a /= +1 then
      b <= 0;
    end if;

    if a(+3 downto +6) = 0 then
      b <= 0;
    end if;

    case some_number is
       when +1 =>

       when +1 | +2 | +3 =>
    end case;

  end process;

end architecture RTL;
