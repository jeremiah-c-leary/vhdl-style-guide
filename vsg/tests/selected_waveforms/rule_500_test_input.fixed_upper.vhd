architecture rtl of fifo is

begin

  process is
  begin

    with mux_select select
      addr <= "0000" WHEN 0,
              "0001" WHEN 1,
              "1111" WHEN others;

  end process;

  with mux_select select
    addr <= "0000" WHEN 0,
            "0001" WHEN 1,
            "1111" WHEN others;

end architecture rtl;
