

var_test : process is

  variable sig1 : std_logic;
variable sig2 : std_logic;
variable sig3 : std_logic;
variable sig4 : std_logic;
variable sig5 : std_logic;
variable sig6 : std_logic;

  variable siga     : std_logic;
variable sigb     : std_logic;
variable sigc     : std_logic;
variable sigd     : std_logic;
variable sige     : std_logic;
variable sigf     : std_logic; -- This is a comment


  -- Test variations of a single variable declaration

  variable sig1 : std_logic;

  variable sig1 : std_logic
    ;

  variable sig1 :
    std_logic
    ;

  variable sig1
    :
    std_logic
    ;

  variable
    sig1
    :
    std_logic
    ;

  -- Test variations of a two variable declarations

  variable sig1, sig2 : std_logic;

  variable sig1, sig2 : std_logic
    ;

  variable sig1, sig2 :
    std_logic
    ;

  variable sig1, sig2
    :
    std_logic
    ;

  variable sig1,
    sig2
    :
    std_logic
    ;

  variable sig1
    ,
    sig2
    :
    std_logic
    ;

  variable
    sig1
    ,
    sig2
    :
    std_logic
    ;

  variable sig1, sig2 : std_logic; -- Comma, should not induce a failure

  -- This should pass
  variable foo : std_logic_vector(maximum(G_A, G_B) + maximum(C_A, C_B)-1 downto 0);
  variable foo : std_logic_vector(maximum(G_A, G_B) + maximum(C_A, C_B)-1 downto 0);
variable bar : std_logic_vector(maximum(G_A, G_B) + maximum(C_A, C_B)-1 downto 0);
variable mine : std_logic_vector(maximum(G_A, G_B) + maximum(C_A, C_B)-1 downto 0);

  variable  ar:    STD_LOGIC_VECTOR (width-1 downto 0);
variable  ai:    STD_LOGIC_VECTOR (width-1 downto 0);
variable  ar3:    STD_LOGIC_VECTOR (width-1 downto 0);
variable  ai3:    STD_LOGIC_VECTOR (width-1 downto 0);
  variable  br1:    STD_LOGIC_VECTOR (width-1 downto 0);
variable  bi1:    STD_LOGIC_VECTOR (width-1 downto 0);
variable  br:    STD_LOGIC_VECTOR (width-1 downto 0);
variable  bi:    STD_LOGIC_VECTOR (width-1 downto 0);
variable  br2:    STD_LOGIC_VECTOR (width-1 downto 0);
variable  bi2:    STD_LOGIC_VECTOR (width-1 downto 0);

begin

end process var_test;
