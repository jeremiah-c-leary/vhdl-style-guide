

architecture ARCH of ENTITY is

  signal sig1, sig2, sig3,
     sig4, sig5, sig6 : std_logic;

  signal siga, sigb,
     sigc,
     sigd,
     sige,
     sigf
     : std_logic; -- This is a comment


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
  signal foo, bar, mine : std_logic_vector(maximum(G_A, G_B) + maximum(C_A, C_B)-1 downto 0);

  signal  ar,ai,ar3,ai3:    STD_LOGIC_VECTOR (width-1 downto 0);
  signal  br1,bi1,br,bi,br2,bi2:    STD_LOGIC_VECTOR (width-1 downto 0);

begin

end architecture ARCH;

