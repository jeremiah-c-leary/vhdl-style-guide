
architecture ARCH of ENTITY is

begin

  U_INST1 : INST1
    generic map (
      GENERIC_1 => generic_1,
      GENERIC_2 => generic_2
    )
    port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

  PROC_NAME : process (one) is
  begin
  end process PROC_NAME;

  U_INST1 : INST1
  genEric  map (
      GENERIC_1 => generic_1,
      GENERIC_2 => generic_2
    )
    port map  (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

  U_INST1 : INST1
     generic mAP  (
      GENerIC_1 => generic_1,
      GENERIC_2 => generic_2
    )
    port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

  U_INST1 : INST1
    generic map (
       GENERIC_1 => generic_1,
     GENERic_2 => generic_2)
    port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

  U_INST1 : INST1
    generic map(GENERIC_1 => generic_1,
      generic_2 => generic_2
    )
    port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

  U_INST1 : INST1  generic map (
      GENERIC_1 => generic_1,
      GENERIC_2 => generic_2)
    port map(
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

  U_INST1 : INST1
  generic map (8)
    port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );


end architecture ARCH;

