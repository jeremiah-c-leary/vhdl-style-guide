
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

entity b is
  generic (
    type DATA_TYPE;
    function foo (
      a : natural;
      b : DATA_TYPE
    ) return natural;
    impure function bar (
      a          : integer;
      b          : integer;
      constant c : integer
    ) return natural;
    procedure baz (
      c        : boolean;
      signal d : in std_logic
    );
    val : natural := 0;
    val2 : natural := 0
  );
end entity b;
