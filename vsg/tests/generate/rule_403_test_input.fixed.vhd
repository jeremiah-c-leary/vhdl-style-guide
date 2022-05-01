
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

end;
