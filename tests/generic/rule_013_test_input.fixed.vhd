
entity FIFO is
  generic (
    G_WIDTH : integer := 256;
    G_DEPTH : integer := 32
  );
end entity FIFO;


-- Violation below

entity FIFO is
  GENERIC(
g_size : integer := 10;
   g_width : integer := 256;
   g_depth : integer := 32
  );
end entity FIFO;
