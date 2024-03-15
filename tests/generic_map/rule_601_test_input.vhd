
architecture ARCH of ENTITY1 is

begin

  U_INST1 : INST1
    generic map (
      G_GEN_1 => 3,
      G_GEN_2 => 4,
      G_GEN_3 => 5
    )
    port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

  -- Violations below

  U_INST1 : INST1
    generic map (
      W_GEN_1 => 3,
      GEN_2   => 4,
      WR_GEN_3 => 5
    )
    port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

  U_INST2 : INST2
    generic map (
      W_GEN_1(W_GEN_1) => 3,
      G_GEN_2(W_GEN_1) => 10
    );

end architecture ARCH;

