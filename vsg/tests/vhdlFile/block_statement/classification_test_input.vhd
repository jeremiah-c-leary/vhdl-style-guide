
architecture RTL of BLOCK_EXAMPLE is

begin

  -- correct block format
  BLK : block is

  begin

    BLK2 : block is
    begin

        BLK3 : block is
        begin

        end block BLK3;

    end block BLK2;

    BLK4 : block is
    begin

        BLK5 : block is
        begin

            BLK6 : block is

            begin

            end block BLK6;

        end block BLK5;

    end block BLK4;

  end block BLK;

  b1  : block begin end block;

  process begin end process;

  b1 : block begin

      process begin end process;

  end block;

  assert true report "something" severity failure;

end architecture RTL;
