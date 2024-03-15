
architecture ARCH of ENTITY1 is

begin

  U_INST1 : INST1
    generic map (
      GEN_1_G => 3,
      GEN_2_G => 4,
      GEN_3_G => 5
    )
    port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

  -- Violations below

  U_INST1 : INST1
    generic map (
      GEN_1_W => 3,
      GEN_2   => 4,
      GEN_3_WR => 5
    )
    port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );


end architecture ARCH;

