
architecture ARCH of ENTITY1 is

begin

  U_INST1 : INST1
    generic map (
      -- Keep Comment
      G_GEN_1 => 3,-- Comment
      -- Keep Comment
      G_GEN_2 => 4,  -- Comment
      -- Keep Comment
      G_GEN_3 => 5-- Comment
      -- Keep Comment
    )
    port map (
      -- Keep Comment
      PORT_1 => w_port_1,    -- Comment
      -- Keep Comment
      PORT_2 => w_port_2, -- Comment
      -- Keep Comment
      PORT_3 => w_port_3--Comment
      -- Keep Comment
    );

end architecture ARCH;

