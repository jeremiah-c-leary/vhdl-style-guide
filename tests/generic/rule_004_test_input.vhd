
entity FIFO is
  generic (
    G_WIDTH : integer := 256;
    G_DEPTH : integer := 32
  );
end entity FIFO;


-- Violation below

entity FIFO is
  generic(
   G_WIDTH : integer := 256;
   G_DEPTH : integer := 32
  );
end entity FIFO;

entity FIFO is
  generic      (
      G_WIDTH : integer := 256;
      G_DEPTH : integer := 32
  );
end entity FIFO;

entity FIFO is
  generic  (
G_WIDTH : integer := 256;
                 G_DEPTH : integer := 32
  );
end entity FIFO;

