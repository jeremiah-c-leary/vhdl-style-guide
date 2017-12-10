
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
    DATAIN   : in    std_logic_vector (2 downto 0);
    ADDRESSX : out   std_logic_vector (9 downto 0);
    ADDRESSY : out   std_logic_vector (8 downto 0)
  );
end entity SYNCHRONIZER;

architecture BEHAVIORAL of SYNCHRONIZER is

  signal x, nX                   : STD_LOGIC_VECTOR (10 downto 0) := (others=>'0');
  signal y, nY                   : STD_LOGIC_VECTOR (20 downto 0) := (others=>'0');
  constant tpw : STD_LOGIC_VECTOR (1 downto 0) := "00";
  constant tbp : STD_LOGIC_VECTOR (1 downto 0) := "01";
  constant tdp : STD_LOGIC_VECTOR (1 downto 0) := "10";
  constant tfp : STD_LOGIC_VECTOR (1 downto 0) := "11";
  signal xstate                  : std_logic_vector (1 downto 0) := TPW;
  signal ystate                  : std_logic_vector (1 downto 0) := TPW;
  signal enabledisplay           : std_logic;
  signal addressofy, nAddressOfY : STD_LOGIC_VECTOR (8 downto 0);

begin

  nX            <= X+1;
  nY            <= Y+1;
  nAddressOfY   <= AddressOfY+1;
  HS            <= '0' when XState=TPW else
                   '1';
  VS            <= '0' when YState=TPW else
                   '1';
  EnableDisplay <= '1' when XState=TDP and YState=TDP else
                   '0';
  R             <= dataIn(0) when EnableDisplay='1' else
                   '0';
  B             <= dataIn(1) when EnableDisplay='1' else
                   '0';
  G             <= dataIn(2) when EnableDisplay='1' else
                   '0';
  AddressX      <= X(10 downto 1);
  AddressY      <= AddressOfY-30;

  process (Clk) is
  begin

    if (rising_edge(Clk)) then
      if (XState=TPW and X(7 downto 1)="1100000") then
        X      <= (others=>'0');
        XState <= TBP;
      elsif (XState=TBP and X(6 downto 1)="110000") then
        X      <= (others=>'0');
        XState <= TDP;
      elsif (XState=TDP and X(10 downto 1)="1010000000") then
        X      <= (others=>'0');
        XState <= TFP;
      elsif (XState=TFP and X(5 downto 1)="10000") then
        X          <= (others=>'0');
        XState     <= TPW;
        AddressOfY <= nAddressOfY;
      else
        X <= nX;
      end if;
      if (YState=TPW and Y(12 downto 1)="11001000000") then
        Y      <= (others=>'0');
        YState <= TBP;
      elsif (YState=TBP and Y(16 downto 1)="101101010100000") then
        Y      <= (others=>'0');
        YState <= TDP;
      elsif (YState=TDP and Y(20 downto 1)="1011101110000000000") then
        Y      <= (others=>'0');
        YState <= TFP;
      elsif (YState=TFP and Y(14 downto 1)="1111101000000") then
        Y          <= (others=>'0');
        X          <= (others=>'0');
        YState     <= TPW;
        XState     <= TPW;
        AddressOfY <= (others=>'0');
      else
        Y <= nY;
      end if;
    end if;

  end process;

end architecture BEHAVIORAL;
