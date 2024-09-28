
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
    I_PORTA : in T_USER2;
    I_PORT3 : in STD_LOGIC_VECTOR(3 downto 0);
    I_PORT4 : in SIGNED(15 downto 0);
    I_PORT5 : in UNSIGNED(7 downto 0);
    I_PORT6 : in STD_ULOGIC;
    I_PORT7 : in T_USER1
  );

end entity FIFO;

architecture rtl of fifo is

  type my_type is range 10 to 100;

  subtype my_subtype   is MY_TYPE range 10 to 20;
  subtype my_subtype_t is MY_EXTERNAL_TYPE range 10 to 20;
  subtype my_int       is INTEGER range 10 to 100;
  subtype my_nat       is NATURAL range 10 to 100;
  subtype my_pos       is POSITIVE range 10 to 100;
  subtype my_char      is CHARACTER range 'a' downto 'b';

  signal s_my_subtype   : MY_EXTERNAL_SUBTYPE;
  signal s_my_subtype   : MY_SUBTYPE;
  signal s_my_subtype_t : MY_SUBTYPE_T;
  signal s_my_int       : MY_INT;
  signal s_my_nat       : MY_NAT;
  signal s_my_pos       : MY_POS;
  signal s_my_char      : MY_CHAR;
  signal s_my_type_t    : MY_TYPE_T;
  signal s_int          : INTEGER;
  signal s_nat          : NATURAL;
  signal s_pos          : POSITIVE;
  signal s_char         : CHARACTER;

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
      I_PORTA : in T_USER2;
      I_PORT3 : in STD_LOGIC_VECTOR(3 downto 0);
      I_PORT4 : in SIGNED(15 downto 0);
      I_PORT5 : in UNSIGNED(7 downto 0);
      I_PORT6 : in STD_ULOGIC;
      I_PORT7 : in T_USER1
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
    I_PORTA : in T_USER2;
    I_PORT3 : in STD_LOGIC_VECTOR(3 downto 0);
    I_PORT4 : in SIGNED(15 downto 0);
    I_PORT5 : in UNSIGNED(7 downto 0);
    I_PORT6 : in STD_ULOGIC;
    I_PORT7 : in T_USER1
  );

end entity FIFO;

architecture rtl of fifo is

  type MY_TYPE is range 10 to 100;

  subtype MY_SUBTYPE   is MY_TYPE range 10 to 20;
  subtype MY_SUBTYPE_T is MY_EXTERNAL_TYPE range 10 to 20;
  subtype MY_INT       is INTEGER range 10 to 100;
  subtype MY_NAT       is NATURAL range 10 to 100;
  subtype MY_POS       is POSITIVE range 10 to 100;
  subtype MY_CHAR      is CHARACTER range 'a' downto 'b';

  signal S_MY_SUBTYPE   : MY_EXTERNAL_SUBTYPE;
  signal S_MY_SUBTYPE   : MY_SUBTYPE;
  signal S_MY_SUBTYPE_T : MY_SUBTYPE_T;
  signal S_MY_INT       : MY_INT;
  signal S_MY_NAT       : MY_NAT;
  signal S_MY_POS       : MY_POS;
  signal S_MY_CHAR      : MY_CHAR;
  signal S_MY_TYPE_T    : MY_TYPE_T;
  signal S_INT          : INTEGER;
  signal S_NAT          : NATURAL;
  signal S_POS          : POSITIVE;
  signal S_CHAR         : CHARACTER;

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
      I_PORTA : in T_USER2;
      I_PORT3 : in STD_LOGIC_VECTOR(3 downto 0);
      I_PORT4 : in SIGNED(15 downto 0);
      I_PORT5 : in UNSIGNED(7 downto 0);
      I_PORT6 : in STD_ULOGIC;
      I_PORT7 : in T_USER1
    );
  end component;

begin

end architecture rtl;
