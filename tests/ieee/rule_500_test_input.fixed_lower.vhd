
entity FIFO is

  generic (
    G_GEN1 : std_logic;
    G_GEN2 : std_logic_vector(3 downto 0);
    G_GEN3 : integer;
    G_GEN4 : signed(15 downto 0);
    G_GEN5 : unsigned(7 downto 0)
  );
  port (
    I_PORT1 : in integer;
    I_PORT2 : in std_logic;
    I_PORTA : in t_user2;
    I_PORT3 : in std_logic_vector(3 downto 0);
    I_PORT4 : in signed(15 downto 0);
    I_PORT5 : in unsigned(7 downto 0);
    I_PORT6 : in std_ulogic;
    I_PORT7 : in t_user1
  );

end entity FIFO;

architecture rtl of fifo is

  signal my_sig : std_logic;
  constant my_con : std_logic_vector(3 downto 0);

  procedure my_proc (
    init : in std_logic
  ) is
    variable my_sig : std_logic;
    constant my_con : std_logic_vector(3 downto 0);
  begin
  end procedure;

  component MY_COMP is
    generic (
      G_GEN1 : std_logic;
      G_GEN2 : std_logic_vector(3 downto 0);
      G_GEN3 : integer;
      G_GEN4 : signed(15 downto 0);
      G_GEN5 : unsigned(7 downto 0)
    );
    port (
      I_PORT1 : in integer;
      I_PORT2 : in std_logic;
      I_PORTA : in t_user2;
      I_PORT3 : in std_logic_vector(3 downto 0);
      I_PORT4 : in signed(15 downto 0);
      I_PORT5 : in unsigned(7 downto 0);
      I_PORT6 : in std_ulogic;
      I_PORT7 : in t_user1
    );
  end component;

begin

end architecture rtl;

--====== UPPERCASE before

entity FIFO is

  generic (
    G_GEN1 : std_logic;
    G_GEN2 : std_logic_vector(3 downto 0);
    G_GEN3 : integer;
    G_GEN4 : signed(15 downto 0);
    G_GEN5 : unsigned(7 downto 0)
  );
  port (
    I_PORT1 : in integer;
    I_PORT2 : in std_logic;
    I_PORTA : in t_user2;
    I_PORT3 : in std_logic_vector(3 downto 0);
    I_PORT4 : in signed(15 downto 0);
    I_PORT5 : in unsigned(7 downto 0);
    I_PORT6 : in std_ulogic;
    I_PORT7 : in t_user1
  );

end entity FIFO;

architecture rtl of fifo is

  signal my_sig : std_logic;
  constant my_con : std_logic_vector(3 downto 0);

  procedure my_proc (
    init : in std_logic
  ) is
    variable my_sig : std_logic;
    constant my_con : std_logic_vector(3 downto 0);
  begin
  end procedure;

  component MY_COMP is
    generic (
      G_GEN1 : std_logic;
      G_GEN2 : std_logic_vector(3 downto 0);
      G_GEN3 : integer;
      G_GEN4 : signed(15 downto 0);
      G_GEN5 : unsigned(7 downto 0)
    );
    port (
      I_PORT1 : in integer;
      I_PORT2 : in std_logic;
      I_PORTA : in t_user2;
      I_PORT3 : in std_logic_vector(3 downto 0);
      I_PORT4 : in signed(15 downto 0);
      I_PORT5 : in unsigned(7 downto 0);
      I_PORT6 : in std_ulogic;
      I_PORT7 : in t_user1
    );
  end component;

begin

end architecture rtl;
