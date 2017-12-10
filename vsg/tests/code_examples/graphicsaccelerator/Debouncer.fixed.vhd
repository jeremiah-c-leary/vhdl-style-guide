
library IEEE;
  use IEEE.STD_LOGIC_1164.ALL;
  use IEEE.numeric_std.all;
  use IEEE.std_logic_unsigned.all;

entity DEBOUNCER is
  port (
    CLK    : in    std_logic;
    BUTTON : in    std_logic;
    DOUT   : out   std_logic
  );
end entity DEBOUNCER;

architecture BEHAVIORAL of DEBOUNCER is

  signal counter, nCounter             : STD_LOGIC_VECTOR(23 downto 0) := x"000000";
  signal buttonhistory, nButtonHistory : STD_LOGIC_VECTOR(1 downto 0) := "00";
  signal nexthistory                   : std_logic := '0';

begin

  nCounter       <= x"FFFFFF" when Counter=x"FFFFFF" and Button='1' else
                    x"000000" when Counter=x"000000" and Button='0' else
                    Counter+1 when Button='1' else
                    Counter-1;
  nextHistory    <= '0' when Counter=x"000000" else
                    '1';
  nButtonHistory <= nextHistory & ButtonHistory(1);
  Dout           <= '1' when ButtonHistory="01" else
                    '0';

  process (Clk) is
  begin

    if (rising_edge(Clk)) then
      Counter       <= nCounter;
      ButtonHistory <= nButtonHistory;
    end if;

  end process;

end architecture BEHAVIORAL;
