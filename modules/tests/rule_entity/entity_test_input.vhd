

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
end ENTITY1


 entITy   entiTY2  IS
  generic (
    G_GENERIC1 : std_logic := '0';
    G_GENERIC2 : std_logic := '1'
  );

  PORt   (
    i_port1 : in  std_logic;
  o_port2 :  out   std_logic;
    io_port3 : inout       std_logic;
      PORT4 :in std_logic;
    PORT5 :  out std_logic;
    PORT6 : inout std_logic  );

   end     entiTY2
    eNTITY   entiTY3    is
  generic (
    G_GENERIC1 : std_logic := '0';
    G_GENERIC2 : std_logic := '1'
  );
   PORt (
    i_port1 :   in      std_logic;
    o_port2 : out      std_logic;
    io_port3 :  inout std_logic;
      PORT4 : in std_logic;
    PORT5 :    out std_logic;
     PORT6 : inout     std_logic
 );
 END entiTY3

entity ENTITY1
is
  generic (
    G_GENERIC1 : std_logic := '0';
    G_GENERIC2 : std_logic := '1'
  );

port  (
  I_PORT1 : in        std_logic;
    O_PORT2 :out   std_logic;
IO_PORT3 : inout   std_logic;
    port4 :   in  std_logic;
        port5 : out std_logic;
    port6 : inout  std_logic);
End  ENTITY1

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
end ENTITY1
