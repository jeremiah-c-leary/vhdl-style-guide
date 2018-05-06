

entity ENTITY1 is
  generic (
    G_GENERIC1 : std_logic := '0';
    G_GENERIC2 : std_logic := '1'
  );
  port (
    I_PORT1 : in    std_logic;
    O_PORT2 : out   t_USER_DEFINED_TYPE;
    IO_PORT3 : inout std_logic_vector(1 downto 0);
    use_4 : in integer;
    port5 : out std_logic;
    port6 : inout std_logic
  );
end entity ENTITY1


 entITy   entiTY2  IS
  generic (
       G_GENERIC1 : std_logic :='0';
    G_generic2 : std_logic := '1'
  );

  PORt   (
    i_port1 : in  SIGNED;
  o_port2 :  out   STD_LOGIC;
    io_port3(c_index) : inout       NATURAL;
      PORT4(c_index) :in INTEGER;
    USE_5 :  out STD_LOGIC_VECTOR(G_GENERIC1 downto 0);
    PORT6 : inout UNSIGNED  );

 end entity    entiTY2
    eNTITY   entiTY3    is
  generic (
    g_generIC1 :std_logic := '0';
    G_GeneRIC2 :std_logic :='1'
  );
   PORt (
    i_port1 :   IN      std_logic;
    o_port2 : out      std_logic;
    io_port3 :  inout std_logic;
      PORT4 : iN std_logic := '0';
    PORT5 :    oUt STD_LOGIC;
     PORT6 : inOut     std_logic
 );
 END ENTITY entiTY3

entity ENTITY1
is
   generic  (
    G_GENERIC1 :   std_logic :=   '0';
  G_GENERIC2 : std_logic :=    '1'
  );

port  (
  I_PORT1 : in        std_logic;
    O_PORT2 :out   std_logic := '1';
IO_PORT3 : inout   std_logic;
    port4 :   in  std_logic;
        port5 : out std_logic;
    port6 : inout  std_logic);
End  entity  ENTITY1

entity ENTITY1 is
 geneRIC (
    A_generic1 :std_logic := '0';
   G_GENERIC2 : std_logic :='1'
  );
  port (
    I_PORT1 : in    std_logic;
    O_PORT2 : out   std_logic;
    IO_PORT3 : inout std_logic;
    port4 : in std_logic;
    port5 : out std_logic := '0';
    port6 : inout std_logic
   );
end ENtity ENTITY1

entity ENTITY1 is

  gENEric  (
      G_GENERIC1 : std_logic :=  '0';
    G_GENERIC2 :   std_logic := '1'
 );
  port (
    I_PORT1 : in    std_logic;
    O_PORT2 : out   std_logic;
    IO_PORT3 : inout std_logic
  );
end   entity ENTITY1


entity ENTITY1 is
  Generic (
    A_GENERIC1 : std_logic := '0';
    G_GENERIC2 : std_logic := '1');
  Port (
    PORT1_I : in    std_logic;
    PORT2_O : out   std_logic;
    PORT3_IO : inout std_logic
  );
end ENTITY1

architecture RTL of ENTITY1 is

begin
   end architecture  rtl;


-- Check for more than one port assigned on a single line

entity ENTITY1 is
  generic (
    G_GENERIC1 : std_logic := '0';
    A_GENERIC2 : std_logic := '1'
   );
  port (
    I_PORT1, I_PORT4 : in    std_logic;
    O_PORT2 : out   std_logic;
    IO_PORT3, IO_PORT5 : inout std_logic
  );
end entity  ENTITY1

-- Check if no generic is present

entity ENTITY1 is
  port (
    I_PORT1 : in    std_logic;
    O_PORT2 : out   std_logic;
    IO_PORT3 : inout std_logic
    --- debug ports: can be removed or left unconnected for the application circuit ---
  );
end entity ENTITY1


-- Check if port exists on port keyword line

entity ENTITY1 is
  port (   I_PORT1 : in    std_logic;
    O_PORT_OUT: out   std_logic;
    IO_PORT3 : inout std_logic
    --- debug ports: can be removed or left unconnected for the application circuit ---
  );
end entity ENTITY1

-- Check if port opening parenthesis is on the same line

entity ENTITY1 is
  port
    (
    PORT1 : in    std_logic 
  );
end entity ENTITY1;
