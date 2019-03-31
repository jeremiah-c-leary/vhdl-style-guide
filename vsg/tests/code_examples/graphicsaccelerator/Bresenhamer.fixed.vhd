
library IEEE;
  use IEEE.STD_LOGIC_1164.ALL;
  use IEEE.numeric_std.all;
  use IEEE.std_logic_unsigned.all;

entity BRESENHAMER is
  port (
    WRITEENABLE : out   std_logic;
    X           : out   std_logic_vector(9 downto 0);
    Y           : out   std_logic_vector(8 downto 0);
    X1          : in    std_logic_vector(9 downto 0);
    Y1          : in    std_logic_vector(8 downto 0);
    X2          : in    std_logic_vector(9 downto 0);
    Y2          : in    std_logic_vector(8 downto 0);
    SS          : out   std_logic_vector(3 downto 0);
    CLK         : in    std_logic;
    STARTDRAW   : in    std_logic;
    DBG         : out   std_logic_vector(11 downto 0);
    RESET       : in    std_logic
  );
end entity BRESENHAMER;

architecture BEHAVIORAL of BRESENHAMER is

  signal myx1,     myx2                                             : std_logic_vector(11 downto 0);
  signal myy1,     myy2                                             : std_logic_vector(11 downto 0);
  signal p, p0_1, p0_2, p0_3, p0_4, p0_5, p0_6, p0_7, p0_8          : std_logic_vector(11 downto 0);
  signal p_1, p_2, p_3, p_4, p_5, p_6, p_7, p_8                     : std_logic_vector(11 downto 0);
  signal ndx,      ndy                                              : std_logic_vector(11 downto 0);
  signal dx, dy, t_2dx, t_2dy, neg_dx, neg_dy, t_2neg_dx, t_2neg_dy : std_logic_vector(11 downto 0);
  signal dx_minus_dy                                                : std_logic_vector(11 downto 0);
  signal minus_dx_minus_dy                                          : std_logic_vector(11 downto 0);
  signal minus_dx_plus_dy                                           : std_logic_vector(11 downto 0);
  signal dx_plus_dy                                                 : std_logic_vector(11 downto 0);
  signal state                                                      : std_logic_vector(3 downto 0) := "0000";
  signal condx1x2, condy1y2                                         : std_logic;
  constant idle  : std_logic_vector(3 downto 0) := "0000";
  constant init  : std_logic_vector(3 downto 0) := "0001";
  constant case1 : std_logic_vector(3 downto 0) := "0010";
  constant case2 : std_logic_vector(3 downto 0) := "0011";
  constant case3 : std_logic_vector(3 downto 0) := "0100";
  constant case4 : std_logic_vector(3 downto 0) := "0101";
  constant case5 : std_logic_vector(3 downto 0) := "0110";
  constant case6 : std_logic_vector(3 downto 0) := "0111";
  constant case7 : std_logic_vector(3 downto 0) := "1000";
  constant case8 : std_logic_vector(3 downto 0) := "1001";
  constant clear : std_logic_vector(3 downto 0) := "1010";
  signal ccounter                                                   : std_logic_vector(18 downto 0) := "0000000000000000000";

begin

  ndx               <= ("00" & X2) - ("00" & X1);
  ndy               <= ("000" & Y2) - ("000" & Y1);
  neg_dx            <= 0 - dx;
  neg_dy            <= 0 - dy;
  dbg               <= p;
  dx_minus_dy       <= dx + neg_dy;
  minus_dx_minus_dy <= neg_dx + neg_dy;
  minus_dx_plus_dy  <= neg_dx + dy;
  dx_plus_dy        <= dx + dy;
  t_2dy             <= dy(10 downto 0) & '0';
  t_2dx             <= dx(10 downto 0) & '0';
  t_2neg_dy         <= neg_dy(10 downto 0) & '0';
  t_2neg_dx         <= neg_dx(10 downto 0) & '0';
  p0_1              <= t_2dy + neg_dx;
  p0_2              <= t_2dx + neg_dy;
  p0_3              <= t_2neg_dx + dy;
  p0_4              <= t_2dy + neg_dx;
  p0_5              <= t_2neg_dy + dx;
  p0_6              <= t_2neg_dx + dy;
  p0_7              <= t_2dx + neg_dy;
  p0_8              <= t_2neg_dy + dx;
  p_1               <= p + t_2dy when p(11)='1' else
                       p + t_2dy + t_2neg_dx;
  p_2               <= p + t_2dx when p(11)='1' else
                       p + t_2dx + t_2neg_dy;
  p_3               <= p + t_2neg_dx when p(11)='1' else
                       p + t_2neg_dx + t_2neg_dy;
  p_4               <= p + t_2dy when p(11)='1' else
                       p + t_2dy + t_2dx;
  p_5               <= p + t_2neg_dy when p(11)='1' else
                       p + t_2neg_dy + t_2dx;
  p_6               <= p + t_2neg_dx when p(11)='1' else
                       p + t_2neg_dx + t_2dy;
  p_7               <= p + t_2dx when p(11)='1' else
                       p + t_2dx + t_2dy;
  p_8               <= p + t_2neg_dy when p(11)='1' else
                       p + t_2neg_dy + t_2neg_dx;
  X                 <= ccounter(9 downto 0) when state = CLEAR else
                       myx1(9 downto 0);
  Y                 <= ccounter(18 downto 10) when state = CLEAR else
                       myy1(8 downto 0);
  SS                <= state;
  WriteEnable       <= '0' when state = IDLE or state = INIT else
                       '1';

  process (Clk) is
  begin

    if (Clk'event and Clk = '1') then
      if (state = IDLE) then
        if (Reset = '1') then
          state    <= CLEAR;
          ccounter <= (others=>'0');
        elsif (StartDraw = '1') then
          myx1(9 downto 0)   <= X1;
          myx1(11 downto 10) <= "00";
          myy1(8 downto 0)   <= Y1;
          myy1(11 downto 9)  <= "000";
          myx2(9 downto 0)   <= X2;
          myx2(11 downto 10) <= "00";
          myy2(8 downto 0)   <= Y2;
          myy2(11 downto 9)  <= "000";
          dx                 <= ndx;
          dy                 <= ndy;
          state              <= INIT;
        end if;
      elsif (state = INIT) then
        if (dx(11) = '0' and dy(11) = '0' and dx_minus_dy(11) = '0') then
          state <= CASE1;
          p     <= p0_1;
        elsif (dx(11) = '0' and dy(11) = '0' and dx_minus_dy(11) = '1') then
          state <= CASE2;
          p     <= p0_2;
        elsif (dx(11) = '1' and dy(11) = '0' and minus_dx_minus_dy(11) = '1') then
          state <= CASE3;
          p     <= p0_3;
        elsif (dx(11) = '1' and dy(11) = '0' and minus_dx_minus_dy(11) = '0') then
          state <= CASE4;
          p     <= p0_4;
        elsif (dx(11) = '1' and dy(11) = '1' and minus_dx_plus_dy(11) = '0') then
          state <= CASE5;
          p     <= p0_5;
        elsif (dx(11) = '1' and dy(11) = '1' and minus_dx_plus_dy(11) = '1') then
          state <= CASE6;
          p     <= p0_6;
        elsif (dx(11) = '0' and dy(11) = '1' and dx_plus_dy(11) = '1') then
          state <= CASE7;
          p     <= p0_7;
        else
          state <= CASE8;
          p     <= p0_8;
        end if;
      elsif (state = CASE1) then
        if (myx1 = myx2) then
          state <= IDLE;
        else
          myx1 <= myx1 + 1;
          p    <= p_1;
          if (p(11) = '0') then
            myy1 <= myy1 + 1;
          end if;
        end if;
      elsif (state = CASE2) then
        if (myy1 = myy2) then
          state <= IDLE;
        else
          myy1 <= myy1 + 1;
          p    <= p_2;
          if (p(11) = '0') then
            myx1 <= myx1 + 1;
          end if;
        end if;
      elsif (state = CASE3) then
        if (myy1 = myy2) then
          state <= IDLE;
        else
          myy1 <= myy1 + 1;
          p    <= p_3;
          if (p(11) = '0') then
            myx1 <= myx1 - 1;
          end if;
        end if;
      elsif (state = CASE4) then
        if (myx1 = myx2) then
          state <= IDLE;
        else
          myx1 <= myx1 - 1;
          p    <= p_4;
          if (p(11) = '0') then
            myy1 <= myy1 + 1;
          end if;
        end if;
      elsif (state = CASE5) then
        if (myx1 = myx2) then
          state <= IDLE;
        else
          myx1 <= myx1 - 1;
          p    <= p_5;
          if (p(11) = '0') then
            myy1 <= myy1 - 1;
          end if;
        end if;
      elsif (state = CASE6) then
        if (myy1 = myy2) then
          state <= IDLE;
        else
          myy1 <= myy1 - 1;
          p    <= p_6;
          if (p(11) = '0') then
            myx1 <= myx1 - 1;
          end if;
        end if;
      elsif (state = CASE7) then
        if (myy1 = myy2) then
          state <= IDLE;
        else
          myy1 <= myy1 - 1;
          p    <= p_7;
          if (p(11) = '0') then
            myx1 <= myx1 + 1;
          end if;
        end if;
      elsif (state = CASE8) then
        if (myx1 = myx2) then
          state <= IDLE;
        else
          myx1 <= myx1 + 1;
          p    <= p_8;
          if (p(11) = '0') then
            myy1 <= myy1 - 1;
          end if;
        end if;
      elsif (state = CLEAR) then
        ccounter <= ccounter + 1;
        if (ccounter = "1111111111111111111") then
          state <= IDLE;
        end if;
      end if;
    end if;

  end process;

end architecture BEHAVIORAL;
