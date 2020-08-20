
entity BLOCK_EXAMPLE is
end entity BLOCK_EXAMPLE;

architecture RTL of BLOCK_EXAMPLE is

begin

  BLK : block is
  begin

    GEN : for ii in 0 to 7 generate

      BLK2 : block is
      begin

        GEN2 : for jj in 0 to 7 generate

        end generate GEN2; 

      end block BLK2;

    end generate GEN;

  end block BLK;

end architecture RTL;
