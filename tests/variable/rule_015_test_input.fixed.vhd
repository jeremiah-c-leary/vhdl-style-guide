
architecture ARCH of ENTITY is
begin

process

  variable var1 : std_logic;
  variable var2 : std_logic;
  variable var3 : std_logic;

  shared variable var4 : std_logic;
  shared variable var5 : std_logic;
  shared variable var6 : std_logic;

  -- Test variations of a single variable declaration

  variable var1 : std_logic;

  shared variable var1 : std_logic
    ;

  variable var1 :
    std_logic
    ;

  variable var1
    :
    std_logic
    ;

  variable
    var1
    :
    std_logic
    ;

  -- Test variations of a two variable declarations

  variable var1, var2 : std_logic;

  shared variable var1, var2 : std_logic
    ;

  variable var1, var2 :
    std_logic
    ;

  variable var1, var2
    :
    std_logic
    ;

  variable var1,
    var2
    :
    std_logic
    ;

  shared variable var1
    ,
    var2
    :
    std_logic
    ;

  variable
    var1
    ,
    var2
    :
    std_logic
    ;

  variable var1, var2 : std_logic; -- Comma, should not induce a failure

  shared variable var1, var2 : std_logic; -- Comma, should not induce a failure

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

  shared variable cr:    STD_LOGIC_VECTOR (width-1 downto 0);
  shared variable ci:    STD_LOGIC_VECTOR (width-1 downto 0);
  shared variable cr3:    STD_LOGIC_VECTOR (width-1 downto 0);
  shared variable ci3:    STD_LOGIC_VECTOR (width-1 downto 0);

begin
end process;

end architecture ARCH;
