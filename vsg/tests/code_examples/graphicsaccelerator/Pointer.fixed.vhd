
library IEEE;
  use IEEE.STD_LOGIC_1164.ALL;
  use IEEE.numeric_std.all;
  use IEEE.std_logic_unsigned.all;

entity POINTER is
  generic (
    INITX : std_logic_vector(9 downto 0);
    INITY : std_logic_vector(8 downto 0)
  );
  port (
    MOVEUP    : in    std_logic;
    MOVEDOWN  : in    std_logic;
    MOVELEFT  : in    std_logic;
    MOVERIGHT : in    std_logic;
    MOVE      : in    std_logic;
    CLK       : in    std_logic;
    HERE      : out   std_logic;
    X         : out   std_logic_vector(9 downto 0);
    Y         : out   std_logic_vector(8 downto 0);
    SYNCX     : in    std_logic_vector(9 downto 0);
    SYNCY     : in    std_logic_vector(8 downto 0)
  );
end entity POINTER;

architecture BEHAVIORAL of POINTER is

  signal rx : std_logic_vector(9 downto 0) := initX;
  signal ry : std_logic_vector(8 downto 0) := initY;

begin

  Here <= '1' when syncX(9 downto 3)=rx(9 downto 3) and
          syncY(8 downto 3)=ry(8 downto 3) else
          '0';
  X    <= rx;
  Y    <= ry;

  process (Clk) is
  begin

    if (Clk'event and Clk = '1') then
      if (Move = '1') then
        if (MoveLeft = '1' and MoveRight = '0') then
          if (not (rx = "0000000000")) then
            rx <= rx - 1;
          end if;
        elsif (MoveLeft = '0' and MoveRight = '1') then
          if (not (rx = "1001111111")) then
            rx <= rx + 1;
          end if;
        end if;
        if (MoveUp = '1' and MoveDown = '0') then
          if (not (ry = "000000000")) then
            ry <= ry - 1;
          end if;
        elsif (MoveUp = '0' and MoveDown = '1') then
          if (not (ry = "111011111")) then
            ry <= ry + 1;
          end if;
        end if;
      end if;
    end if;

  end process;

end architecture BEHAVIORAL;
