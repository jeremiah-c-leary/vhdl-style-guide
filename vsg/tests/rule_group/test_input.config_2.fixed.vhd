
library ieee;
  use ieee.std_logic_1164.all;

entity BLAH is
  generic (
    G_BLAH : std_logic
  );
  port (
    I_INPUT  : in    std_logic;
    O_OUTPUT : out   std_logic;
    IO_INOUT : inout std_logic
  );
end entity BLAH;

architecture RTL of BLAH is

  constant CON_A : STD_LOGIC;
  signal   SIG_A : std_logic;

begin

end architecture RTL;

package SOME_PKG is

end package SOME_PKG;

package body SOME_PKG_BODY is

end package body SOME_PKG_BODY;
