
entity FIFO is
  generic (
    G_WIDTH : integer := 256;
    G_DEPTH : integer := 32
  );
end entity FIFO;


-- Violation below

entity FIFO is
  generic (
    W_WIDTH : integer := 256;
    DEPTH : integer := 32
  );
end entity FIFO;

