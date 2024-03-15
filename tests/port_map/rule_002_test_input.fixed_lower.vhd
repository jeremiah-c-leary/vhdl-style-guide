
architecture ARCH of ENTITY1 is

begin

  U_INST1 : INST1
    generic map (
      G_GEN_1(3 downto 0) => 3,
      G_GEN_2(2 downto 1) => 4,
      G_GEN_3 => 5
    )
    port map (
      port_1(3 downto 0) => w_port_1,
      port_2 => w_port_2,
      port_3(2 downto 1) => w_port_3
    );

  -- Violations below
  U_INST1 : INST1
    generic map (
      g_gen_1(3 downto 0) => 3,
      g_gen_2(2 downto 1) => 4,
      g_gen_3 => 5
    )
    port map (
      port_1(3 downto 0) => w_port_1,
      port_2 => w_port_2,
      port_3(2 downto 1) => w_port_3
    );

end architecture ARCH;

