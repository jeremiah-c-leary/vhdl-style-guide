
architecture RTL of ENTITY1 is

  -- These should fail
  variable v_var1 : std_logic;
  signal s_sig1 : std_logic;
  constant c_cons1 : std_logic;
  file f_fil1 : load_file_type open read_mode is load_file_name;
  type t_typ1 is (idle, write, read);
  subtype s_sub1 is range 0 to 9;

  -- These should pass
  variable v_var1 : std_logic;
  signal   s_sig1 : std_logic;
  constant c_cons1 : std_logic;
  file     f_fil1 : load_file_type open read_mode is load_file_name;
  type     t_typ1 is (idle, write, read);
  subtype  s_sub1 is range 0 to 9;

  -- Test with different spacing
  variable  v_var1 : std_logic;
  signal   s_sig1 : std_logic;
  constant    c_cons1 : std_logic;
  file    f_fil1 : load_file_type open read_mode is load_file_name;
  type     t_typ1 is (idle, write, read);
  subtype   s_sub1 is range 0 to 9;

  -- Test with shorter combinations
  signal s_sig1 : std_logic;
  file   f_fil1 : load_file_type open read_mode is load_file_name;
  type   t_typ1 is (idle, write, read);

  -- Test with comments
  variable v_var1 : std_logic;
  signal   s_sig1 : std_logic;
  -- some comment
  constant c_cons1 : std_logic;
  file     f_fil1 : load_file_type open read_mode is load_file_name;
  -- some comment
  type    t_typ1 is (idle, write, read);
  subtype s_sub1 is range 0 to 9;

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

end architecture RTL;
