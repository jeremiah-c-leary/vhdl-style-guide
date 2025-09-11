
--! Comment 1

library ieee;
  --! Comment 1.5
  use ieee.std_logic_1164.all;
--! Comment 2

library ieee;
  --! Comment 2.5
  use ieee.std_logic_1164.all;
  --! Comment 3

  --! Comment 3.5
  use ieee.std_logic_1164.all;
--! Comment 4

--! Comment 5

architecture RTL of FIFO is

begin

  SOME_LABEL : case D_DEPTH generate

    -- When comment
    -- When comment
    when 0 =>

      -- Comment 10
      b <= 0;

    -- When Comment 2
    -- When Comment 2
    when 1 =>

  end generate SOME_LABEL;

end architecture RTL;
