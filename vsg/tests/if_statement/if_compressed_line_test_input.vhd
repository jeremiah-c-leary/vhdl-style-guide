
architecture RTL of ENTITY1 is

begin

  PROC_1 : process (A, B, C) is
  begin

    if (A = '1' and B = '1') then X <= '1'; elsif (C = '0') then Y <= '0'; else W := '0'; end if;

    if (A = '1' and B = '1')then X <= '1';elsif (C = '0')then Y <= '0';else W <= '0';end if;

  end process PROC_1;

end architecture RTL;
