
architecture ARCH of ENTITY

begin

  -- comment
   -- comment
    -- comment

  PROC_1 : process (a) is
    -- comment
     -- comment
  begin

    -- comment
    a <= b;             -- comment
    b <= c;             -- comment
    d <= e;             -- comment

  end process PROC_1:


  PROC_1 : process (a) is
    -- comment
     -- comment
  begin

    -- comment
    a <= b;             -- comment
    b <= c;            -- comment
    d <= e;             -- comment

  end process PROC_1:


  PROC_1 : process (a) is
      variable a : integer 0 to 10;    -- comment
      variable b : natural 0 to 256;       -- comment
  begin

    -- comment
    a <= b;              -- comment
    b <= c;             -- comment
    d <= e;             -- comment

  end process PROC_1:

end architecture ARCH;
