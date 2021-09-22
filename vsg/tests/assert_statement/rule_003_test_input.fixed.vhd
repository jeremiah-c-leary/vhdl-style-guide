
architecture ARCH of ENTITY1 is

begin

  assert boolean report "Something" severity FAILURE;

  process begin

    LABEL : assert boolean
 report "Something" severity FAILURE;
  
    LABEL : assert boolean
      report "Something" severity FAILURE;
  
    LABEL : assert boolean
 report "Something"
      severity FAILURE;
  
    LABEL : assert boolean
      report "Something"
      severity FAILURE;
  
    assert boolean
 report "Something" severity FAILURE;
  
    assert boolean
      report "Something" severity FAILURE;
  
    assert boolean
 report "Something"
      severity FAILURE;
  
    assert boolean
      report "Something"
      severity FAILURE;

  end process;

  assert boolean report "Something" severity FAILURE;

end architecture ARCH;
