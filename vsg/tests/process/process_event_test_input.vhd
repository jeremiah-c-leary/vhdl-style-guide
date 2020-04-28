
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

    if (some_signal_rising_edge = '1') then
       overflow <= '1';
    end if;

    if (some_signal_falling_edge = '0') then
       overflow <= '1';
    end if;

    -- This will check for records
    if (rising_edge(q_ff.some_flop)) then
       wr_en <= '1';
    end if;

    if (q_ff.some_flop'event and q_ff.some_flop = '1') then
       wr_en <= '1';
    end if;

    if (something) then
       wr_en <= '1';
    elsif (falling_edge(q_ff.some_flop)) then
       wr_en <= '0';
    end if;

    if (something) then
       wr_en <= '1';
    elsif (q_ff.some_flop'event and q_ff.some_flop = '0') then
       wr_en <= '0';
    end if;


  end process PROC_1;

end architecture RTL;
