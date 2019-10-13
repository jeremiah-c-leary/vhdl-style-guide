
architecture RTL of ENTITY1 is

begin

  -- This should pass

  LABEL1 : process (A) is
  begin

  end process LABEL1;

  -- This should fail

  LABEL1 :
  process (A) is
  begin

  end process LABEL1;

  -- This should fail

  LABEL1 :

  process (A) is
  begin

  end process LABEL1;

  -- This should be ignored

  LABEL2 : A <= B when Y = '0' else
                '1';

  -- This should be ignored

  LABEL2 :
  A <= B when Y = '0' else
       '1';

  -- This should be ignored

  LABEL2 :

  A <= B when Y = '0' else
       '1';

  -- This should not be flagged

  process (A) is
  begin

  end process LABEL1;

end architecture RTL;
