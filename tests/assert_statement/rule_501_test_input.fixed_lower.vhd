
architecture ARCH of ENTITY1 is

begin

  ASSERT boolean report "Something" SEVERITY FAILURE;

  assert boolean report "Something" severity FAILURE;

  process begin

    LABEL : ASSERT boolean
      report "Something"
      SEVERITY FAILURE;

    LABEL : assert boolean
      report "Something"
      severity FAILURE;

    ASSERT boolean report "Something" SEVERITY FAILURE;

    assert boolean report "Something" severity FAILURE;

    ASSERT boolean
      report "Something"
      SEVERITY FAILURE;

    assert boolean
      report "Something"
      severity FAILURE;

  end process;

end architecture ARCH;
