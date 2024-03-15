architecture rtl of fifo is

begin

  -- Typical formatting

  process is
  begin

    with (mux_select or reset) select
      addr := "0000" when 0,
              "0001" when 1,
              "1111" when others;

    with (mux_select or reset) select
      addr <= force "0000" when 0,
                    "0001" when 1,
                    "1111" when others;

    with (mux_select or reset) select
      addr <= "0000" when 0,
              "0001" when 1,
              "1111" when others;

  end process;

  with (mux_select or reset) select
    addr <= guarded "0000" when 0,
            "0001" when 1,
            "1111" when others;

  -- Next line

  process is
  begin

    with (mux_select or reset) select
      addr := "0000"
 when 0,
              "0001" when 1,
              "1111" when others;

    with (mux_select or reset) select
      addr <= force "0000"
 when 0,
                    "0001" when 1,
                    "1111" when others;

    with (mux_select or reset) select
      addr <= "0000"
 when 0,
              "0001" when 1,
              "1111" when others;

  end process;

  with (mux_select or reset) select
    addr <= guarded "0000"
 when 0,
            "0001" when 1,
            "1111" when others;

end architecture rtl;
