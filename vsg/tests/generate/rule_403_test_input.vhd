
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

architecture nested of fifo is begin

  g_0 : if true generate
    g_1 : if true generate
        signal sig0      : bit;
        signal sig00   : bit;
    begin end generate g_1;

  elsif true generate

    g_2a : if true generate
        g_2 : if true generate
            signal sig0      : bit;
            signal sig00   : bit;
        begin end generate g_2;
    end generate g_2a;

  elsif true generate

    g_3 : if true generate
        signal sig0      : bit;
        signal sig00   : bit;
    begin

        G_X : if true generate

        end generate G_X;

    end generate g_3;

  else generate

    g_4a : if true generate
        g_4 : if true generate
            signal sig0      : bit;
            signal sig00   : bit;
        begin end generate g_4;
    end generate g_4a;

  end generate g_0;

end architecture fifo;
