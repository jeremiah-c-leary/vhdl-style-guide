library IEEE;
  use ieee.std_logic_1164.all;
  use ieee.numeric_std.all;
  use ieee.std_logic_unsigned.all;

entity FREQDIV is
  port (
    CLK  : in    std_logic;
    CLK2 : out   std_logic
  );
end entity FREQDIV;

architecture BEHAVIORAL of FREQDIV is

  signal counter : std_logic_vector(19 downto 0);

begin

  CLK2 <= counter(19);

  process (CLK) is
  begin

    if (CLK'event and CLK = '1') then
      counter <= counter + 1;
    end if;

  end process;

end architecture BEHAVIORAL;
