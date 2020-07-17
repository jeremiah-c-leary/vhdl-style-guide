
architecture RTL of ENTITY1 is

begin

  PROC : process (a) is
    -- These should fail
    variable v_var1 : std_logic;
    signal s_sig1 : std_logic;
    constant c_cons1 : std_logic;
    file f_fil1 : load_file_type open read_mode is load_file_name;
    type t_typ1 is (idle, write, read);
    subtype s_sub1 is range 0 to 9;
  begin
  end process PROC;

  PROC : process (a) is
    -- These should pass
    variable v_var1 : std_logic;
    signal   s_sig1 : std_logic;
    constant c_cons1 : std_logic;
    file     f_fil1 : load_file_type open read_mode is load_file_name;
    type     t_typ1 is (idle, write, read);
    subtype  s_sub1 is range 0 to 9;
  begin
  end process PROC;

  PROC : process (a) is
    -- Test with different spacing
    variable  v_var1 : std_logic;
    signal   s_sig1 : std_logic;
    constant    c_cons1 : std_logic;
    file    f_fil1 : load_file_type open read_mode is load_file_name;
    type     t_typ1 is (idle, write, read);
    subtype   s_sub1 is range 0 to 9;
  begin
  end process PROC;

  PROC : process (a) is
    -- Test with shorter combinations
    signal s_sig1 : std_logic;
    file   f_fil1 : load_file_type open read_mode is load_file_name;
    type   t_typ1 is (idle, write, read);
  begin
  end process PROC;

  PROC : process (a) is
    -- Test with comments
    variable v_var1 : std_logic;
    signal   s_sig1 : std_logic;
    -- some comment
    constant c_cons1 : std_logic;
    file     f_fil1 : load_file_type open read_mode is load_file_name;
    -- some comment
    type    t_typ1 is (idle, write, read);
    subtype s_sub1 is range 0 to 9;
  begin
  end process PROC;

  PROC : process (a) is
    -- Test multiline declarations
    type state_type is (
      state1, state2,
      state3, state4
    );
    signal sig1 : std_logic;
  
    -- This should not error
    type state_type2 is (
      state1, state2,
      state3, state4
    );
  
    signal sig1 : std_logic;
  begin
  end process PROC;

  -- Test functions and procedures in the process declarative region

  PROC : process (a) is

    signal sig1 : std_logic;
    variable var1 : std_logic;
    constant con1 : integer := 0;
    file fil1 : something;

    function func_1 (
      constant a : integer;
      signal b : integer;
      signal c : unsigned(3 downto 0);
      signal d : std_logic_vector(7 downto 0);
      constant e : std_logic) return integer is
      file file1 : load_file_type open read_mode is load_file_name;
      constant con1 : integer := 0;
      signal sig1 : std_logic_vector;
    begin
  
    end;

      signal     sig1 : std_logic;
      file fil1 : something;

    procedure AVERAGE_SAMPLES (
      constant a : in integer;
      signal b : in std_logic;
      variable c : in std_logic_vector(3 downto 0);
      signal d : out std_logic) is
      signal sig1 : std_logic;
      file file1 : something;
      variable var1 : integer;
    begin
    end procedure AVERAGE_SAMPLES;  

     signal sig1 : std_logic;
     file fil1 : something;
  begin
  end process PROC;

end architecture RTL;
