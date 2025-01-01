
package body RTL is

  -- These should pass
  variable v_var1   : std_logic;
  constant c_cons1  : std_logic;
  file     f_fil1   : load_file_type open read_mode is load_file_name;
  type     t_typ1   is (idle, write, read);
  subtype  s_sub1   is integer range 0 to 9;
  alias    a_alias1 is name;
  alias    a_alias2 : subtype_indictor is name;

  -- These should fail
  variable v_var1   : std_logic;
  constant c_cons1  : std_logic;
  file     f_fil1   : load_file_type open read_mode is load_file_name;
  type     t_typ1 is (idle, write, read);
  subtype  s_sub1 is integer range 0 to 9;
  alias    a_alias1 is name;
  alias    a_alias2 : subtype_indictor is name;

  -- Checking exclusions
  constant c_abc : integer;
  function my_func return integer is
    constant c_abc : integer;
  begin
  end function;
  constant c_abc : integer;
  type flag_pt is protected body
    variable flag : boolean;
  end protected body;

end package body RTL;
