
entity FIFO is
  generic (
    G_WIDTH : integer := 256;  -- Comment
    G_DEPTH : integer := 32    -- Comment
  );
end entity FIFO;


-- Violation below

entity FIFO is
  generic(g_size: integer := 10;g_width    : integer := 256;g_depth: integer := 32
  );
  port(
   i_port1 : in std_logic;i_port2 : in std_logic
  );  
end entity FIFO;


