
architecture RTL of FIFO is

begin

  process

  begin

    if a = '1' then
      b <= '0';
    elsif c = '1' then
      b <= '1';
    elsif a(3 downto 0) = 0 then
      b <= '0';
    elsif a(3 downto 0) + f(34, 56, 72) - g(f(35, 25, 60) downto h(45, 32)) then
      b <= '1';
    elsif (a or b) and (c or d) then
      b <= '0';
    end if;

    -- Violations below

    if a = '1' then
      b <= '0';
    elsif c = '1' then
      b <= '1';
    elsif a(3 downto 0) = 0 then
      b <= '0';
    elsif a(3 downto 0) + f(34, 56, 72) - g(f(35, 25, 60) downto h(45, 32)) then
      b <= '1';
    elsif (a or b) and (c or d) then
      b <= '0';
    end if;

  end process;

  process begin

    if (x(k) = '1') and (v_y = '0') then
      b <= '0';
    end if;

    if ((ctrl_done_d1 = '0') and (CTRL_DONE = '1')) or (dev_addr = dev_addr_prv) then
      b <= '0';
    end if;

  end process;

  process begin

    if (sync_reset) = '1' then
      b <= '0';
    end if;

    if a='1' then
      b <= '0';
    end if;

    if a='1' then
      b <= '0';
    end if;

    if a='1' then
      b <= '0';
    end if;

    if a='1' then
      b <= '0';
    end if;

    if a='1' then
      b <= '0';
    end if;

    if a='1' then
      b <= '0';
    end if;

  end process;

  process begin

    if something then
      b <= 0;
    elsif something_else then
      b <= 1;
    end if;

    if something then
      b <= 0;
    elsif something_else then
      b <= 1;
    end if;

  end process;

end architecture RTL;
