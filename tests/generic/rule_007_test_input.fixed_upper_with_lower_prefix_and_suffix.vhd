
entity FIFO is
  generic (
    G_WIDTH : integer := 256;
    G_DEPTH : integer := 32;
    prefix_GENERIC_suffix : integer := 20
  );
  port (
    I_PORT1 : in std_logic;
    I_PORT2 : out std_logic
  );
end entity FIFO;

entity FIFO is
  generic (
    G_WIDTH : integer := 256;
    G_DEPTH : integer := 32;
    prefix_GENERIC_suffix : integer := 20
  );
  port (
    I_PORT1 : in std_logic;
    I_PORT2 : out std_logic
  );
end entity FIFO;

entity FIFO is
  generic (
    G_WIDTH : integer := 256;
    G_DEPTH : integer := 32;
    prefix_GENERIC_suffix : integer := 20
  );
  port (
    I_PORT1 : in std_logic;
    I_PORT2 : out std_logic
  );
end entity FIFO;

entity FIFO is
  generic (
    G_WIDTH : integer := 256;
    G_DEPTH : integer := 32;
    prefix_GENERIC_suffix : integer := 20
  );
  port (
    I_PORT1 : in std_logic;
    I_PORT2 : out std_logic
  );
end entity FIFO;

entity FIFO is
  generic(G_SIZE : integer := 10;
   G_WIDTH : integer := 256;
   G_DEPTH : integer := 32;
   prefix_GENERIC_suffix : integer := 20
  );
  port (
    i_port1 : in std_logic := '0';
    i_port2 : out std_logic :='1'
  );
end entity FIFO;

entity FIFO is
  generic(G_SIZE : integer := 10;
   G_WIDTH : integer := 256;
   G_DEPTH : integer := 32;
   prefix_GENERIC_suffix : integer := 20
  );
  port (
    i_port1 : in std_logic := '0';
    i_port2 : out std_logic :='1'
  );
end entity FIFO;

entity FIFO is
  generic(G_SIZE : integer := 10;
   G_WIDTH : integer := 256;
   G_DEPTH : integer := 32;
   prefix_GENERIC_suffix : integer := 20
  );
  port (
    i_port1 : in std_logic := '0';
    i_port2 : out std_logic :='1'
  );
end entity FIFO;

entity FIFO is
  generic(G_SIZE : integer := 10;
   G_WIDTH : integer := 256;
   G_DEPTH : integer := 32;
   prefix_GENERIC_suffix : integer := 20
  );
  port (
    i_port1 : in std_logic := '0';
    i_port2 : out std_logic :='1'
  );
end entity FIFO;

entity FIFO is
  generic(G_SIZE : integer := 10;
   G_WIDTH : integer := 256;
   G_DEPTH : integer := 32;
   prefix_GENERIC : integer := 20
  );
  port (
    i_port1 : in std_logic := '0';
    i_port2 : out std_logic :='1'
  );
end entity FIFO;

entity FIFO is
  generic(G_SIZE : integer := 10;
   G_WIDTH : integer := 256;
   G_DEPTH : integer := 32;
   prefix_GENERIC : integer := 20
  );
  port (
    i_port1 : in std_logic := '0';
    i_port2 : out std_logic :='1'
  );
end entity FIFO;

entity FIFO is
  generic(G_SIZE : integer := 10;
   G_WIDTH : integer := 256;
   G_DEPTH : integer := 32;
   GENERIC_suffix : integer := 20
  );
  port (
    i_port1 : in std_logic := '0';
    i_port2 : out std_logic :='1'
  );
end entity FIFO;

entity FIFO is
  generic(G_SIZE : integer := 10;
   G_WIDTH : integer := 256;
   G_DEPTH : integer := 32;
   GENERIC_suffix : integer := 20
  );
  port (
    i_port1 : in std_logic := '0';
    i_port2 : out std_logic :='1'
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
