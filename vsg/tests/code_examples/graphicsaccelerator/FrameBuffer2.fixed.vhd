
library IEEE;
  use IEEE.STD_LOGIC_1164.ALL;
  use IEEE.NUMERIC_STD.ALL;
  use IEEE.std_logic_unsigned.all;
  use IEEE.STD_LOGIC_ARITH.ALL;

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

  type fbuffer is array (0 to 524288 / 16 - 1) of std_logic_vector(2 downto 0);

  impure function initFB return FBuffer is
    variable temp : fbuffer;
    variable i    : integer;
  begin
    for i in 0 to 524288 / 16 - 1 loop
      temp(i) := "000";
    end loop;
    return temp;
  end initFB;

  signal mybuffer                  : fbuffer := initFB;
  signal addresswrite, addressread : std_logic_vector(14 downto 0);
  signal temp                      : std_logic_vector(2 downto 0);

begin

  addresswrite <= inX(9 downto 2) & inY(8 downto 2);
  addressread  <= outX(9 downto 2) & outY(8 downto 2);
  outColor     <= temp;

  process (clk) is
  begin

    if (Clk'event and Clk = '1') then
      if (BufferWrite = '1') then
        mybuffer(conv_integer(addresswrite)) <= inColor;
      end if;
      temp <= mybuffer(conv_integer(addressread));
    end if;

  end process;

end architecture BEHAVIORAL;
