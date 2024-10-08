
architecture RTL of FIFO is

  -- Examples adapted from those given in the LRM.

  constant c_test : std_logic_vector := B"1111_1111_1111"; -- Equivalent to the string literal "111111111111".
  constant c_test : std_logic_vector := X"FFF";            -- Equivalent to B"1111_1111_1111".
  constant c_test : std_logic_vector := O"777";            -- Equivalent to B"111_111_111".
  constant c_test : std_logic_vector := X"777";            -- Equivalent to B"0111_0111_0111".
  constant c_test : std_logic_vector := B"XXXX_01LH";      -- Equivalent to the string literal "XXXX01LH"
  constant c_test : unsigned         := UO"27";            -- Equivalent to B"010_111"
  constant c_test : unsigned         := UO"2C";            -- Equivalent to B"011_CCC"
  constant c_test : signed           := SX"3W";            -- Equivalent to B"0011_WWWW"
  constant c_test : std_logic_vector := D"35";             -- Equivalent to B"100011"
  constant c_test : std_logic_vector := 12UB"X1";          -- Equivalent to B"0000_0000_00X1"
  constant c_test : std_logic_vector := 12SB"X1";          -- Equivalent to B"XXXX_XXXX_XXX1"
  constant c_test : unsigned         := 12UX"F-";          -- Equivalent to B"0000_1111_----"
  constant c_test : signed           := 12SX"F-";          -- Equivalent to B"1111_1111_----"
  constant c_test : std_logic_vector := 12D"13";           -- Equivalent to B"0000_0000_1101"
  constant c_test : unsigned         := 12UX"000WWW";      -- Equivalent to B"WWWW_WWWW_WWWW"
  constant c_test : signed           := 12SX"FFFC00";      -- Equivalent to B"1100_0000_0000"
  constant c_test : signed           := 12SX"XXXX00";      -- Equivalent to B"XXXX_0000_0000"
  constant c_test : std_logic_vector := 8D"511";           -- Error
  constant c_test : unsigned         := 8UO"477";          -- Error
  constant c_test : signed           := 8SX"0FF";          -- Error
  constant c_test : signed           := 8SX"FXX";          -- Error
  constant c1: STRING := B"1111_1111_1111";
  constant c2: BIT_VECTOR := X"FFF";

  type MVL is ('X', '0', '1', 'Z');
  type MVL_VECTOR is array (NATURAL range <>) of MVL;
  constant c3: MVL_VECTOR := O"777";

begin

  assert c1'LENGTH = 12 and c2'LENGTH = 12 and c3 = "111111111";

  signal_b  <= B"01uxzwlh-";
  signal_sb <= sB"01uxzwlh-";
  signal_ub <= uB"01uxzwlh-";
  signal_o  <= O"01234567uxzwlh-";
  signal_so <= sO"01234567uxzwlh-";
  signal_uo <= uO"01234567uxzwlh-";
  signal_x  <= X"0123456789abcdefuxzwlh-";
  signal_sx <= sX"0123456789abcdefuxzwlh-";
  signal_ux <= uX"0123456789abcdefuxzwlh-";
  signal_d  <= D"0123456789";

  process (all) is
  begin

    variable_b  := B"01uxzwlh-";
    variable_sb := sB"01uxzwlh-";
    variable_ub := uB"01uxzwlh-";
    variable_o  := O"01234567uxzwlh-";
    variable_so := sO"01234567uxzwlh-";
    variable_uo := uO"01234567uxzwlh-";
    variable_x  := X"0123456789abcdefuxzwlh-";
    variable_sx := sX"0123456789abcdefuxzwlh-";
    variable_ux := uX"0123456789abcdefuxzwlh-";
    variable_d  := D"0123456789";

  end process;

end architecture RTL;
