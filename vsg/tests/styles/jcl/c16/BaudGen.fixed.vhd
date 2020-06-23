
library IEEE;
  use IEEE.STD_LOGIC_1164.ALL;
  use IEEE.STD_LOGIC_ARITH.ALL;
  use IEEE.STD_LOGIC_UNSIGNED.ALL;
  use STD.TEXTIO.ALL;

--  Uncomment the following lines to use the declarations that are
--  provided for instantiating Xilinx primitive components.
--library UNISIM;
--use UNISIM.VComponents.all;

entity BAUDGEN is
  generic (
    BG_CLOCK_FREQ : integer;
    BG_BAUD_RATE  : integer
  );
  port (
    CLK_I  : in    std_logic;
    RST_I  : in    std_logic;
    CE_16  : out   std_logic
  );
end entity BAUDGEN;

architecture BEHAVIORAL of BAUDGEN is

  -- divide bg_clock_freq and bg_baud_rate
  -- by their common divisor...
  --

  function gcd (M, N: integer) return integer is
  begin

    if ((M mod N) = 0) then
      return N;
    else
      return gcd(N, M mod N);
    end if;

  end;

  constant common_div : integer := gcd(bg_clock_freq, 16 * bg_baud_rate);
  constant clock_freq : integer := bg_clock_freq     / common_div;
  constant baud_freq  : integer := 16 * bg_baud_rate / common_div;
  constant limit      : integer := clock_freq - baud_freq;

  signal counter      : integer range 0 to clock_freq - 1;

begin

  process (CLK_I) is
  begin

    if (CLK_I'event and CLK_I = '1') then
      CE_16 <= '0';    -- make CE_16 stay on for (at most) one cycle

      if (RST_I = '1') then
        counter <= 0;
      elsif (counter >= limit) then
        CE_16   <= '1';
        counter <= counter - limit;
      else
        counter <= counter + baud_freq;
      end if;
    end if;

  end process;

end architecture BEHAVIORAL;
