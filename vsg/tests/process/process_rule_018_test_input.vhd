
architecture test of some_entity is

begin


  PROC_LABEL1 : process
  begin
  end process PROC_LABEL1;

  -- Test with missing end label
  PROC_LABEL2 : process
  begin
  end process;

  -- Test with missing front and end label
  process
  begin
  end process;

  -- Test with missing front label
  process
  begin
  end process PROC_LABEL3;

end architecture test;
