
entity FIFO is
  generic (
    WIDTH_G : integer := 256;
    DEPTH_G : integer := 32
  );
end entity FIFO;


-- Violation below

entity FIFO is
  generic (
    WIDTH_W : integer := 256;
    DEPTH : integer := 32
  );
end entity FIFO;

