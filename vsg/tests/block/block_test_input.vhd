
entity BLOCK_EXAMPLE is
end entity BLOCK_EXAMPLE;

architecture RTL of BLOCK_EXAMPLE is

begin

  -- correct block format
  BLK : block is
    signal private : integer;

    type int_array is array (natural range <>) of integer;

    constant vals : int_array(1 downto 0) := (
      3, 10
    );
  begin
    private <= vals(1);

    U_INST1 : INST1
      port map (
        PORT_1 => w_port_1,
        PORT_2 => w_port_2,
        PORT_3 => w_port_3
      );
    
  end block BLK;

end architecture RTL;

