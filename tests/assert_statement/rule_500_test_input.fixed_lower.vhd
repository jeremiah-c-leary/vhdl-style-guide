
architecture ARCH of ENTITY1 is

begin

  assert boolean REPORT "Something" SEVERITY FAILURE;

  assert boolean report "Something" severity FAILURE;

  process begin

    LABEL : assert boolean
      REPORT "Something"
      SEVERITY FAILURE;

    LABEL : assert boolean
      report "Something"
      severity FAILURE;

    assert boolean REPORT "Something" SEVERITY FAILURE;

    assert boolean report "Something" severity FAILURE;

    assert boolean
      REPORT "Something"
      SEVERITY FAILURE;

    assert boolean
      report "Something"
      severity FAILURE;

  end process;

end architecture ARCH;
