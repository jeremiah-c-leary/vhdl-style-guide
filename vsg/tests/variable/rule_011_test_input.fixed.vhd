
architecture RTL of ENTITY1 is


begin

  PROC_NAME : process () is

    variable var1 : std_logic;
    variable var2 : std_logic;
    variable var3 : std_logic;
    variable var4 : std_logic;

  begin

    var1 <= '0';

    if (var2 = '0') then
      var3 <= '1';
    elsif (var2 = '1') then
      var4 <= '0';
    end if;

    var1 <= var2 & var3 & var4;

  end process PROC_NAME;

end architecture RTL;

