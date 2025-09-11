library IEEE;
  use ieee.std_logic_1164.all;
  use ieee.numeric_std.all;
  use ieee.std_logic_unsigned.all;
  use ieee.std_logic_arith.all;

entity FRAMEBUFFER is
  port (
    INX         : in    std_logic_vector(9 downto 0);
    INY         : in    std_logic_vector(8 downto 0);
    OUTX        : in    std_logic_vector(9 downto 0);
    OUTY        : in    std_logic_vector(8 downto 0);
    OUTCOLOR    : out   std_logic_vector(2 downto 0);
    INCOLOR     : in    std_logic_vector(2 downto 0);
    BUFFERWRITE : in    std_logic;
    CLK         : in    std_logic
  );
end entity FRAMEBUFFER;

architecture BEHAVIORAL of FRAMEBUFFER is

  type fbuffer is array(0 to 524288 / 16 - 1) of std_logic_vector(2 downto 0);

  impure function initfb return fbuffer is

    variable temp : fbuffer;
    variable i    : integer;

  begin

    for i in 0 to 524288 / 16 - 1 loop

      temp(i) := "000";

    end loop;

    return temp;

  end function initfb;

  signal mybuffer                  : fbuffer := initfb;
  signal addresswrite, addressread : std_logic_vector(14 downto 0);
  signal temp                      : std_logic_vector(2 downto 0);

begin

  addresswrite <= INX(9 downto 2) & INY(8 downto 2);
  addressread  <= OUTX(9 downto 2) & OUTY(8 downto 2);
  OUTCOLOR     <= temp;

  process (CLK) is
  begin

    if (rising_edge(CLK)) then
      if (BUFFERWRITE = '1') then
        mybuffer(conv_integer(addresswrite)) <= INCOLOR;
      end if;
      temp <= mybuffer(conv_integer(addressread));
    end if;

  end process;

end architecture BEHAVIORAL;
