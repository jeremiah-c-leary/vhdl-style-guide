
architecture rtl of fifo is

  constant GBE_RX_AVST_NULL : t_avst_packet(data(7 downto 0), empty(0 downto 0), error(5 downto 0)) :=
  (
    x"00",
    '0',
    '0',
    '0',
    "-",
    "000000"
  );

  constant GBE_RX_AVST_NULL : t_avst_packet(data(7 downto 0), empty(0 downto 0), error(5 downto 0)) :=
  (
    x"00", '0', '0',
    '0', "-",
    "000000"
  );

begin

end architecture rtl;
