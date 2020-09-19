

entity ENTITY1 is
  generic (
    G_GENERIC1 : std_logic := '0';G_GENERIC2 : std_logic := '1';G_GENERIC3 : std_logic := '1';G_GENERIC4 : std_logic := '1';G_GENERIC5 : std_logic := '1'
  );
  port (
    I_PORT1 : in    std_logic;
    O_PORT2 : out   std_logic;
    IO_PORT3 : inout std_logic;
    port4 : in std_logic;
    port5 : out std_logic;
    port6 : inout std_logic
  );
end entity ENTITY1;

entity ENTITY1 is
  generic (
    G_GENERIC1 : std_logic := '0';
    G_GENERIC2 : std_logic := '1'
  );
  port (
    I_PORT1 : in    std_logic;
    O_PORT2 : out   std_logic;
    IO_PORT3 : inout std_logic;
    port4 : in std_logic;
    port5 : out std_logic;
    port6 : inout std_logic
  );
end entity ENTITY1;
