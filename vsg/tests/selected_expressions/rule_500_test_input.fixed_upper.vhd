architecture rtl of fifo is

begin

  process is
  begin

    with mux_select select
      addr := "0000" WHEN 0,
              "0001" WHEN 1,
              "1111" WHEN others;

    with mux_select select
      addr <= force "0000" WHEN 0,
                    "0001" WHEN 1,
                    "1111" WHEN others;

  end process;

end architecture rtl;
