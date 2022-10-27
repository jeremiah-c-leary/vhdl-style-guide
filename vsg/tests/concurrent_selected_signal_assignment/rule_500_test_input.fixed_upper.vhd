architecture rtl of fifo is

begin

  WITH mux_select select
    addr <= "0000" when 0,
            "0001" when 1,
            "1111" when others;

  WITH mux_select select
    addr <= "0000" when 0,
            "0001" when 1,
            "1111" when others;

  WITH mux_select select
    addr <= "0000" when 0,
            "0001" when 1,
            "1111" when others;


end architecture rtl;
