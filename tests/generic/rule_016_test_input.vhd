
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

-- functions passed as a generic
entity b is
  generic (
    type DATA_TYPE;
    function foo (
      a : natural :=0; b : DATA_TYPE
    ) return natural;
    impure function bar (
      a          : integer :=1; b          : integer :=32; constant c : integer
    ) return natural;
    procedure baz (
      c        : boolean; signal d : in std_logic
    )
  );
end entity b;
