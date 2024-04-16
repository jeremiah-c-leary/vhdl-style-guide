
architecture ARCH of ENTITY1 is

begin

  U_INST1 : INST1
    generic map (
      G_GEN_1 => 3, -- comment
      G_GEN_2 => 4, -- comment
      G_GEN_3 => 5  -- comment
    )
    port map (
      PORT_1 => w_port_1, -- comment
      PORT_2 => w_port_2, -- comment
      PORT_3 => w_port_3  -- comment
    );

  -- Violations below

  U_INST1 : INST1
    generic map (
      G_GEN_1 => 3, -- comment
      G_GEN_2 => 4, -- comment
      G_GEN_3 => 5  -- comment
    )
    port map (
      PORT_1 => w_port_1, -- comment
      PORT_2 => w_port_2, --comment
      PORT_3 => w_port_3  -- comment
    );

end architecture ARCH;
