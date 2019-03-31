
library IEEE;
  use IEEE.std_logic_1164.all;
  use IEEE.numeric_std.all;
  use IEEE.std_logic_unsigned.all;

entity SYNCHRONIZER is
  port (
    R        : out   std_logic;
    G        : out   std_logic;
    B        : out   std_logic;
    HS       : out   std_logic;
    VS       : out   std_logic;
    CLK      : in    std_logic;
    DATAIN   : in    std_logic_vector(2 downto 0);
    ADDRESSX : out   std_logic_vector(9 downto 0);
    ADDRESSY : out   std_logic_vector(8 downto 0)
  );
end entity SYNCHRONIZER;

architecture BEHAVIORAL of SYNCHRONIZER is

  signal x,          nx          : std_logic_vector(10 downto 0) := (others=>'0');
  signal y,          ny          : std_logic_vector(20 downto 0) := (others=>'0');
  constant tpw : std_logic_vector(1 downto 0) := "00";
  constant tbp : std_logic_vector(1 downto 0) := "01";
  constant tdp : std_logic_vector(1 downto 0) := "10";
  constant tfp : std_logic_vector(1 downto 0) := "11";
  signal xstate                  : std_logic_vector(1 downto 0) := tpw;
  signal ystate                  : std_logic_vector(1 downto 0) := tpw;
  signal enabledisplay           : std_logic;
  signal addressofy, naddressofy : std_logic_vector(8 downto 0);

begin

  nx            <= x + 1;
  ny            <= y + 1;
  naddressofy   <= addressofy + 1;
  HS            <= '0' when xstate=tpw else
                   '1';
  VS            <= '0' when ystate=tpw else
                   '1';
  enabledisplay <= '1' when xstate=tdp and ystate=tdp else
                   '0';
  R             <= dataIn(0) when enabledisplay='1' else
                   '0';
  B             <= dataIn(1) when enabledisplay='1' else
                   '0';
  G             <= dataIn(2) when enabledisplay='1' else
                   '0';
  AddressX      <= x(10 downto 1);
  AddressY      <= addressofy - 30;

  process (Clk) is
  begin

    if (Clk'event and Clk = '1') then
      if (xstate=tpw and x(7 downto 1)="1100000") then
        x      <= (others=>'0');
        xstate <= tbp;
      elsif (xstate=tbp and x(6 downto 1)="110000") then
        x      <= (others=>'0');
        xstate <= tdp;
      elsif (xstate=tdp and x(10 downto 1)="1010000000") then
        x      <= (others=>'0');
        xstate <= tfp;
      elsif (xstate=tfp and x(5 downto 1)="10000") then
        x          <= (others=>'0');
        xstate     <= tpw;
        addressofy <= naddressofy;
      else
        x <= nx;
      end if;
      if (ystate=tpw and y(12 downto 1)="11001000000") then
        y      <= (others=>'0');
        ystate <= tbp;
      elsif (ystate=tbp and y(16 downto 1)="101101010100000") then
        y      <= (others=>'0');
        ystate <= tdp;
      elsif (ystate=tdp and y(20 downto 1)="1011101110000000000") then
        y      <= (others=>'0');
        ystate <= tfp;
      elsif (ystate=tfp and y(14 downto 1)="1111101000000") then
        y          <= (others=>'0');
        x          <= (others=>'0');
        ystate     <= tpw;
        xstate     <= tpw;
        addressofy <= (others=>'0');
      else
        y <= ny;
      end if;
    end if;

  end process;

end architecture BEHAVIORAL;
