
architecture ARCH of ENTITY1 is

begin

  ASSERT boolean REPORT "Something" SEVERITY FAILURE;

  assert boolean report "Something" SEVERITY FAILURE;

  process begin

    LABEL : ASSERT boolean
      REPORT "Something"
      SEVERITY FAILURE;

    LABEL : assert boolean
      report "Something"
      SEVERITY FAILURE;

    ASSERT boolean REPORT "Something" SEVERITY FAILURE;

    assert boolean report "Something" SEVERITY FAILURE;

    ASSERT boolean
      REPORT "Something"
      SEVERITY FAILURE;

    assert boolean
      report "Something"
      SEVERITY FAILURE;

  end process;

end architecture ARCH;
