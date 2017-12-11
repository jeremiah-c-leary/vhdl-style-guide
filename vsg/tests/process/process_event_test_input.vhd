
architecture RTL of ENTITY1 is

begin

  PROC_1 : process(CLK) is
  begin

    if (rising_edge(CLK)) then
       wr_en <= '1';
    end if;

    if (falling_edge(CLK)) then
       rd_en <= '1';
    end if;

    if (CLK'event and CLK = '1') then
       overflow <= '1';
    end if;

    if (CLK'event and CLK = '0') then
       underflow <= '1';
    end if;

  end process PROC_1;

end architecture RTL;
