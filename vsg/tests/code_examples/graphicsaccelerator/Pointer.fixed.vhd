
library IEEE;
  use IEEE.STD_LOGIC_1164.ALL;
  use IEEE.numeric_std.all;
  use IEEE.std_logic_unsigned.all;

entity POINTER is
  generic (
    INITX : STD_LOGIC_VECTOR
    INITY : STD_LOGIC_VECTOR (8 downto 0)
  );
  port (
    MOVEUP    : in    std_logic;
    MOVEDOWN  : in    std_logic;
    MOVELEFT  : in    std_logic;
    MOVERIGHT : in    std_logic;
    MOVE      : in    std_logic;
    CLK       : in    std_logic;
    HERE      : out   std_logic;
    X         : out   std_logic_vector (9 downto 0);
    Y         : out   std_logic_vector (8 downto 0);
    SYNCX     : in    std_logic_vector (9 downto 0);
    SYNCY     : in    std_logic_vector (8 downto 0)
  );
end entity POINTER;

architecture BEHAVIORAL of POINTER is

  signal rx : std_logic_vector (9 downto 0) := initX;
  signal ry : std_logic_vector (8 downto 0) := initY;

begin

  Here <= '1' when syncX(9 downto 3)=rX(9 downto 3) and
          syncY(8 downto 3)=rY(8 downto 3) else
          '0';
  X    <= rX;
  Y    <= rY;

  process (Clk) is
  begin

    if (rising_edge(Clk)) then
      if (Move = '1') then
        if (MoveLeft = '1' and MoveRight = '0') then
          if (not (rX = "0000000000")) then
            rX <= rX - 1;
          end if;
        elsif (MoveLeft = '0' and MoveRight = '1') then
          if (not (rX = "1001111111")) then
            rX <= rX + 1;
          end if;
        end if;
        if (MoveUp = '1' and MoveDown = '0') then
          if (not (rY = "000000000")) then
            rY <= rY - 1;
          end if;
        elsif (MoveUp = '0' and MoveDown = '1') then
          if (not (rY = "111011111")) then
            rY <= rY + 1;
          end if;
        end if;
      end if;
    end if;

  end process;

end architecture BEHAVIORAL;
