
package pkg is

  signal          sig1          : std_logic                    := '0';    -- Signal Comment
  constant        default_value : integer                      := 32;     -- Constant Comment
  shared variable var1          : std_logic_vector(3 downto 0) := "0101"; -- Variable Comment

  type t_flag_type is protected body -- protected type declaration

    constant        default_value : integer                      := 32;     -- Constant Comment
    shared variable var1          : std_logic_vector(3 downto 0) := "0101"; -- Variable Comment

  end protected body T_FLAG_TYPE;

end package pkg;

package body pkg_bdy is

  constant        default_value : integer                      := 32; -- Constant Comment
  shared variable var1          : std_logic_vector(3 downto 0) := "0101"; -- Variable Comment

  procedure proc1 is

    constant c : std_logic := '0'; -- Constant Comment
    variable v : integer   := 32; -- Variable Comment

  begin

  end procedure proc1;

  function func1 return integer is

    constant c : integer   := 32; -- Constant Comment
    variable v : std_logic := '1'; -- Variable Comment

  begin

  end function func1;

  type t_flag_type is protected body       -- protected type declaration

    constant        default_value : integer                      := 32; -- Constant Comment
    shared variable var1          : std_logic_vector(3 downto 0) := "0101"; -- Variable Comment

  end protected body T_FLAG_TYPE;

end package body pkg_bdy;

entity ENT is
  signal sig1 : std_logic                             := '0';               -- Signal Comment
  constant default_value : integer                    := 32;                -- Constant Comment
  shared variable var1 : std_logic_vector(3 downto 0) := "0101";            -- Variable Comment

  procedure proc1 is

    constant c : std_logic := '0';                                          -- Constant Comment
    variable v : integer   := 32;                                           -- Variable Comment

  begin

  end procedure proc1;

  function func1 return integer is

    constant c : integer   := 32;                                           -- Constant Comment
    variable v : std_logic := '1';                                          -- Variable Comment

  begin

  end function func1;

  type t_flag_type is protected body                                        -- protected type declaration

    constant        default_value : integer                      := 32;     -- Constant Comment
    shared variable var1          : std_logic_vector(3 downto 0) := "0101"; -- Variable Comment

  end protected body T_FLAG_TYPE;

end entity ENT;

architecture RTL of FIFO is

  signal          sig1          : std_logic                    := '0';      -- Signal Comment
  constant        default_value : integer                      := 32;       -- Constant Comment
  shared variable var1          : std_logic_vector(3 downto 0) := "0101";   -- Variable Comment

  procedure proc1 is

    constant c : std_logic := '0';                                          -- Constant Comment
    variable v : integer   := 32;                                           -- Variable Comment

  begin

  end procedure proc1;

  function func1 return integer is

    constant c : integer   := 32;                                           -- Constant Comment
    variable v : std_logic := '1';                                          -- Variable Comment

  begin

  end function func1;

  type t_flag_type is protected body                                        -- protected type declaration

    constant        default_value : integer                      := 32;     -- Constant Comment
    shared variable var1          : std_logic_vector(3 downto 0) := "0101"; -- Variable Comment

  end protected body T_FLAG_TYPE;

begin

  process is

    constant        default_value : integer                      := 32;       -- Constant Comment
    shared variable var1          : std_logic_vector(3 downto 0) := "0101";   -- Variable Comment

    procedure proc1 is

      constant c : std_logic := '0';                                          -- Constant Comment
      variable v : integer   := 32;                                           -- Variable Comment

    begin

    end procedure proc1;

    function func1 return integer is

      constant c : integer   := 32;                                           -- Constant Comment
      variable v : std_logic := '1';                                          -- Variable Comment

    begin

    end function func1;

    type t_flag_type is protected body                                        -- protected type declaration

      constant        default_value : integer                      := 32;     -- Constant Comment
      shared variable var1          : std_logic_vector(3 downto 0) := "0101"; -- Variable Comment

    end protected body T_FLAG_TYPE;

  begin

  end process;

  block_label : block is

    signal          sig1          : std_logic                    := '0'; -- Signal Comment
    constant        default_value : integer                      := 32; -- Constant Comment
    shared variable var1          : std_logic_vector(3 downto 0) := "0101"; -- Variable Comment

    procedure proc1 is

      constant c : std_logic := '0'; -- Constant Comment
      variable v : integer   := 32; -- Variable Comment

    begin

    end procedure proc1;

    function func1 return integer is

      constant c : integer   := 32; -- Constant Comment
      variable v : std_logic := '1'; -- Variable Comment

    begin

    end function func1;

    type t_flag_type is protected body       -- protected type declaration

      constant        default_value : integer                      := 32; -- Constant Comment
      shared variable var1          : std_logic_vector(3 downto 0) := "0101"; -- Variable Comment

    end protected body T_FLAG_TYPE;

  begin

  end block block_label;

end architecture RTL;
