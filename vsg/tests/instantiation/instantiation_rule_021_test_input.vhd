
architecture ARCH of ENTITY is

begin

  U_INST1 : INST1
    port map (
      PORT_1 => w_port_1(3 downto 0)  , PORT_2 => w_port_2, PORT_3 => w_port_3
    );

  U_INST1 : INST1
    port map (
      PORT_1 => w_port_1, PORT_2 => w_port_2,
      PORT_3 => w_port_3,
      PORT_4 => w_port_4
    );

  U_INST1 : INST1
    port map (PORT_1 => w_port_1, PORT_2 => w_port_2, PORT_3 => w_port3);

  -- This is to test functions in port assignments.
  U_INST1 : INST1
    port map (
      I_PORTMAP_FORMAL => I_ENTITY_INPUT(generate_loop_index)(function_call(G_GENERIC_A(generate_loop_index),8)-1 downto 0),
      I_PORTMAP_FORMAL_OK => I_ENTITY_INPUT(generate_loop_index)(function_call2(G_GENERIC_A(generate_loop_index))-1 downto 0)
    );

  U_INST1 : INST1
    port map (PORT_1 => w_port_1, PORT_2 => w_port_2, PORT_3 => w_port3(45));

  U_INST1 : INST1
    port map (PORT_1 => w_port_1, PORT_2 => w_port_2, PORT_3 => w_port3(45)
    );

end architecture ARCH;

