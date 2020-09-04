
architecture ARCH of ENTITY is

begin

  -- Component instantiation without component keyword.

  U_INST1 : INST1
    generic map (
      GEN_1 => c_gen_1,
      GEN_2 => c_gen_2,
      GEN_3 => c_gen_3
    )
    port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

  U_INST1 : INST1
    port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

  U_INST1 : INST1
    generic map (
      GEN_1 => c_gen_1,
      GEN_2 => c_gen_2,
      GEN_3 => c_gen_3
    );

  U_INST1 : INST1;

  -- Component instantiation with component keyword.

  U_INST1 : component INST1
    generic map (
      GEN_1 => c_gen_1,
      GEN_2 => c_gen_2,
      GEN_3 => c_gen_3
    )
    port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

  U_INST1 : component INST1
    port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

  U_INST1 : component INST1
    generic map (
      GEN_1 => c_gen_1,
      GEN_2 => c_gen_2,
      GEN_3 => c_gen_3
    );

  U_INST1 : component INST1;

  -- entity without architecture identifier

  U_INST1 : entity INST1
    generic map (
      GEN_1 => c_gen_1,
      GEN_2 => c_gen_2,
      GEN_3 => c_gen_3
    )
    port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

  U_INST1 : entity INST1
    port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

  U_INST1 : entity INST1
    generic map (
      GEN_1 => c_gen_1,
      GEN_2 => c_gen_2,
      GEN_3 => c_gen_3
    );

  U_INST1 : entity INST1;

  -- entity with architecture identifier

  U_INST1 : entity INST1 (rtl)
    generic map (
      GEN_1 => c_gen_1,
      GEN_2 => c_gen_2,
      GEN_3 => c_gen_3
    )
    port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

  U_INST1 : entity INST1 (rtl)
    port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

  U_INST1 : entity INST1 (rtl)
    generic map (
      GEN_1 => c_gen_1,
      GEN_2 => c_gen_2,
      GEN_3 => c_gen_3
    );

  U_INST1 : entity INST1 (rtl);

  -- configuration

  U_INST1 : configuration INST1
    generic map (
      GEN_1 => c_gen_1,
      GEN_2 => c_gen_2,
      GEN_3 => c_gen_3
    )
    port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

  U_INST1 : configuration INST1
    port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

  U_INST1 : configuration INST1
    generic map (
      GEN_1 => c_gen_1,
      GEN_2 => c_gen_2,
      GEN_3 => c_gen_3
    );

  U_INST1 : configuration INST1;



end architecture ARCH;

