
architecture ARCH of ENTITY1 is

begin

  assert boolean
    report "Something"
    severity FAILURE;

   assert boolean
  report "Something"
    severity FAILURE;


  assert boolean
   report "Something"
  severity FAILURE;

  assert boolean
  report "Something"
 severity FAILURE;

  PROC : process (CLK) is
  begin

    assert 3 <= 7
      report "something";

  end process PROC;


end architecture ARCH;
