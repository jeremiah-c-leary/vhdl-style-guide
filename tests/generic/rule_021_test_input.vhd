
entity FIFO is
  generic (
    G_WIDTH : integer := 256;
    G_DEPTH : integer := 32  -- Comment
  );
  port (
    I_PORT1 : in std_logic;
    I_PORT2 : out std_logic
  );
end entity FIFO;


-- Violation below

entity FIFO is
  GENERIC(g_size : integer := 10;
   g_width : integer := 256;
   g_depth : integer := 32)  -- Comment should stay
  ;
  PORT (
    i_port1 : in std_logic := '0';
    i_port2 : out std_logic :='1');
end entity FIFO;
