
architecture RTL of ENTITY1 is

begin

  U_FIFO : FIFO
    generic map (GENERIC1, GENERIC2 => 3
       GENERIC0 => 3,
       GENERIC3 => 4, GENERIC5, GENERIC4 => 5
       GENERIC7 => 4, GENERIC8, GENERIC9,
       GENERIC6 => 7
    )
    port map (PORT1, PORT2 => 3,
       PORT3, PORT4 => 5, PORT5 => 6,
       PORT6 => 7,
       PORT7 => 4
    );

end architecture RTL;
