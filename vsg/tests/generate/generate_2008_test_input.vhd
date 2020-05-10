

architecture RTL of ENT is

begin

  gen_delay : case d_depth generate
    --! No delay of #sig_i
   when 0 => 
      delay_reg(0) <= sig_i;
    when 1 =>
      --! Delay #sig_i by one clock cycle
      proc_singleDelay : process (clk)
      begin
        if rising_edge(clk) then
          delay_reg(0) <= sig_i;
        end if;
      end process;
     when others =>
      --! Delay #sig_i by multiple clock cycles
      proc_multipleDelay : process (clk)
      begin
        if rising_edge(clk) then
          --! shift right and insert sig_in on the left
          delay_reg(d_depth-1 downto 0) <= sig_i & delay_reg(d_depth-1 downto 1);
        end if;
      end process;
  end generate;

end architecture RTL;
