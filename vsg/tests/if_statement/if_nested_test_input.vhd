

architecture RTL of ENTITY1 is

begin

  PROC_1 : process (A, B, C) is
  begin

    -- This is not an error
    if (A = '1' and B = '1') then 
      X <= '1';
      if (C = '1') then
        X <= '0';
        if (D = '0') then
          X <= '1';
        end if;
      end if;
    end if;
    X <= '0';  -- This should be an error 

    X <= '1';  -- This should be an error
    if (A = '1' and B = '1') then 
      X <= '1';
      if (C = '1') then
        X <= '0';
        if (D = '0') then
          X <= '1';
        end if;
      end if;
    end if;

    X <= '0';  -- This should not be an error 

  end process PROC_1;


end architecture RTL;
