

entity entity1 is
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
end entity entity1


 entITy   entiTY2  IS
  generic (
       G_GENERIC1 : std_logic :='0';-- Comment
    G_generic2 : std_logic := '1'             -- Comment
  );

  PORt   (
    i_port1 : in  std_logic;           -- Comment
  o_port2 :  out   std_logic;      -- Comment
    io_port3 : inout       std_logic;    -- Comment
      PORT4 :in std_logic;   -- Comment
    PORT5 :  out std_logic;--Comment
    PORT6 : inout std_logic  );--Comment

 end entity    entiTY2
    eNTITY   entiTY3    is
  generic (
    g_generIC1 :std_logic := '0';
    G_GeneRIC2 :std_logic :='1'
  );
   PORt (
    i_port1 :   in      std_logic;
    o_port2 : out      std_logic;
    io_port3 :  inout std_logic;
      PORT4 : in std_logic := '0';
    PORT5 :    out std_logic;
     PORT6 : inout     std_logic
 );
 END ENTITY entiTY3

entity entity1
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
End  entity  entity1

entity entity1 is
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
end ENtity entity1

entity entity1 is

  gENEric  (
      G_GENERIC1 : std_logic :=  '0';
    G_GENERIC2 :   std_logic := '1'
 );
  port (
    I_PORT1 : in    std_logic;
    O_PORT2 : out   std_logic;
    IO_PORT3 : inout std_logic
  );
end   entity entity1


entity entity1 is
  Generic (
    A_GENERIC1 : std_logic := '0';
    G_GENERIC2 : std_logic := '1');
  port (
    PORT1_I : in    std_logic;
    PORT2_O : out   std_logic;
    PORT3_IO : inout std_logic
  );
end ENT1;

architecture RTL of entity1 is

begin
   end architecture  rtl;


-- Check for more than one port assigned on a single line

entity entity1 is
  generic (
    G_GENERIC1 : std_logic := '0';
    A_GENERIC2 : std_logic := '1'
   );
  port (
    I_PORT1, I_PORT4 : in    std_logic;
    O_PORT2 : out   std_logic;
    IO_PORT3, IO_PORT5 : inout std_logic
  );
end entity  entity1

-- Check if no generic is present

entity entity1 is
  port (
    I_PORT1 : in    std_logic;
    O_PORT2 : out   std_logic;
    IO_PORT3 : inout std_logic
  );
end entity;


-- Check proper alignment of :'s does not cause an error

entity entity1 is
  port (
    I_PORT1  : in    std_logic;
    O_PORT2  : out   std_logic;
    IO_PORT3 : inout std_logic
  );


end entity entity1;

-- Check for generics that start with port

entity entity1 is
  generic (
    PORT_1 : std_logic := '0';
    PORT_2 : std_logic := '1'
   );
  port (
    I_PORT1  : in    std_logic;
    O_PORT2  : out   std_logic;
    IO_PORT3 : inout std_logic
  );
end entity entity1;

-- Test for ports with block in the name

entity entity1 is
  port (
    block : in std_logic;
  );
end entity entity1;
