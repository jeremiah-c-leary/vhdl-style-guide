
architecture ARCH of ENTITY1 is

begin

  ASSERT boolean REPORT "Something" SEVERITY FAILURE;

  ASSERT boolean report "Something" severity FAILURE;

  process begin

    LABEL : ASSERT boolean
      REPORT "Something"
      SEVERITY FAILURE;

    LABEL : ASSERT boolean
      report "Something"
      severity FAILURE;

    ASSERT boolean REPORT "Something" SEVERITY FAILURE;

    ASSERT boolean report "Something" severity FAILURE;

    ASSERT boolean
      REPORT "Something"
      SEVERITY FAILURE;

    ASSERT boolean
      report "Something"
      severity FAILURE;

  end process;

end architecture ARCH;
