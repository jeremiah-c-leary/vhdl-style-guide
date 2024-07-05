
architecture ARCH of ENTITY1 is

begin

  -- new line

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

  U_INST1 : INST1 port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

  U_INST1 : configuration CONFIG port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

  U_INST1 : entity FIFO port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

  U_INST1 : entity FIFO(rtl) port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

  U_INST1 : component FIFO port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

  -- no new line

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

  U_INST1 : INST1 port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

  U_INST1 : configuration CONFIG port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

  U_INST1 : entity FIFO port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

  U_INST1 : entity FIFO(rtl) port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

  U_INST1 : component FIFO port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

  -- with comments

  U_INST1 : INST1
    generic map (
      G_GEN_1 => 3,
      G_GEN_2 => 4,
      G_GEN_3 => 5
    )
    -- Comment
    port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

  U_INST1 : INST1
    -- Comment
    port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

  U_INST1 : configuration CONFIG
    -- Comment
    port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

  U_INST1 : entity FIFO
    -- Comment
    port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

  U_INST1 : entity FIFO(rtl)
    -- Comment
    port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

  U_INST1 : component FIFO
    -- Comment
    port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

-- port map left aligned

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

  U_INST1 : INST1 port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

  U_INST1 : configuration CONFIG port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

  U_INST1 : entity FIFO port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

  U_INST1 : entity FIFO(rtl) port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

  U_INST1 : component FIFO port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

end architecture ARCH;
