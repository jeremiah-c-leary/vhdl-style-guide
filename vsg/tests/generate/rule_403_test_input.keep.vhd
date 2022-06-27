
architecture RTL of FIFO is

begin

  IF_LABEL : if a = '1' generate

    signal          signal1 : std_logic;
    constant        con1    : std_logic;
    shared variable var1    : std_logic;
    alias           a       is name;
    alias           a       : subtype_indication is name;

  begin

  elsif b = '0' generate

    signal          sig1      : std_logic;
    constant        constant1 : std_logic;
    shared variable var1      : std_logic;
    alias           a         is name;
    alias           a         : subtype_indication is name;

  begin

  else generate

    signal          sig1  : std_logic;
    constant        con1  : std_logic;
    shared variable vars1 : std_logic;
    alias           a     is name;
    alias           a     : subtype_indication is name;

  begin

  end generate;

  -- Violations below

  IF_LABEL : if a = '1' generate

    signal          signal1: std_logic;
    constant        con1     : std_logic;
    shared variable var1 : std_logic;
    alias           a is name;
    alias           a                 : subtype_indication is name;

  begin

  elsif b = '0' generate

    signal          sig1   : std_logic;
    constant        constant1: std_logic;
    shared variable var1         : std_logic;
    alias           a is name;
    alias           a                 : subtype_indication is name;

  begin

  else generate

    signal          sig1       : std_logic;
    constant        con1    : std_logic;
    shared variable vars1: std_logic;
    alias           a is name;
    alias           a                 : subtype_indication is name;

  begin

  end generate;

end;

--- Test nested generates

architecture nested of fifo is

begin

  g_0 : if true generate
    g_1 : if true generate
        signal sig0      : bit;
        signal sig00   : bit;
    begin end generate g_1;
  end generate g_0;

end architecture fifo;
