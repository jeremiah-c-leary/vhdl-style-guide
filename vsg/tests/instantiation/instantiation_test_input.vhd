
architecture ARCH of ENTITY is

begin

  U_INST1 : INST1
    port map (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

  PROC_NAME : process (one) is
  begin
  end process PROC_NAME;

  U_INsT1 : INST1
    port map (
     port_1 => w_port_1,
      port_2 => w_port_2,
       port_3 => w_port_3
    );
  U_INST1 : InST1
    port map (
     port_1 => w_port_1,
     port_2 =>  w_port_2,
     port_3 =>w_port_3
    ) ;
  U_INST1 : INST1

      pOrt map (
       port_1 => w_port_1,
       port_2 => w_port_2,
       port_3 => w_port_3
   );
  U_INST1: INST1
   port mAp (

      port_1 => w_pORt_1,
      port_2 => w_port_2,
      port_3 => w_porT_3
      );

 U_INST1 :INST1
    port  map(
      port_1 => w_port_1,
      port_2 => w_port_2,
      port_3 => w_port_3

    );

   U_InST1:INsT1  port mAp (
      port_1 => w_port_1,
      port_2 => w_port_2,
      port_3 => w_port_3);

  U_INST1 : INST1
    port map (PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3
    );

  U_INST1 : INST1
    port map (
      PORT_1 => w_port_1(3 downto 0)  , PORT_2 => w_port_2, PORT_3 => w_port_3
    );
 --This is a comment

  U_INST1 : INST1
    port map (
      port_1(3 downto 0)  => w_port_1,
      port_2 (3 downto 0) => w_port_2
    );

  U_INST1 : INST1
    port map (
      PORT_1 => w_port_1, PORT_2 => w_port_2,
      PORT_3 => w_port_3,
      PORT_4 => w_port_4
    );

  U_INST1 : INST1
    port map
     (
      PORT_1 => w_port_1,
      PORT_2 => w_port_2,
      PORT_3 => w_port_3,
      PORT_4 => w_port_4
    );

end architecture ARCH;

