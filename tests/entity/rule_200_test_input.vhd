
entity FIFO is
  generic (
    G_WIDTH : integer := 256;
    G_DEPTH : integer := 32
  );
end entity FIFO;

package my_pkg is

  generic (
    G_WIDTH : integer := 256;
    G_DEPTH : integer := 32
  );

end package my_pkg;

-- Violation below

entity FIFO is



  generic (
    G_WIDTH : integer := 256;
    G_DEPTH : integer := 32
  );
end entity FIFO;
