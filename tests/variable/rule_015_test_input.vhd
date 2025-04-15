
architecture ARCH of ENTITY is
begin

process

  variable var1, var2, var3 : std_logic;

  shared variable var4, var5, var6 : std_logic;

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
  variable foo, bar, mine : std_logic_vector(maximum(G_A, G_B) + maximum(C_A, C_B)-1 downto 0);

  variable  ar,ai,ar3,ai3:    STD_LOGIC_VECTOR (width-1 downto 0);
  variable  br1,bi1,br,bi,br2,bi2:    STD_LOGIC_VECTOR (width-1 downto 0);

  shared variable cr,ci,cr3,ci3:    STD_LOGIC_VECTOR (width-1 downto 0);

begin
end process;

end architecture ARCH;
