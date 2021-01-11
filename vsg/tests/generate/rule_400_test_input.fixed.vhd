
architecture RTL of FIFO is

begin

  FOR_LABEL : for i in 0 to 7 generate

    signal          sig1 : std_logic;
    constant        con1 : std_logic;
    shared variable var1 : std_logic;

  begin

  end generate;

  IF_LABEL : if a = '1' generate

    signal          sig1 : std_logic;
    constant        con1 : std_logic;
    shared variable var1 : std_logic;

  begin

  end generate;

  CASE_LABEL : case data generate

    when a = 1 =>

        signal          sig1 : std_logic;
        constant        con1 : std_logic;
        shared variable var1 : std_logic;

      begin

  end generate;

  -- Violations below

  FOR_LABEL : for i in 0 to 7 generate

    signal          sig1 : std_logic;
    constant        con1 : std_logic;
    shared variable var1 : std_logic;

  begin

  end generate;

  IF_LABEL : if a = '1' generate

    signal                sig1 : std_logic;
    constant    con1 : std_logic;
    shared variable    var1 : std_logic;

  begin

  end generate;

  CASE_LABEL : case data generate

    when a = 1 =>

        signal  sig1 : std_logic;
        constant             con1 : std_logic;
        shared variable   var1 : std_logic;

      begin

  end generate;


end;
