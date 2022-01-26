
architecture RTL of BLOCK_EXAMPLE is

begin

  b1 : block begin

      process begin end process;

  end block;

  assert true report "something" severity failure;

end architecture RTL;
