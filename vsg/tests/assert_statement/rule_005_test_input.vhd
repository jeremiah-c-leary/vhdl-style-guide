
architecture ARCH of ENTITY1 is

begin

  assert boolean report "Something" severity FAILURE;

  process begin

    LABEL : assert boolean report "Something" severity FAILURE;
  
    LABEL : assert boolean
      report "Something" severity FAILURE;
  
    LABEL : assert boolean report "Something"
      severity FAILURE;
  
    LABEL : assert boolean
      report "Something"
      severity FAILURE;
  
    assert boolean report "Something" severity FAILURE;
  
    assert boolean
      report "Something" severity FAILURE;
  
    assert boolean report "Something"
      severity FAILURE;
  
    assert boolean
      report "Something"
      severity FAILURE;

    if a then
      assert (sel_0(4 downto 0) = "11001") report "Results wrong" severity warning;
    else
      assert (sel_0(4 downto 0) = "11001") report "Results wrong" severity warning;
    end if;

  end process;

  assert boolean report "Something" severity FAILURE;

end architecture ARCH;
