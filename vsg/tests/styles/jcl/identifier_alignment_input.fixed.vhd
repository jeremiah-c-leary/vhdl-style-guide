
architecture ARCH of ENTITY1 is

  constant con1   : integer;
  signal   sig1   : std_logic; -- Sig
  file     file1  : load_file_file open read_mode is load_file_name;

  constant con12  : integer;
  signal   sig12  : std_logic;
  file     file12 : load_file_file open read_mode is load_file_name;

  -- This should not fail
  constant con12  : integer;
  signal   sig12  : std_logic;
  file     file12 : load_file_file open read_mode is load_file_name;
  
begin

  PROC1 : process (A) is

    variable var1   : boolean; 
    constant con1   : integer := 1;
    file     file1  : load_file_file open read_mode is load_file_name; -- 1
    variable var12  : boolean;
    constant con12  : integer;
    file     file12 : load_file_file open read_mode is load_file_name; -- 2

  begin

  end process PROC1;

  PROC1 : process (A) is

    variable var1  : boolean;
    constant con1  : integer;
    file     file1 : load_file_file open read_mode is load_file_name;  -- 3

    variable var12  : boolean;
    constant con12  : integer;
    file     file12 : load_file_file open read_mode is load_file_name; -- 4

  begin

  end process PROC1;

  -- This should not fail
  PROC1 : process (A) is

    variable var1  : boolean;
    constant con1  : integer;
    file     file1 : load_file_file open read_mode is load_file_name;  -- 5

    variable var12  : boolean;
    constant con12  : integer;
    file     file12 : load_file_file open read_mode is load_file_name; -- 6

  begin

  end process PROC1;

  PROC1 : process (A) is

    variable var1  : boolean;
    constant con1  : integer := 1;
    file     file1 : load_file_file open read_mode is load_file_name; -- 7

    procedure test_p (x: integer) is
      variable a, b : integer;
    begin
    end procedure

    variable var1  : boolean;
    constant con1  : integer := 1;
    file     file1 : load_file_file open read_mode is load_file_name; -- 8

    function test_f (
      x: integer) is
      variable c, d : integer;
    begin
    end function;

    variable var1  : boolean;
    constant con1  : integer := 1;
    file     file1 : load_file_file open read_mode is load_file_name; -- 9

  begin

  end process PROC1;

  PROC1 : process (a) is

    variable a, b : integer;
    variable c    : integer;

  begin

  end process PROC1;

end architecture ARCH;

