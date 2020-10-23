
architecture RTL of ENTITY1 is

begin

  -- This should pass

  LABEL1 : process is
  begin

  end process LABEL1;

  -- This should fail

  process is
  begin

  end process;

  -- This should fail

  process is
  begin

  end process;

  -- This should pass

  LABEL1 : process is
  begin

  end process LABEL1;

  -- This should fail

  process is
  begin

  end process;

  -- This should fail

  process is
  begin

  end process;

end architecture RTL;
