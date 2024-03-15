
architecture ARCH of ENTITY1 is

begin

  U_INST1 : entity fifo_dsn.INST1(rtl);

  U_INST2 : component INST2
    generic map (
      G_GEN_1 => 3,
      G_GEN_2 => 4,
      G_GEN_3 => 5
    );

  U_INST3 : INST3
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

  -- Violation below

  U_INST1 : entity fifo_dsn.INST1(rtl)
;

  U_INST2 : component INST2
    generic map (
      G_GEN_1 => 3,
      G_GEN_2 => 4,
      G_GEN_3 => 5
    )
                ;

  U_INST3 : INST3
    generic map (
      G_GEN_1 => 3,
      G_GEN_2 => 4,
      G_GEN_3 => 5
    )
    port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    )
   ;


end architecture ARCH;

