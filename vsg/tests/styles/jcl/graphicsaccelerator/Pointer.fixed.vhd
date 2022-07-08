library IEEE;
  use ieee.std_logic_1164.all;
  use ieee.numeric_std.all;
  use ieee.std_logic_unsigned.all;

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

  signal rx : std_logic_vector(9 downto 0) := INITX;
  signal ry : std_logic_vector(8 downto 0) := INITY;

begin

  HERE <= '1' when SYNCX(9 downto 3)=rx(9 downto 3) and
                   SYNCY(8 downto 3)=ry(8 downto 3) else
          '0';
  X    <= rx;
  Y    <= ry;

  process (CLK) is
  begin

    if (rising_edge(CLK)) then
      if (MOVE = '1') then
        if (MOVELEFT = '1' and MOVERIGHT = '0') then
          if (not (rx = "0000000000")) then
            rx <= rx - 1;
          end if;
        elsif (MOVELEFT = '0' and MOVERIGHT = '1') then
          if (not (rx = "1001111111")) then
            rx <= rx + 1;
          end if;
        end if;
        if (MOVEUP = '1' and MOVEDOWN = '0') then
          if (not (ry = "000000000")) then
            ry <= ry - 1;
          end if;
        elsif (MOVEUP = '0' and MOVEDOWN = '1') then
          if (not (ry = "111011111")) then
            ry <= ry + 1;
          end if;
        end if;
      end if;
    end if;

  end process;

end architecture BEHAVIORAL;
