
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

  signal counter,       ncounter       : std_logic_vector(23 downto 0) := x"000000";
  signal buttonhistory, nbuttonhistory : std_logic_vector(1 downto 0) := "00";
  signal nexthistory                   : std_logic := '0';

begin

  ncounter       <= x"FFFFFF" when counter=x"FFFFFF" and Button='1' else
                    x"000000" when counter=x"000000" and Button='0' else
                    counter + 1 when Button='1' else
                    counter - 1;
  nexthistory    <= '0' when counter=x"000000" else
                    '1';
  nbuttonhistory <= nexthistory & buttonhistory(1);
  Dout           <= '1' when buttonhistory="01" else
                    '0';

  process (Clk) is
  begin

    if (Clk'event and Clk = '1') then
      counter       <= ncounter;
      buttonhistory <= nbuttonhistory;
    end if;

  end process;

end architecture BEHAVIORAL;
