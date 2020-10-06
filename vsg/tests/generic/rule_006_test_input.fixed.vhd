
entity FIFO is
  generic (
    G_WIDTH : integer := 256;
    G_DEPTH : integer := 32
  );
  port (
    I_PORT1 : in std_logic;
    I_PORT2 : out std_logic
  );
end entity FIFO;


-- Violation below

entity FIFO is
  generic(G_SIZE :  integer := 10;
   G_WIDTH : integer := 256;
   G_DEPTH : integer := 32
  );
  port (
    I_PORT1 : in std_logic :=    '0';
    I_PORT2 : out std_logic :='1'
  );
end entity FIFO;


