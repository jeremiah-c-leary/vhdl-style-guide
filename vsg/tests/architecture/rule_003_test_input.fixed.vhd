
architecture RTL of FIFO is begin end architecture RTL;

-- This should not fail
architecture RTL of FIFO is begin end architecture RTL;

-- This should fail
library ieee;

architecture RTL of FIFO is begin end architecture RTL;

-- This should not fail
library ieee;

architecture RTL of FIFO is begin end architecture RTL;
