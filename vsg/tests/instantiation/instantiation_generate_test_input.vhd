
architecture ARCH of ENTITY is

begin

  GENERATE_1 : for CONDITION in 0 to 7 generate

    U_INST1 : INST1
      port map (
        PORT_1 => w_port_1,
        PORT_2 => w_port_2,
        PORT_3 => w_port_3
      );

  end generate;

end architecture ARCH;

