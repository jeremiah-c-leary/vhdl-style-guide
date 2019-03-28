
architecture RTL of ENTITY1 is

  signal sig1 : std_logic;
  signal sig2 : std_logic;

begin

  PROC_NAME : process (siG2) is
  begin

    siG1 <= '0';

    if (SIG2 = '0') then
      sIg1 <= '1';
    elsif (SiG2 = '1') then
      SIg1 <= '0';
    end if;

  end process PROC_NAME;

end architecture RTL;
