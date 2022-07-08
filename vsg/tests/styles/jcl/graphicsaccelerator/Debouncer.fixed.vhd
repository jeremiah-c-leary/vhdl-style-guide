library IEEE;
  use ieee.std_logic_1164.all;
  use ieee.numeric_std.all;
  use ieee.std_logic_unsigned.all;

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

  ncounter       <= x"FFFFFF" when counter=x"FFFFFF" and BUTTON='1' else
                    x"000000" when counter=x"000000" and BUTTON='0' else
                    counter + 1 when BUTTON='1' else
                    counter - 1;
  nexthistory    <= '0' when counter=x"000000" else
                    '1';
  nbuttonhistory <= nexthistory & buttonhistory(1);
  DOUT           <= '1' when buttonhistory="01" else
                    '0';

  process (CLK) is
  begin

    if (rising_edge(CLK)) then
      counter       <= ncounter;
      buttonhistory <= nbuttonhistory;
    end if;

  end process;

end architecture BEHAVIORAL;
