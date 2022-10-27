architecture rtl of fifo is

begin

  process is
  begin

    with mux_select select
      addr := "0000" when 0,
              "0001" When 1,
              "1111" WHEN others;

    with mux_select select
      addr <= force "0000" when 0,
                    "0001" When 1,
                    "1111" WHEN others;

  end process;

end architecture rtl;
