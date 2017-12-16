
architecture ARCH of ENTITY1 is

begin

  PROC_1 : process (A) is
  begin

    for index in 4 to 23 loop
       sig1(index) <= '0';
    end loop;

  end process PROC_1;

  PROC_2 : process (B) is
  begin

    if (A = 1) then
       for index in 3 to 72 loop
        sig1(index) <= '1';
       for j in 0 to 32 loop
          sig2(index) <= '0';
         end loop;
      end loop;
    elsif (B = 0) then
      for index in 2 to 16 loop
        sig3(index) <= '1';
      end loop;
    end if;

  end process PROC_2;

end architecture ARCH;
