library IEEE;
  use ieee.std_logic_1164.all;
  use ieee.std_logic_arith.all;
  use ieee.std_logic_unsigned.all;
  use std.textio.all;

--  Uncomment the following lines to use the declarations that are
--  provided for instantiating Xilinx primitive components.
-- library UNISIM;
-- use UNISIM.VComponents.all;

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

  end function gcd;

  constant common_div : integer := gcd(BG_CLOCK_FREQ, 16 * BG_BAUD_RATE);
  constant clock_freq : integer := BG_CLOCK_FREQ     / common_div;
  constant baud_freq  : integer := 16 * BG_BAUD_RATE / common_div;
  constant limit      : integer := clock_freq - baud_freq;

  signal counter      : integer range 0 to clock_freq - 1;

begin

  process (CLK_I) is
  begin

    if (rising_edge(CLK_I)) then
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
