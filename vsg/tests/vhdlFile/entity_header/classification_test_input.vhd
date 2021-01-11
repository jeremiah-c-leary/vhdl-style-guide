
entity FIFO is

  generic (
    A : std_logic := 0;
    B, C : std_logic := '0';
    D : integer
  );
  port (
    A : in std_logic;
    B : out std_logic;
    C : inout std_logic;
    X, Y, Z : buffer integer
  );

end entity FIFO;

entity FIFO is

  generic (
    A : std_logic := 0;
    B, C : std_logic := '0';
    D : integer
  );

end entity FIFO;

entity FIFO is

  port (
    A : in std_logic;
    B : out std_logic;
    C : inout std_logic;
    X, Y, Z : buffer integer
  );

end entity FIFO;

entity FIFO is


end entity FIFO;

