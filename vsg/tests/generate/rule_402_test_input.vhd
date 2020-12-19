
architecture RTL of FIFO is

begin

  IF_LABEL : if a = '1' generate

    signal          sig1 : std_logic;
    constant        con1 : std_logic;
    shared variable var1 : std_logic;

  begin

  elsif b = '0' generate

    signal          sig1 : std_logic;
    constant        con1 : std_logic;
    shared variable var1 : std_logic;

  begin

  else generate

    signal          sig1 : std_logic;
    constant        con1 : std_logic;
    shared variable var1 : std_logic;

  begin

  end generate;

  -- Violations below

  IF_LABEL : if a = '1' generate

    signal sig1 : std_logic;
    constant con1 : std_logic;
    shared variable        var1 : std_logic;

  begin

  elsif b = '0' generate

    signal                   sig1 : std_logic;
    constant             con1 : std_logic;
    shared variable  var1 : std_logic;

  begin

  else generate

    signal      sig1 : std_logic;
    constant       con1 : std_logic;
    shared variable  var1 : std_logic;

  begin

  end generate;

end;
