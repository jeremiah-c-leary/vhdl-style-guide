
architecture ARCH of ENTITY_1 is

  constant con2 : integer := 100;
  signal sig2 : integer := 20;

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

  function func_1 (
     constant a : integer;
     signal   b : integer;
     signal   c : unsigned(3 downto 0);
     signal   d : std_logic_vector(7 downto 0);
     constant e : std_logic) return integer is
     file     file1 : load_file_type open read_mode is load_file_name;
     constant con1 : integer := 0;
     signal   sig1 : std_logic_vector;
  begin

  end;

  constant con2 : integer := 100;
  signal sig2 : integer := 20;

begin

  PROC1 : process (A) is
  
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

  begin

  end process PROC1;

end architecture ARCH;

package TEST_PKG is

  constant con2 : integer := 100;
  signal sig2 : integer := 20;

  function func_1 (
    constant a : integer;
    signal b : integer;
    signal c : unsigned(3 downto 0);
    signal d : std_logic_vector(7 downto 0);
    constant e : std_logic)
  return integer;

  function func_1 (
    constant a : integer;
    signal   b : integer;
    signal   c : unsigned(3 downto 0);
    signal   d : std_logic_vector(7 downto 0);
    constant e : std_logic)
  return integer;

  constant con2 : integer := 100;
  signal sig2 : integer := 20;

  -- Check alignment of closing parenthesis
  function MAX (
    constant A : natural := 0;
    signal B : natural := 0
  ) return natural;

  constant con2 : integer := 100;
  signal sig2 : integer := 20;

  function MAX (
    constant A : natural := 0;
    signal   B : natural := 0
  ) return natural;

  constant con2 : integer := 100;
  signal sig2 : integer := 20;

end package TEST_PKG;


package body TEST_PKG_BODY is

  constant con2 : integer := 100;
  signal sig2 : integer := 20;

  constant con2 : integer := 100;
  signal sig2 : integer := 20;

  function func_1 (
     constant a : integer;
     signal    b : integer;
     signal c : unsigned(3 downto 0);
     signal  d : std_logic_vector(7 downto 0);
     constant e : std_logic) return integer is
     file file1 : load_file_type open read_mode is load_file_name;
     constant con1 : integer := 0;
     signal sig1 : std_logic_vector;
  begin

  end;

  --- This should pass
  function func_1 (
     constant a : integer;
     signal   b : integer;
     signal   c : unsigned(3 downto 0);
     signal   d : std_logic_vector(7 downto 0);
     constant e : std_logic) return integer is
     file     file1 : load_file_type open read_mode is load_file_name;
     constant con1 : integer := 0;
     signal   sig1 : std_logic_vector;
  begin

  end;

end package body TEST_PKG_BODY;
