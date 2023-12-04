architecture rtl of fifo is

begin

    dut : entity work.ampersand
    generic map (
      g_FIRST     => c_FIRST,
      g_SECOND(0) => c_SECOND
    )
    port map (
      i_thing    => inthing,
      o_thing(0) => outthing
    );

end architecture rtl;
