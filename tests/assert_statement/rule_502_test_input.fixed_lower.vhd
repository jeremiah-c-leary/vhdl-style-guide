
architecture ARCH of ENTITY1 is

begin

  ASSERT boolean REPORT "Something" severity FAILURE;

  assert boolean report "Something" severity FAILURE;

  process begin

    LABEL : ASSERT boolean
      REPORT "Something"
      severity FAILURE;

    LABEL : assert boolean
      report "Something"
      severity FAILURE;

    ASSERT boolean REPORT "Something" severity FAILURE;

    assert boolean report "Something" severity FAILURE;

    ASSERT boolean
      REPORT "Something"
      severity FAILURE;

    assert boolean
      report "Something"
      severity FAILURE;

  end process;

end architecture ARCH;
