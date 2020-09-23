
architecture RTL of FIFO is begin end architecture RTL;

-- This should fail
architecture RTL of FIFO is
  signal a : std_logic;

begin end architecture RTL;

-- This should fail
architecture RTL of FIFO is -- Comment
  signal a : std_logic;

begin end architecture RTL;

-- This should fail
architecture RTL of FIFO is-- Comment
  signal a : std_logic;

begin end architecture RTL;

-- This should not fail
architecture RTL of FIFO is
  signal a : std_logic;

begin end architecture RTL;
