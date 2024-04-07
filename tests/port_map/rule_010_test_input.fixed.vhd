
architecture ARCH of ENTITY1 is

begin

  U_INST1 : INST1
    generic map (
      -- Keep Comment
      G_GEN_1 => 3,
      -- Keep Comment
      G_GEN_2 => 4,
      -- Keep Comment
      G_GEN_3 => 5
      -- Keep Comment
    )
    port map (
      -- Keep Comment
      PORT_1 => w_port_1,
      -- Keep Comment
      PORT_2 => w_port_2,
      -- Keep Comment
      PORT_3 => w_port_3
      -- Keep Comment
    );

end architecture ARCH;
