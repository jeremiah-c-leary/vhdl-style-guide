
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
  end block BLK;

end architecture RTL;

