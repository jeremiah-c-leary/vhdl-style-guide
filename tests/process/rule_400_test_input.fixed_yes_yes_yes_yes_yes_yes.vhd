
architecture RTL of FIFO is

  procedure rst_procedure is
  begin
      a    <= (others => '0');
      b <= (others => '0');
      c       := d;
  end procedure;

begin

  PROC_1 : process

    procedure rst_procedure is
    begin
        a    <= (others => '0');
        b <= (others => '0');
        c       := d;
    end procedure;

  begin

    a <= 2;
    b := 1;

    a <= 2;
    b := 3;

    a <= 3;
    b := 10;

  end process;

  PROC_2 : process

  begin

    a  <= x;
    aa <= x;

    if a = b then
      aaa  <= x;
      aaaa <= x;
    elsif a = b then
      aaaaa  <= x;
      aaaaaa <= x;
    else
      aaaaaaa  <= x;
      aaaaaaaa <= x;
    end if;

    case a is
      when 0 =>
        aaaaaaaaa  <= x;
        aaaaaaaaaa <= x;
      when 1 =>
        aaaaaaaaaaa  <= x;
        aaaaaaaaaaaa <= x;
      when others =>
        aaaaaaaaaaaaa  <= x;
        aaaaaaaaaaaaaa <= x;
    end case;

    loop
      aaaaaaaaaaaaaaa  <= x;
      aaaaaaaaaaaaaaaa <= x;
    end loop;

  end process;

  -- Check for alignment of assignment types

  PROC_3 : process

  begin

    a    <= x;
    aa   <= force x;
    aaa  <= release;
    aaaa <= x when y = z else w;

  end process;

end architecture RTL;
