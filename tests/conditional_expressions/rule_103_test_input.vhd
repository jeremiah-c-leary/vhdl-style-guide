
architecture rtl of fifo is

begin

  process
  begin

    var1 := '0' when (rd_en = '1') else'1';

    var2 := '0' when (rd_en = '1') else '1';

    wr_en_a <= force '0' when (rd_en = '1') else'1';

    wr_en_b <= force '0' when (rd_en = '1') else '1';

  end process;

  concurrent_wr_en_a <= '0' when (rd_en = '1') else'1';

  concurrent_wr_en_b <= '0' when (rd_en = '1') else '1';

end architecture rtl;
