
-- vsg_off library_008 process_012
library ieee;
use ieee.std_logic_arith.all;
-- vsg_on library_008 process_012

library ieee;
  use ieee.std_logic.all;

-- vsg_off : comment
entity FIFO is
  port (
    WRITE_EN : in std_logic;
    READ_EN  : in std_logic
  );
end entity;
-- vsg_on : comment

-- vsg_off library_002 : comment
library  ieee;
-- vsg_on library_002 : comment
library  ieee;
-- vsg_off : comment
library  ieee;
-- vsg_on : comment
library  ieee;

-- vsg_off library_001 process_001


-- vsg_on library_001


-- vsg_off case_001

-- vsg_on  process_001

-- vsg_off library_001

-- vsg_on case_001 library_001

architecture rtl of fifo is

begin

-- vsg_off comment_010
-- Comment
-- Comment
-- vsg_on comment_010

  a <= b;

end architecture rtl;

-- vsg_off

architecture rtl of fifo is

  constant CONST : t_rec_vector :=
  (
    (val1 => 1, val2 => 2), -- Despite the tag vsg_off, VSG reports missing carriage return here
    (val1 => 3, val2 => 4), -- Despite the tag vsg_off, VSG reports missing carriage return here
    (val1 => 5, val2 => 6)  -- Despite the tag vsg_off, VSG reports missing carriage return here
  );
-- vsg_on

begin

  -- vsg_off length_003 length_001 : comment

  p_length_003_passing : process is
  begin

    a <= b;
    a <= b;
    a <= b;

  end process p_length_003;

  -- vsg_on length_003

  p_length_003_failing : process is
  begin

    a <= b;
    a <= b;
    a <= b;

  end process p_length_003;

end architecture rtl;

-- vsg_on comment_010
