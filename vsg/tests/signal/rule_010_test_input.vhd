
architecture RTL of FIFO is

  signal sig1 : std_logic;
  signal sig2 : std_logic_vector(4 downto 0);
  signal siga : t_user;
  signal sig2 : integer;
  signal sig2 : signed(15 downto 0);
  signal sig2 : unsigned(15 downto 0);
  signal sig2 : natural;
  signal sigb : t_user;
  signal sig2 : std_ulogic(15 downto 0);
  signal sigc : t_user;

  -- Violations below

  signal sig1 : STD_LOGIC;
  signal sig2 : STD_LOGIC_VECTOR(4 downto 0);
  signal siga : T_USER;
  signal sig2 : INTEGER;
  signal sig2 : SIGNED(15 downto 0);
  signal sig2 : UNSIGNED(15 downto 0);
  signal sig2 : NATURAL;
  signal sigb : T_USER;
  signal sig2 : STD_ULOGIC(15 downto 0);
  signal sigc : T_USER;

begin

end architecture RTL;
