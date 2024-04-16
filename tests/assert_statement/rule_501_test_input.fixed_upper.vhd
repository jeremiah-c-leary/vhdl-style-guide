
architecture ARCH of ENTITY1 is

begin

  ASSERT boolean REPORT "Something" SEVERITY FAILURE;

  assert boolean REPORT "Something" severity FAILURE;

  process begin

    LABEL : ASSERT boolean
      REPORT "Something"
      SEVERITY FAILURE;

    LABEL : assert boolean
      REPORT "Something"
      severity FAILURE;

    ASSERT boolean REPORT "Something" SEVERITY FAILURE;

    assert boolean REPORT "Something" severity FAILURE;

    ASSERT boolean
      REPORT "Something"
      SEVERITY FAILURE;

    assert boolean
      REPORT "Something"
      severity FAILURE;

  end process;

end architecture ARCH;
