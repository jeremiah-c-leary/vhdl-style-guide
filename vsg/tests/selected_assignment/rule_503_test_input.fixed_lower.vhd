architecture rtl of fifo is

begin

  -- lower case

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

  -- Mixed Case

  process is
  begin

    With (mux_select or reset) Select
      addr := "0000" when 0,
              "0001" when 1,
              "1111" when others;

    With (mux_select or reset) Select
      addr <= Force "0000" when 0,
                    "0001" when 1,
                    "1111" when others;

    With (mux_select or reset) Select
      addr <= "0000" when 0,
              "0001" when 1,
              "1111" when others;

  end process;

  With (mux_select or reset) Select
    addr <= guarded "0000" when 0,
            "0001" when 1,
            "1111" when others;

  -- Upper case

  process is
  begin

    WITH (mux_select or reset) SELECT
      addr := "0000" when 0,
              "0001" when 1,
              "1111" when others;

    WITH (mux_select or reset) SELECT
      addr <= FORCE "0000" when 0,
                    "0001" when 1,
                    "1111" when others;

    WITH (mux_select or reset) SELECT
      addr <= "0000" when 0,
              "0001" when 1,
              "1111" when others;

  end process;

  WITH (mux_select or reset) SELECT
    addr <= guarded "0000" when 0,
            "0001" when 1,
            "1111" when others;

end architecture rtl;
