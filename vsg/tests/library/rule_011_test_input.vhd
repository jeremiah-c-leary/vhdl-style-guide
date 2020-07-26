
-- This should pass
library ieee;
  use ieee.std_logic_1164.all;

--- this should fail
library ieee; use ieee.std_logic_1164; library analog; use analog.all; library digital; use digital.gates.and;

library ieee; use ieee.std_logic_1164; library analog; use
analog.all; use
analog.all;
