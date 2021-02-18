
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

  -- Verify others are still handled 
  constant cons2 : t_type :=
  (others => (valid => '0', data => (others => '0')), others => (1 => '0', (others => '0'));

  -- Verify assignments are still handled
  constant cons1 : t_type := (
    1 => func1(std_logic_vector(G_GEN), G_GEN2), 2 => func1(std_logic_vector(G_GEN3), G_GEN4));

begin

end architecture rtl;
