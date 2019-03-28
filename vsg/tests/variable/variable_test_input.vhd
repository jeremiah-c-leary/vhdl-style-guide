

architecture ARCH of ENTITY is

  variable a_sig : std_logic_vector(31 downto 0);
   variable a_SIg :  std_logic_vector(31 downto 0);
  Variable b_sig: std_logic_vector(31 downto 0);
 variable  b_sig : std_logic_vector(31 downto 0);
  variable  siG : std_logic_vector(31 downto 0);
  variable d_sig :std_logic_vector(31 downto 0);
  varIAble e_sig: std_logic_vector(31 downto 0) := "0";
  variable   SIg : STD_LOGIC_VECTOR(31 downto 0);
  variabLE sig :   std_logic_vector(GENERIC_1 downto 0);
  variable sig :std_logic_vector(31 downto 0);
     variable sIg : std_logic_vector(31 downto 0);
  variable sig :   std_logic_vector(31 downto 0) := (others => '0');

  variable e_sig1, d_sig2 : STD_LOGIC;
  variable a_sig1, c_sig2: std_logic;
  variable b_sig1, b_sig2 :std_logic;
  variable c_sig1, a_sig2:std_logic;

begin

  PROC_1 : process (A) is

    variable p1_variable_1 : std_logic;
    variable p1_variable_10 : integer;
    variable p1_variable_long_10 : real;

  begin

  end process PROC_1;

  PROC_2 : process(B) is

    variable p1_var_1       : std_logic;
    variable p1_var_10      : integer;
    variable p1_var_long_10 : real;

  begin

  end process PROC_2;

  PROC_3 : process(C) is

    variable process1_variable_1 : std_logic;
    variable process1_variable_10 : integer;
    variable process1_variable_long_10 : real;

  begin

  end process PROC_3;

  PROC_4 : process(C) is
 
    variable clk_cnt : integer range SPI_2X_CLK_DIV - 1 downto 0;

  begin

  end process PROC_4;

end architecture ARCH;
