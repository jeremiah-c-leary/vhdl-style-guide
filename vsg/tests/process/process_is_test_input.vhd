
architecture RTL of ENT is

begin

  PROC1 : process (a, b ,c) is
  begin
  end process PROC1;

  PROC1 : process (a, b, c)
  is
  begin
  end process PROC1;

  PROC1 : process (a, b, c)
  is begin
  end process PROC1;

  PROC1 : process (a, b, c) is begin
  end process PROC1;

  PROC1 : process (a, b ,c) is-- This is a comment
  begin
  end process PROC1;

  PROC1 : process (a, b ,c)is
  begin
  end process PROC1;

  PROC1 : process (a, b ,c)is begin
  end process PROC1;

  PROC1 : process (a, b, c)
  begin
  end process PROC1;

end architecture RTL;
