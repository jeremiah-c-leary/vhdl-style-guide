
architecture ARCH of ENTITY is

begin

  a <= sig1 when b = '1' else
       sig2 when b = '0' else
       sig3;

  process
  begin

    d <= sig1 when b = '1' else--This is a comment
         sig2 when c = '0' else -- This is a comment
         sig3 when d = '1' else
         sig4;

  end process;

  -- Violations below

  a <= sig1 when b = '1'
       else sig2 when b = '0'
else sig3;

  process
  begin

    d <= sig1 when b = '1'--This is a comment
else sig2 when c = '0'  -- This is a comment
         else sig3 when d = '1'
         else sig4;

  end process;

  a <= b when (c = '1')else d;
  a <= b when (c = '1'else d;

end architecture ARCH;
