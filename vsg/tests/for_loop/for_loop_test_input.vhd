
architecture ARCH of ENTITY1 is

begin

  PROC_1 : process (A) is
  begin

    for index in 4 to 23 loop
       sig1(index) <= '0';
    end loop;

  end process PROC_1;

end architecture ARCH;
