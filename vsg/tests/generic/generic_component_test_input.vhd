
architecture RTL of ENTITY is

  component ENTITY1 is
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
  end component ENTITY1;

  component ENTITY1 is
    generic (
      G_GENERIC1 : std_logic;
      G_GENERIC2 : std_logic
    );
    port (
      I_PORT1 : in    std_logic;
      O_PORT2 : out   std_logic;
      IO_PORT3 : inout std_logic;
      port4 : in std_logic;
      port5 : out std_logic;
      port6 : inout std_logic
    );
  end component ENTITY1;

  component ENTITY1 is
    generic (
      G_GENERIC1 : std_logic :=  '0';
      G_GENERIC2 : std_logic :=   '1'
    );
    port (
      I_PORT1 : in    std_logic;
      O_PORT2 : out   std_logic;
      IO_PORT3 : inout std_logic;
      port4 : in std_logic;
      port5 : out std_logic;
      port6 : inout std_logic
    );
  end component ENTITY1;

begin

end architecture RTL;
