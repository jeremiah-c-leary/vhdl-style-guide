-- This should be okay

architecture rtl of fifo is

 -- Comment
  signal a : std_logic;

  -- Okay comment
  signal b : std_logic_vector;

begin

 -- Comment 1
  a <= b;
 -- Comment 2
  c <= d;
 -- Comment 3
  e <= f;

end architecture rtl;
