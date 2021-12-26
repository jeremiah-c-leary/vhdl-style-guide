
library ieee;
use ieee.std_logic_1164.all;

entity blah is
  generic (
    G_BLAH : std_logic
  );
  port (
    I_INPUT : in std_logic;
    O_OUTPUT : out std_logic;
    IO_INOUT : inout std_logic
  );
end entity blah;

