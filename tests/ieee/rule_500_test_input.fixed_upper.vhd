
entity FIFO is

  generic (
    G_GEN1 : STD_LOGIC;
    G_GEN2 : STD_LOGIC_VECTOR(3 downto 0);
    G_GEN3 : INTEGER;
    G_GEN4 : SIGNED(15 downto 0);
    G_GEN5 : UNSIGNED(7 downto 0)
  );
  port (
    I_PORT1 : in INTEGER;
    I_PORT2 : in STD_LOGIC;
    I_PORTA : in t_user2;
    I_PORT3 : in STD_LOGIC_VECTOR(3 downto 0);
    I_PORT4 : in SIGNED(15 downto 0);
    I_PORT5 : in UNSIGNED(7 downto 0);
    I_PORT6 : in STD_ULOGIC;
    I_PORT7 : in t_user1
  );

end entity FIFO;

architecture rtl of fifo is

  signal my_sig : STD_LOGIC;
  constant my_con : STD_LOGIC_VECTOR(3 downto 0);

  procedure my_proc (
    init : in STD_LOGIC
  ) is
    variable my_sig : STD_LOGIC;
    constant my_con : STD_LOGIC_VECTOR(3 downto 0);
  begin
  end procedure;

  component MY_COMP is
    generic (
      G_GEN1 : STD_LOGIC;
      G_GEN2 : STD_LOGIC_VECTOR(3 downto 0);
      G_GEN3 : INTEGER;
      G_GEN4 : SIGNED(15 downto 0);
      G_GEN5 : UNSIGNED(7 downto 0)
    );
    port (
      I_PORT1 : in INTEGER;
      I_PORT2 : in STD_LOGIC;
      I_PORTA : in t_user2;
      I_PORT3 : in STD_LOGIC_VECTOR(3 downto 0);
      I_PORT4 : in SIGNED(15 downto 0);
      I_PORT5 : in UNSIGNED(7 downto 0);
      I_PORT6 : in STD_ULOGIC;
      I_PORT7 : in t_user1
    );
  end component;

begin

end architecture rtl;

--====== UPPERCASE before

entity FIFO is

  generic (
    G_GEN1 : STD_LOGIC;
    G_GEN2 : STD_LOGIC_VECTOR(3 downto 0);
    G_GEN3 : INTEGER;
    G_GEN4 : SIGNED(15 downto 0);
    G_GEN5 : UNSIGNED(7 downto 0)
  );
  port (
    I_PORT1 : in INTEGER;
    I_PORT2 : in STD_LOGIC;
    I_PORTA : in t_user2;
    I_PORT3 : in STD_LOGIC_VECTOR(3 downto 0);
    I_PORT4 : in SIGNED(15 downto 0);
    I_PORT5 : in UNSIGNED(7 downto 0);
    I_PORT6 : in STD_ULOGIC;
    I_PORT7 : in t_user1
  );

end entity FIFO;

architecture rtl of fifo is

  signal my_sig : STD_LOGIC;
  constant my_con : STD_LOGIC_VECTOR(3 downto 0);

  procedure my_proc (
    init : in STD_LOGIC
  ) is
    variable my_sig : STD_LOGIC;
    constant my_con : STD_LOGIC_VECTOR(3 downto 0);
  begin
  end procedure;

  component MY_COMP is
    generic (
      G_GEN1 : STD_LOGIC;
      G_GEN2 : STD_LOGIC_VECTOR(3 downto 0);
      G_GEN3 : INTEGER;
      G_GEN4 : SIGNED(15 downto 0);
      G_GEN5 : UNSIGNED(7 downto 0)
    );
    port (
      I_PORT1 : in INTEGER;
      I_PORT2 : in STD_LOGIC;
      I_PORTA : in t_user2;
      I_PORT3 : in STD_LOGIC_VECTOR(3 downto 0);
      I_PORT4 : in SIGNED(15 downto 0);
      I_PORT5 : in UNSIGNED(7 downto 0);
      I_PORT6 : in STD_ULOGIC;
      I_PORT7 : in t_user1
    );
  end component;

begin

end architecture rtl;
