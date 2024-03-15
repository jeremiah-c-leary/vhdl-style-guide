
architecture RTL of FIFO is

  signal sig1, sig2 : std_logic_vector(3 downto 0);
  constant c_cons1   , c_const2 : integer := 200;
  constant c_cons2 : integer := 200;

begin

  U_RAM : RAM_ARRAY
    generic map (
      G_WIDTH => 512     ,
      G_DEPTH => 2048 ,
      G_SIZE => 32
    )
    port map (
      I_DATA_A => data_a   ,
      I_DATA_B => data_b
    );

end architecture RTL;

