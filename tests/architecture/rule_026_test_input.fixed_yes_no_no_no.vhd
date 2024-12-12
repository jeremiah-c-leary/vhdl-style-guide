
architecture RTL of FIFO is

  constant c_a             : integer;
  signal sig_b             : std_logic;
  shared variable var_1    : integer;
  file file1               : integer;
  alias alias1             is name;
  alias alias1             : subtype_identifier is name;
  type state_machine is (idle, write, read, done);
  -- Comment to break up groups
  constant c_ab            : integer;
  signal sig_bc            : std_logic;
  shared variable var_12   : integer;
  file file12              : integer;

  constant c_abc           : integer;
  signal sig_bcd           : std_logic;
  shared variable var_123  : integer;
  file file123             : integer;
  -- Comment to break up groups
  constant c_abcd          : integer;
  signal sig_bcde          : std_logic;
  shared variable var_1234 : integer;
  file file1234            : integer;

  -- Checking exclusions
  constant c_abc           : integer;
  function my_func return integer is
    constant c_abc : integer;
  begin
  end function;
  constant c_abc           : integer;
  type flag_pt is protected body
    variable flag  : boolean;
  end protected body;

begin

end architecture RTL;
