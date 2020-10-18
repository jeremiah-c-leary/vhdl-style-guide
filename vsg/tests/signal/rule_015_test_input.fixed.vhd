

architecture ARCH of ENTITY is

  signal sig1 : std_logic;
signal sig2 : std_logic;
signal sig3 : std_logic;
signal sig4 : std_logic;
signal sig5 : std_logic;
signal sig6 : std_logic;

  signal siga : std_logic;
signal sigb : std_logic;
signal sigc : std_logic;
signal sigd : std_logic;
signal sige : std_logic;
signal sigf : std_logic; -- This is a comment


  -- Test variations of a single signal declaration

  signal sig1 : std_logic;

  signal sig1 : std_logic
    ;

  signal sig1 :
    std_logic
    ;

  signal sig1
    :
    std_logic
    ;

  signal
    sig1
    :
    std_logic
    ;

  -- Test variations of a two signal declarations

  signal sig1, sig2 : std_logic;

  signal sig1, sig2 : std_logic
    ;

  signal sig1, sig2 :
    std_logic
    ;

  signal sig1, sig2
    :
    std_logic
    ;

  signal sig1,
    sig2
    :
    std_logic
    ;

  signal sig1
    ,
    sig2
    :
    std_logic
    ;

  signal
    sig1
    ,
    sig2
    :
    std_logic
    ;

  signal sig1, sig2 : std_logic; -- Comma, should not induce a failure

  -- This should pass
  signal foo : std_logic_vector(maximum(G_A, G_B) + maximum(C_A, C_B)-1 downto 0);
  signal foo : std_logic_vector(maximum(G_A, G_B) + maximum(C_A, C_B)-1 downto 0);
signal bar : std_logic_vector(maximum(G_A, G_B) + maximum(C_A, C_B)-1 downto 0);
signal mine : std_logic_vector(maximum(G_A, G_B) + maximum(C_A, C_B)-1 downto 0);

begin

end architecture ARCH;

