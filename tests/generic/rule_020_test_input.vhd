
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

-- functions passed as a generic
entity b is
  generic (
    type DATA_TYPE;
    function foo (
      a : natural :=0;
      b : DATA_TYPE
    ) return natural;
    impure function bar (
      a          : integer :=1;
      b          : integer :=32;
      constant c : integer
    ) return natural;
    procedure baz (
      c        : boolean;
      signal d : in std_logic
    )
  );
end entity b;
